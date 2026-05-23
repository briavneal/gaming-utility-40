def validate_username(username):
    if not isinstance(username, str):
        raise ValueError("Username must be a string.")
    if not (3 <= len(username) <= 20):
        raise ValueError("Username must be between 3 and 20 characters.")
    if not username.isalnum():
        raise ValueError("Username must be alphanumeric.")


def validate_score(score):
    if not isinstance(score, int):
        raise ValueError("Score must be an integer.")
    if score < 0:
        raise ValueError("Score must be a non-negative integer.")


def validate_level(level):
    if not isinstance(level, int):
        raise ValueError("Level must be an integer.")
    if level < 1:
        raise ValueError("Level must be at least 1.")


def main_loop():
    users = []
    while True:
        username = input("Enter your username: ")
        try:
            validate_username(username)
        except ValueError as e:
            print(e)
            continue

        score = input("Enter your score: ")
        try:
            validate_score(int(score))
        except ValueError as e:
            print(e)
            continue

        level = input("Enter your level: ")
        try:
            validate_level(int(level))
        except ValueError as e:
            print(e)
            continue

        users.append((username, score, level))
        print(f"User {username} with score {score} and level {level} added.")

        if input("Add another user? (y/n): ").lower() != 'y':
            break


if __name__ == '__main__':
    main_loop()