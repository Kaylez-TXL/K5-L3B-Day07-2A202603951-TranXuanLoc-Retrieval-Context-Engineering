"""Offline checks for the bonus tool loop; not model-quality measurements."""
import unittest
from src.bonus import run_agent
from src.anthropic_api import ProviderError


class Client:
    def __init__(self, actions):
        self.actions = iter(actions)
        self.transport_events = []
        self.requests = []

    def message(self, **payload):
        self.requests.append(payload)
        name, args = next(self.actions)
        return dict(id='fixture', model='claude-haiku-5-5', stop_reason='tool_use', usage={'input_tokens': 10, 'output_tokens': 2},
                    content=[dict(type='tool_use', id='call', name=name, input=args)]), 1


class Index:
    pages = {1: {}, 2: {}}
    def search(self, query, top_k, caption_boost=False):
        return [dict(page=1, text='Source text', score=.9)]
    def image(self, page, bbox, edge):
        return b'fixture-image', dict(page=page, bbox=bbox, text='Original source text', pixel_size=[100,100], sha256='fixture')


class BonusTests(unittest.TestCase):
    def test_answer_links_to_an_actually_viewed_source_region(self):
        client = Client([('search', {'query':'example'}), ('read', {'page':1,'bbox':[0,0,1,1]}),
                         ('finish', {'answer':'Answer','abstain':False,'citations':[{'region_id':'p001-r1','location':'Figure A, upper panel'}]})])
        trace = run_agent('Question', client, Index(), 'compact', 'claude-haiku-5-5')
        self.assertEqual(trace['status'], 'answered')
        self.assertEqual(trace['citations'][0]['page'], 1)
        self.assertEqual(trace['citations'][0]['bbox'], [0,0,1,1])
        self.assertTrue(any(b['type']=='image' for b in client.requests[-1]['messages'][-1]['content'][0]['content']))

    def test_cannot_cite_an_unviewed_page(self):
        client = Client([('search', {'query':'example'}),
                         ('finish', {'answer':'Answer','abstain':False,'citations':[{'region_id':'p099-r1','location':'invented'}]})])
        self.assertEqual(run_agent('Question',client,Index(),'compact','claude-haiku-5-5')['status'], 'error')

    def test_read_is_limited_to_retrieved_pages_and_immediate_neighbors(self):
        client = Client([('search', {'query':'example'}), ('read', {'page':99,'bbox':[0,0,1,1]})])
        trace = run_agent('Question',client,Index(),'compact','claude-haiku-5-5')
        self.assertEqual(trace['status'], 'error')
        self.assertEqual(trace['regions'], [])

    def test_abstention_does_not_repeat_unverified_model_claims(self):
        client = Client([('search', {'query':'example'}), ('finish', {'answer':'Unverified claim','abstain':True,'citations':[]})])
        trace = run_agent('Question',client,Index(),'compact','claude-haiku-5-5')
        self.assertEqual(trace['status'], 'abstain')
        self.assertNotIn('Unverified', trace['answer'])

    def test_thorough_retries_a_network_failure_and_keeps_its_record(self):
        class Flaky(Client):
            def __init__(self):
                super().__init__([('search',{'query':'example'}),('finish',{'answer':'unknown','abstain':True,'citations':[]})])
                self.failed = False
            def message(self, **payload):
                if not self.failed:
                    self.failed = True
                    raise ProviderError('Anthropic connection failure (TimeoutError)')
                return super().message(**payload)
        trace = run_agent('Question',Flaky(),Index(),'thorough','claude-haiku-5-5')
        self.assertEqual(trace['status'], 'abstain')
        self.assertEqual(len(trace['request_errors']), 1)
        self.assertEqual(len(trace['model_calls']), 2)

    def test_configuration_errors_are_not_retried(self):
        class Broken(Client):
            def __init__(self): super().__init__([])
            def message(self, **payload): raise ProviderError('Anthropic HTTP 400; request_id=fixture')
        trace = run_agent('Question',Broken(),Index(),'thorough','claude-haiku-5-5')
        self.assertEqual(trace['status'], 'error')
        self.assertEqual(len(trace['request_errors']), 1)

    def test_focused_removes_only_the_known_serialization_footer(self):
        client = Client([('search', {'query':'example'}), ('read', {'page':1,'bbox':[0,0,1,1]}),
                         ('finish', {'answer':'42.</answer>\n<parameter name="abstain">false','abstain':False,
                                     'citations':[{'region_id':'p001-r1','location':'Table A, row 1'}]})])
        trace = run_agent('Question',client,Index(),'focused','claude-haiku-5-5')
        self.assertEqual(trace['status'], 'answered')
        self.assertEqual(trace['answer'], '42.')
        self.assertIn('Answer in English',client.requests[-1]['system'])


if __name__ == '__main__':
    unittest.main()
