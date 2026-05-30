import time
import random

class NetworkError(Exception):
    pass

def retry_network_operation(op, retries=5, delay=2):
    attempt = 0
    while attempt < retries:
        try:
            return op()
        except NetworkError as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            time.sleep(delay)
            attempt += 1
    raise Exception('Max retries exceeded')

def simulated_network_operation():
    if random.choice([True, False]):
        raise NetworkError('Simulated network failure')
    return 'Network operation successful!'

if __name__ == '__main__':
    try:
        result = retry_network_operation(simulated_network_operation)
        print(result)
    except Exception as e:
        print(e)