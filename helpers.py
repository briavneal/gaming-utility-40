import json
import random

class GamingDataHandler:
    def __init__(self, data=None):
        self.data = data or []

    def load_data_from_json(self, file_path):
        with open(file_path, 'r') as file:
            self.data = json.load(file)

    def save_data_to_json(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def random_game_selector(self):
        if not self.data:
            return None
        return random.choice(self.data)

    def filter_games_by_genre(self, genre):
        return [game for game in self.data if game.get('genre') == genre]

    def update_game_rating(self, game_title, new_rating):
        for game in self.data:
            if game.get('title') == game_title:
                game['rating'] = new_rating
                return game
        return None

    def get_all_titles(self):
        return [game.get('title') for game in self.data]