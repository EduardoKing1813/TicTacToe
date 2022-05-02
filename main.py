from tkinter import *
import gameBoard


def main():
    root = Tk()
    root.title("TicTacToe")
    root.resizable(width=False, height=False)
    
    board = gameBoard.gameBoard(root)
    board.draw_board()

    root.mainloop()


if __name__ == '__main__':
	main()