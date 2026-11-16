"""Small Anthropic Messages client; never log credentials/provider error bodies."""
import json
import os
import time
import urllib.error
import urllib.request


class ProviderError(RuntimeError):
    pass


class AnthropicClient:
    def __init__(self, key=None, *, timeout=60):
        self.key = key or os.environ.get('ANTHROPIC_API_KEY')
        if not self.key:
            raise ProviderError('ANTHROPIC_API_KEY is missing')
        self.timeout = timeout
        self.transport_events = []

    def request(self, path, payload=None):
        request = urllib.request.Request(
            'https://api.anthropic.com/v1/' + path,
            data=json.dumps(payload).encode('utf-8') if payload is not None else None,
            headers={'x-api-key': self.key, 'anthropic-version': '2023-06-01',
                     'content-type': 'application/json'})
        started = time.perf_counter()
        for attempt in range(2):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    body = json.load(response)
                break
            except urllib.error.HTTPError as exc:
                # Error bodies may echo request values; record status and request ID only.
                raise ProviderError(f'Anthropic HTTP {exc.code}; request_id={exc.headers.get("request-id", "unknown")}') from None
            except urllib.error.URLError as exc:
                category = type(exc.reason).__name__
                self.transport_events.append(dict(path=path.split('?')[0], failure=category, attempt=attempt+1,
                                                   elapsed_ms=(time.perf_counter()-started)*1000))
                # DNS failure occurs before a request reaches the provider. Retry
                # it once; do not silently repeat potentially billed timeouts.
                if category == 'gaierror' and attempt == 0:
                    continue
                raise ProviderError(f'Anthropic connection failure ({category})') from None
            except TimeoutError:
                self.transport_events.append(dict(path=path.split('?')[0], failure='TimeoutError', attempt=attempt+1))
                raise ProviderError('Anthropic request timed out') from None
        return body, (time.perf_counter() - started) * 1000

    def models(self):
        rows = []
        path = 'models?limit=100'
        while True:
            body, _ = self.request(path)
            rows.extend(body.get('data', []))
            if not body.get('has_more'):
                return rows
            path = 'models?limit=100&after_id=' + body['last_id']

    def message(self, **payload):
        return self.request('messages', payload)


if __name__ == '__main__':
    from pathlib import Path
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parents[1] / '.env')
    try:
        print(json.dumps([dict(id=m['id'], display_name=m.get('display_name'))
                          for m in AnthropicClient().models()], ensure_ascii=False, indent=2))
    except ProviderError as exc:
        print(str(exc))
        raise SystemExit(1)
