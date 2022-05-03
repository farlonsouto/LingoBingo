import random
import tkinter as tk
from functools import partial
from math import sqrt, floor


def loadFromFile():
    """loads the buzz words from the default file buzzwords.lingo, which is expected to be located into the same
    directory where the program is called """
    with open("buzzwords.lingo", "r") as f:
        lines = f.readlines()
    buzzwords = []
    for line in lines:
        split = line.split(",")
        for word in split:
            if word != "\n":
                buzzwords.append(word)
    return buzzwords


def readBoardSize(maxSize) -> int:
    """ Reads the (squared) board size and validates that, given the number of available words, loaded from the
        buzzwords file, the max size of the boards is respected.

        Args:
            maxSize: The max size of the board. If the max size is n, then the largest board possible is  an
            n x n board
        Returns:
            An integer value n representing the desired board of size n x n."""
    while True:
        size = floor(float((input("Pick a board size from 2 to {}: ".format(maxSize)))))
        if size < 2 or size > maxSize:
            print("The board size {} is not valid.".format(size))
        else:
            return size


def printBoard(buzzWordsList, size):
    """ Helper that pretty prints a Bingo board to the console.

        Args:
            buzzWordsList: the compiled list of candidate buzz words to populate the board.
            size: the board size n aiming at building an n x n bingo board."""
    largestLength = 1
    for buzzword in buzzWordsList:
        if len(buzzword) > largestLength:
            largestLength = len(buzzword)
    offSet = 2
    formatString = "{:" + str(largestLength + offSet) + "s}"
    sepLine = "-" * ((largestLength + offSet) * size + size + 1)
    i = 0
    for buzzword in buzzWordsList:
        print("|" + formatString.format(buzzword), end="")
        i += 1
        if i == size:
            print("", end="|\n")
            print(sepLine)
            i = 0


def plotBoardGui(buzzWordsList, size):
    """Plots the bingo GUI. Nothing more than a panel full of buttons where each button corresponds to a word in the
        bingo game.

        Args:
            buzzWordsList: the compiled list of candidate buzz words to populate the board.
            size: the board size n aiming at building an n x n bingo board."""
    window = tk.Tk()
    window.title("Lingo Bingo")
    # window.geometry("350x275")
    i, j = 1, 0
    buttons = []
    for word in buzzWordsList:
        button = tk.Button(window, text=word.upper(), bg="white", activebackground="wheat2", height=8, width=16)
        button["command"] = partial(switchButtonColor, button)
        button.grid(row=i, column=j)
        buttons.append(button)
        j += 1
        if j == size:
            j = 0
            i += 1
    window.mainloop()


def switchButtonColor(button):
    if button.cget("bg") == "white":
        button.configure(bg="khaki1")
        button.configure(activebackground="lightgoldenrodyellow")
    else:
        button.configure(bg="white")
        button.configure(activebackground="wheat2")


wordsList = loadFromFile()
maxBoardSize = int(sqrt(len(wordsList)))
boardSize = readBoardSize(maxBoardSize)
boardWords = random.sample(wordsList, boardSize ** 2)
printBoard(boardWords, boardSize)
plotBoardGui(boardWords, boardSize)
