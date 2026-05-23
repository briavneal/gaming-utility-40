from typing import List, Dict, Any

class Game:
    def __init__(self, name: str, genre: str, rating: float) -> None:
        self.name = name
        self.genre = genre
        self.rating = rating

    def __repr__(self) -> str:
        return f"Game(name={self.name}, genre={self.genre}, rating={self.rating})"

class GameLibrary:
    def __init__(self) -> None:
        self.games: List[Game] = []

    def add_game(self, game: Game) -> None:
        """Add a new game to the library."""
        self.games.append(game)

    def get_game_by_name(self, name: str) -> Game:
        """Retrieve a game by its name."""
        for game in self.games:
            if game.name == name:
                return game
        raise ValueError(f"Game with name '{name}' not found.")

    def get_all_games(self) -> List[Dict[str, Any]]:
        """Return a list of all games in the library."""
        return [{'name': game.name, 'genre': game.genre, 'rating': game.rating} for game in self.games]