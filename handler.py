import random
import time

class GameHandler:
    def __init__(self, players):
        self.players = players
        self.scores = {player: 0 for player in players}

    def play_round(self):
        results = {player: random.randint(1, 10) for player in self.players}
        self.update_scores(results)
        return results

    def update_scores(self, results):
        for player, score in results.items():
            self.scores[player] += score

    def get_winner(self):
        winner = max(self.scores, key=self.scores.get)
        return winner, self.scores[winner]

    def display_scores(self):
        print("Current Scores:")
        for player, score in self.scores.items():
            print(f"{player}: {score}")

if __name__ == '__main__':
    game = GameHandler(['Alice', 'Bob', 'Charlie'])
    for _ in range(5):
        game.play_round()
        game.display_scores()
        time.sleep(1)
    winner, score = game.get_winner()
    print(f"Winner: {winner} with score {score}")