class GameError(Exception):
    """Base class for exceptions in this game."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidPlayerError(GameError):
    """Exception raised for invalid player operations."""
    def __init__(self, player_name):
        message = f"Player '{player_name}' is invalid."  
        super().__init__(message)

class ItemNotFoundError(GameError):
    """Exception raised when an item is not found."""
    def __init__(self, item_name):
        message = f"Item '{item_name}' not found."  
        super().__init__(message)

class ActionNotAllowedError(GameError):
    """Exception raised when an action isn't allowed."""
    def __init__(self, action):
        message = f"Action '{action}' is not allowed."  
        super().__init__(message)

class LevelUpError(GameError):
    """Exception raised when leveling up goes wrong."""
    def __init__(self, player_name, reason):
        message = f"'{player_name}' cannot level up: {reason}"  
        super().__init__(message)