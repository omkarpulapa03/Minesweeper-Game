import tkinter as tk
import random

# Define constants
WIDTH = 20
HEIGHT = 20
MINES = 10


class MinesweeperGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Minesweeper")
        self.buttons = []
        self.mines = set()
        self.game_over = False
        self.create_board()

    def create_board(self):
        # Create buttons for each square
        for i in range(WIDTH):
            row = []
            for j in range(HEIGHT):
                button = tk.Button(self.master, width=2, height=1,
                                   command=lambda i=i, j=j: self.handle_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        # Add mines to the board
        while len(self.mines) < MINES:
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            if (x, y) not in self.mines:
                self.mines.add((x, y))

    def handle_click(self, x, y):
        if self.game_over:
            return

        # If the square has a mine, end the game
        if (x, y) in self.mines:
            self.end_game()
            return

        # Otherwise, reveal the square
        self.reveal_square(x, y)

    def reveal_square(self, x, y):
        if (x, y) in self.mines:
            return

        # Count the number of mines in adjacent squares
        mines = 0
        for i in range(max(0, x - 1), min(x + 2, WIDTH)):
            for j in range(max(0, y - 1), min(y + 2, HEIGHT)):
                if (i, j) in self.mines:
                    mines += 1

        # Update the square's text
        button = self.buttons[x][y]
        if mines > 0:
            button.config(text=str(mines))
        else:
            button.config(relief=tk.SUNKEN)

            # Reveal adjacent squares
            for i in range(max(0, x - 1), min(x + 2, WIDTH)):
                for j in range(max(0, y - 1), min(y + 2, HEIGHT)):
                    if (i, j) not in self.mines:
                        self.reveal_square(i, j)

    def end_game(self):
        self.game_over = True

        # Reveal all mines
        for x, y in self.mines:
            self.buttons[x][y].config(relief=tk.SUNKEN, text="*")

        # Display a message box
        tk.messagebox.showinfo("Game Over", "You hit a mine!")


# Start the game
root = tk.Tk()
game = MinesweeperGame(root)
root.mainloop()
