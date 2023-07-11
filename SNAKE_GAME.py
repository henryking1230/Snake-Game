import tkinter as tk
import random

from config import *
from snake import *
from food import *
from check_collisions import *
from game_over import *

def next_turn(snake, food):
    
    # Moves the snake body.
    # Makes necessary changes if food is eaten.
    
    x, y = snake.coordinates[0]
    
    # Move snake body in correct direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
        
    snake.coordinates.insert(0, (x,y))
    
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
    
    snake.squares.insert(0, square)

    # if the snake ran into food
    if x == food.coordinates[0] and y == food.coordinates[1]:

        # increase the score by 1 point and update display
        global score
        score += 1
        label.config(text="Score:{}".format(score))

        # delete the food that was eaten and make new food
        canvas.delete("food")
        food = Food(canvas)

    # if no food eaten then move snake normally
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # end game if snake ran into wall or itself
    if check_collisions(snake):
        game_over(canvas)

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    
    #Uses user input to change snake direction.
    #Does not allow 180 degree turns.

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction


# Create game window with a fixed size
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

# Set starting score to '0' and movement direction to 'down'
score = 0
direction = 'down'

# Create score display
label = tk.Label(window, text="Score:{}".format(score), font=('consolas', 50))
label.pack()

# Set background color and window size
canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Center the window on computer screen
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Define user inputs for changing direction of snake
window.bind('<a>', lambda event: change_direction('left'))
window.bind('<d>', lambda event: change_direction('right'))
window.bind('<w>', lambda event: change_direction('up'))
window.bind('<s>', lambda event: change_direction('down'))
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Create snake and first food object
snake = Snake(canvas)
food = Food(canvas)

next_turn(snake, food)

window.mainloop()