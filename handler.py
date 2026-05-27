import time
import random
import requests

def retry_request(url, max_retries=5, backoff_factor=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Parse JSON if successful
        except requests.exceptions.RequestException as e:
            retries += 1
            wait_time = backoff_factor * (2 ** (retries - 1)) + random.uniform(0, 1)
            print(f'Attempt {retries} failed: {e}. Retrying in {wait_time:.2f} seconds...')
            time.sleep(wait_time)
    raise Exception('Max retries exceeded')

# Example usage:
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(data)
    except Exception as e:
        print(f'Failed to retrieve data: {e}')