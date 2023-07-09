
from config import *

def check_collisions(snake):
    
    #Ends game if snake head runs into window border or snake body.
    #Returns 'True' if collision, 'False' if no collision.
    

    x, y = snake.coordinates[0]

    # if snake runs into game border
    if x < 0 or x >= GAME_WIDTH:
        print("GAME OVER")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("GAME OVER")
        return True

    # if snake runs into itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME_OVER")
            return True

    return False