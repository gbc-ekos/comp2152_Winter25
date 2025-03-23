# Define two Dice
import random

small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

def small_roll():
    return random.choice(small_dice_options)

def big_roll():
    return random.choice(big_dice_options)
