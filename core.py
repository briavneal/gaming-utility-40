import random

class GameUtility:
    @staticmethod
    def roll_dice(sides=6):
        return random.randint(1, sides)

    @staticmethod
    def generate_random_number(minimum, maximum):
        return random.randint(minimum, maximum)

    @staticmethod
    def shuffle_list(items):
        random.shuffle(items)
        return items

    @staticmethod
    def choose_random_item(items):
        return random.choice(items)

    @staticmethod
    def is_valid_choice(choice, valid_options):
        return choice in valid_options

if __name__ == '__main__':
    utility = GameUtility()
    print(f'Rolled Dice: {utility.roll_dice()}')
    print(f'Random Number: {utility.generate_random_number(1, 100)}')
    items = [1, 2, 3, 4, 5]
    print(f'Shuffled List: {utility.shuffle_list(items)}')
    print(f'Chosen Item: {utility.choose_random_item(items)}')
    print(f'Is valid choice: {utility.is_valid_choice(3, items)}')