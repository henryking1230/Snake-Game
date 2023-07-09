import random

from config import *

class Food:
    """
    Creates a food object in a random location for the snake to eat.
    """

    def __init__(self, canvas):
        
        # randomizes location for new food
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x,y]
        
        # Displays the food on screen
        canvas.create_oval(x,y,x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")