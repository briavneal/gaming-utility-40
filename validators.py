import re

def is_valid_username(username):
    return re.match('^[A-Za-z0-9_]{3,16}$', username) is not None

def is_valid_email(email):
    regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    return re.match(regex, email) is not None

def is_valid_password(password):
    return (len(password) >= 8 and 
            re.search('[A-Z]', password) and 
            re.search('[a-z]', password) and 
            re.search('[0-9]', password) and 
            re.search('[^A-Za-z0-9]', password))

def is_valid_game_id(game_id):
    return isinstance(game_id, int) and game_id > 0

if __name__ == '__main__':
    # Test our validators
    print(is_valid_username('GameHero'))  # True
    print(is_valid_email('player@example.com'))  # True
    print(is_valid_password('P@ssw0rd!'))  # True
    print(is_valid_game_id(42))  # True
