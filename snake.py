from config import *

class Snake:
    """
    The snake's body length and location
    """
    
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        # Creates the correct number of body segments
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        # Creats the snake display
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)