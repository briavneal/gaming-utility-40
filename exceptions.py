class InputValidationError(Exception):
    """Custom exception for input validation errors."""  

class GameInput:
    def __init__(self):
        self.user_input = None

    def get_input(self):
        self.user_input = input("Enter your move (e.g., 'a1', 'b2'): ")
        if not self.validate_input(self.user_input):
            raise InputValidationError(f"Invalid input: {self.user_input}")
        return self.user_input

    def validate_input(self, user_input):
        valid_moves = {'a1', 'a2', 'b1', 'b2'}  
        return user_input in valid_moves

if __name__ == '__main__':
    game_input = GameInput()
    try:
        move = game_input.get_input()
        print(f"You chose: {move}")
    except InputValidationError as e:
        print(e)  
        print("Please enter a valid move.")