"""Offline behavior tests; these are not evidence of real agent quality."""
import json
import unittest
from src.agent import run_agent
from src.retrieval import HybridRetriever, LexicalRetriever, reciprocal_rank_fusion
from src.evaluation import context_has_evidence, evidence_hit, summarize
from src.pricing import estimate_cost


def chunk(cid, text, chapter=1):
    return dict(id=cid, text=text, source_id='fixture', source='fixture.txt', page=1,
                metadata={'chapter': chapter}, score=0.9)


class Client:
    def __init__(self, actions):
        self.actions = iter(actions)
        self.requests = []

    def message(self, **payload):
        self.requests.append(payload)
        name, args = next(self.actions)
        return dict(id='message-fixture', model='fixture-model', stop_reason='tool_use',
                    usage={'input_tokens': 10, 'output_tokens': 5},
                    content=[dict(type='tool_use', id='call-fixture', name=name, input=args)]), 1.0


class PipelineTests(unittest.TestCase):
    def test_context_only_joins_contiguous_source_offsets(self):
        a, b = chunk('a', 'alpha beta'), chunk('b', 'beta gamma')
        a['metadata'].update(char_start=0, char_end=10)
        b['metadata'].update(char_start=6, char_end=16)
        gold = [dict(source_id='fixture', page=1, evidence='alpha beta gamma')]
        self.assertFalse(evidence_hit(a, gold))
        self.assertTrue(context_has_evidence([b, a], gold))
        b['metadata'].update(char_start=20, char_end=30)
        self.assertFalse(context_has_evidence([a, b], gold))
        b['metadata'].update(char_start=6, char_end=16)
        b['page'] = 2
        self.assertFalse(context_has_evidence([a, b], gold))

    def test_cost_estimate_is_per_model_call(self):
        self.assertAlmostEqual(estimate_cost([dict(model='claude-haiku-5-5', usage={'input_tokens': 1000, 'output_tokens': 100})]), .00015)
        self.assertIsNone(estimate_cost([dict(model='unknown', usage={})]))

    def test_error_cases_stay_in_evidence_denominator(self):
        record = dict(query_id='q', answerable=True, original_hit1=True, original_hit3=True,
                      original_context_evidence=True, agent_context_evidence=True,
                      agent=dict(status='error', events=[], model_calls=[], cost_usd=0, elapsed_ms=1))
        summary = summarize([record])
        self.assertEqual(summary['agent_context_evidence'], {'n': 0, 'N': 1, 'rate': 0.0})
        self.assertEqual(summary['errors'], 1)
        self.assertEqual(summary['tool_use']['N'], 0)

    def test_rrf_agreement_beats_single_retriever_and_ignores_score_scales(self):
        a, b, c = [chunk(x, x) for x in 'abc']
        a['score'], b['score'], c['score'] = 1000, .0001, 900
        rows = reciprocal_rank_fusion({'dense': [a, b], 'tfidf': [c, b]})
        self.assertEqual(rows[0]['id'], 'b')
        self.assertEqual(rows[0]['component_ranks'], {'dense': 2, 'tfidf': 2})
        self.assertEqual(len({r['id'] for r in rows}), 3)

    def test_lexical_filters_before_cutoff(self):
        index = LexicalRetriever([chunk('a', 'vàng vàng', 1), chunk('b', 'vàng bạc', 2)])
        self.assertEqual(index.search('vàng', filters={'chapter': 2}, top_k=1)[0]['id'], 'b')
        with self.assertRaises(ValueError):
            index.search('vàng', filters={'chapter': True})

    def test_hybrid_records_components_and_propagates_dense_failure(self):
        lexical = LexicalRetriever([chunk('a', 'vàng')])
        class Broken:
            def search(self, *args, **kwargs):
                raise ConnectionError('fixture outage')
        with self.assertRaises(ConnectionError):
            HybridRetriever(Broken(), lexical).search('vàng')

    def test_model_search_answer_and_token_accounting(self):
        client = Client([('search', {'query': 'vàng'}), ('finish', {'answer': 'Vàng [a]', 'citations': ['a'], 'abstain': False})])
        trace = run_agent('Kim loại nào?', client, LexicalRetriever([chunk('a', 'vàng')]), model='fixture')
        self.assertEqual(trace['status'], 'answered')
        self.assertEqual(trace['usage'], {'input_tokens': 20, 'output_tokens': 10})
        self.assertEqual(client.requests[0]['tool_choice']['name'], 'search')
        self.assertEqual(trace['events'][0]['query'], 'vàng')

    def test_invalid_or_unlisted_citation_is_rejected(self):
        for answer, citations in [('Vàng [other]', ['other']), ('Vàng [a] [other]', ['a']), ('Vàng', ['a'])]:
            client = Client([('search', {'query': 'vàng'}), ('finish', dict(answer=answer, citations=citations, abstain=False))])
            trace = run_agent('Kim loại?', client, LexicalRetriever([chunk('a', 'vàng')]), model='fixture')
            self.assertEqual(trace['status'], 'abstain')
            self.assertEqual(trace['stop_reason'], 'invalid_citations')

    def test_latest_context_budget_and_final_search_limit(self):
        class Retriever:
            def __init__(self): self.i = 0
            def search(self, *args, **kwargs):
                self.i += 1
                return [chunk(str(self.i), 'vàng ' * 10)]
        client = Client([('search', {'query': 'one'}), ('search', {'query': 'two'}),
                         ('finish', dict(answer='Vàng [2]', citations=['2'], abstain=False))])
        trace = run_agent('Kim loại?', client, Retriever(), model='fixture', max_searches=2, budget=100)
        self.assertEqual(trace['status'], 'answered')
        self.assertEqual(trace['context_ids'], ['2'])
        self.assertEqual([t['name'] for t in client.requests[-1]['tools']], ['finish'])
        for request in client.requests[1:]:
            result = json.loads(request['messages'][-1]['content'][0]['content'])
            self.assertLessEqual(len(result['context']), 100)
            self.assertEqual(len(request['messages']), 3)

    def test_abstention_and_failure_keep_truthful_status(self):
        client = Client([('search', {'query': 'unknown'}), ('finish', dict(answer='Không biết', citations=[], abstain=True))])
        trace = run_agent('unknown', client, LexicalRetriever([chunk('a', 'vàng')]), model='fixture')
        self.assertEqual(trace['status'], 'abstain')
        class BrokenClient:
            def message(self, **payload): raise RuntimeError('private value should not appear')
        trace = run_agent('q', BrokenClient(), None, model='fixture')
        self.assertEqual(trace['status'], 'error')
        self.assertNotIn('private value', json.dumps(trace))

    def test_explicit_abstention_discards_malformed_provider_free_text(self):
        client = Client([('search', {'query': 'unknown'}), ('finish', dict(answer='malformed untrusted text', abstain=True))])
        trace = run_agent('unknown', client, LexicalRetriever([chunk('a', 'vàng')]), model='fixture')
        self.assertEqual(trace['status'], 'abstain')
        self.assertEqual(trace['citations'], [])
        self.assertNotIn('malformed', trace['answer'])


if __name__ == '__main__':
    unittest.main()
