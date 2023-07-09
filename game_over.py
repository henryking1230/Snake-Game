import tkinter as tk

def game_over(canvas):
    """
    Ends game and displays 'Game Over' screen.
    """

    canvas.delete(tk.ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font = ('consolas', 70),
                       text = "GAME OVER", fill = "red", tag = "gameover")
