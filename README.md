# Minesweeper-Game


Minesweeper Game in Python
This is a command-line version of the classic Minesweeper game, implemented in Python.

How to Play
To play the game, simply run the minesweeper.py file using Python 3. The game will prompt you to enter the dimensions of the game board (height and width) and the number of mines to be placed on the board. Once you've entered these values, the game will start and you'll be presented with a board of tiles.

To uncover a tile, enter its coordinates in the format row,column. For example, to uncover the tile in the first row and second column, you would enter 1,2. If the tile contains a mine, you lose the game. If it doesn't, the tile will display a number indicating how many mines are in the adjacent tiles. Use this information to deduce the location of the remaining mines and mark them with flags by entering f followed by the coordinates of the tile.

The game is won when all non-mine tiles have been uncovered.

Features
This Minesweeper game includes the following features:

Customizable game board dimensions and number of mines
Randomized mine placement
Command-line interface with clear instructions and user prompts
Board display using Unicode characters for better readability
Interactive gameplay with uncovering and flagging options
Game over and win conditions with appropriate messaging
Ability to play again with a new game board

Installation
To play this Minesweeper game, simply download the minesweeper.py file and run it using Python 3. No additional dependencies are required.

License
This Minesweeper game is released under the MIT License. See the LICENSE file for details.
