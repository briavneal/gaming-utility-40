class GameError(Exception):
    """Custom exception for game-related errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

class PlayerNotFoundError(GameError):
    """Exception raised when a player is not found."""
    def __init__(self, player_id: str) -> None:
        super().__init__(f'Player with ID {player_id} not found.')
        self.player_id = player_id

class InvalidMoveError(GameError):
    """Exception raised for illegal moves in the game."""
    def __init__(self, move: str) -> None:
        super().__init__(f'Invalid move: {move}.')
        self.move = move

class GameStateError(GameError):
    """Exception raised for invalid game state transitions."""
    def __init__(self, state: str) -> None:
        super().__init__(f'Invalid state transition for state: {state}.')
        self.state = state