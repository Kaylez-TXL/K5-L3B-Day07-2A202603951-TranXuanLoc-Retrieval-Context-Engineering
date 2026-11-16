"""Three retrieval methods on the same immutable Day 6 A corpus."""
from starter.baseline import TfidfIndex


def validate_search(query, filters, top_k):
    if not isinstance(query, str) or not query.strip() or type(top_k) is not int or top_k < 1:
        raise ValueError('Nonempty query and positive integer top_k required')
    if filters is not None and (not isinstance(filters, dict) or set(filters) - {'chapter'} or
                                any(type(v) is not int or not 1 <= v <= 5 for v in filters.values())):
        raise ValueError('Only integer chapter filters 1–5 supported')


class LexicalRetriever:
    def __init__(self, chunks):
        self.index = TfidfIndex(chunks)

    def search(self, query, *, filters=None, top_k=3):
        validate_search(query, filters, top_k)
        # Rank all before filtering so a valid filtered result is not lost.
        rows = self.index.search(query, top_k=len(self.index.chunks))
        return [c for c in rows if all(c['metadata'].get(k) == v for k, v in (filters or {}).items())][:top_k]


def reciprocal_rank_fusion(rankings, *, constant=60):
    if constant < 1:
        raise ValueError('RRF constant must be positive')
    merged = {}
    for name, rows in rankings.items():
        seen = set()
        for rank, row in enumerate(rows, 1):
            if row['id'] in seen:
                continue
            seen.add(row['id'])
            item = merged.setdefault(row['id'], {**row, 'score': 0.0, 'strategy': 'hybrid', 'component_ranks': {}})
            item['score'] += 1 / (constant + rank)
            item['component_ranks'][name] = rank
    return sorted(merged.values(), key=lambda c: (-c['score'], c['id']))


class HybridRetriever:
    def __init__(self, dense, lexical, *, candidate_k=10, rrf_constant=60):
        if candidate_k < 1:
            raise ValueError('candidate_k must be positive')
        self.dense, self.lexical = dense, lexical
        self.candidate_k, self.rrf_constant = candidate_k, rrf_constant
        self.last_components = {}

    def search(self, query, *, filters=None, top_k=3):
        validate_search(query, filters, top_k)
        k = max(top_k, self.candidate_k)
        self.last_components = {
            'dense': self.dense.search(query, filters=filters, top_k=k),
            'tfidf': self.lexical.search(query, filters=filters, top_k=k)}
        return reciprocal_rank_fusion(self.last_components, constant=self.rrf_constant)[:top_k]
