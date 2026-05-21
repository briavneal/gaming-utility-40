class GameException(Exception):
    """Base class for game-related exceptions."""
    pass

class InvalidInputError(GameException):
    """Raised when the input is invalid."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(GameException):
    """Raised when a game resource is not found."""
    def __init__(self, resource):
        self.resource = resource
        self.message = f'Resource {resource} not found'
        super().__init__(self.message)

class GameOverError(GameException):
    """Raised when the game is over."""
    def __init__(self):
        self.message = 'The game is already over'
        super().__init__(self.message)

# Example usage:
if __name__ == '__main__':
    try:
        raise InvalidInputError('Only numbers are accepted.')
    except GameException as e:
        print(e)

    try:
        raise ResourceNotFoundError('Player1')
    except GameException as e:
        print(e)

    try:
        raise GameOverError()
    except GameException as e:
        print(e)