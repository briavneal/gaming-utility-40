import random
import time

def start_game():
    print("Welcome to the game!")
    time.sleep(1)
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Let's start!")
    return player_name

def generate_enemy():
    enemies = ['Goblin', 'Orc', 'Dragon']
    enemy = random.choice(enemies)
    print(f"A wild {enemy} appears!")
    return enemy

def battle(player, enemy):
    print(f"{player} fights the {enemy}!")
    result = random.choice(["won", "lost"])
    print(f"You {result} the battle!")
    return result

def game_loop():
    player = start_game()
    while True:
        enemy = generate_enemy()
        result = battle(player, enemy)
        if result == 'lost':
            print("Game Over!")
            break
        else:
            continue_game = input("Continue? (y/n): ")
            if continue_game.lower() != 'y':
                print("Thanks for playing!")
                break

if __name__ == '__main__':
    game_loop()