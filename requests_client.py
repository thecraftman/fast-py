# requests_client.py
import requests
from opentelemetry.instrumentation.requests import RequestsInstrumentor

# Instrument requests
RequestsInstrumentor().instrument()

def make_request(url):
    response = requests.get(url)
    return response.text

# Additional requests logic
