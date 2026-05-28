import time
import requests

class RetryException(Exception):
    pass

def retry_request(url, retries=3, backoff=2, timeout=5):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            attempt += 1
            if attempt == retries:
                raise RetryException(f'Failed after {retries} attempts') from e
            wait_time = backoff ** attempt
            print(f'Waiting {wait_time} seconds before retrying...')
            time.sleep(wait_time)
