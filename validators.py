import re

class InputValidator:
    @staticmethod
    def validate_username(username):
        pattern = r'^[a-zA-Z0-9_]{3,16}$'
        if re.match(pattern, username):
            return True
        raise ValueError('Invalid username')

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError('Password too short')
        if not re.search(r'[A-Z]', password):
            raise ValueError('Password should include an uppercase letter')
        if not re.search(r'[a-z]', password):
            raise ValueError('Password should include a lowercase letter')
        if not re.search(r'[0-9]', password):
            raise ValueError('Password should include a number')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValueError('Password should include a special character')
        return True

    @staticmethod
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return True
        raise ValueError('Invalid email format')