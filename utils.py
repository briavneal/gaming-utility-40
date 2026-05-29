import time
import random

class NetworkError(Exception):
    pass

def retry_network_operation(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except NetworkError:
                    if attempt < max_retries:
                        wait_time = delay * (2 ** (attempt - 1)) + random.uniform(0, 1)
                        print(f'Attempt {attempt} failed, retrying in {wait_time:.2f} seconds...')
                        time.sleep(wait_time)
                    else:
                        raise
        return wrapper
    return decorator

@retry_network_operation(max_retries=5)
def simulate_network_request():
    if random.random() < 0.7:
        raise NetworkError('Simulated network failure')
    return 'Network request succeeded'

if __name__ == '__main__':
    try:
        result = simulate_network_request()
        print(result)
    except NetworkError as e:
        print(f'Operation failed after retries: {e}')