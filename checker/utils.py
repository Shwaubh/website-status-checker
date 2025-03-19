import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def get_session():
    session = requests.Session()
    retires = Retry(
        total=3,
        backoff_factor=0.5
    )
    adapter = HTTPAdapter(max_retries=retires)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session