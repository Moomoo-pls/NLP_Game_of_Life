from Game_of_Life.board import Board
import os
import time

def main():
    # Get the size of the board from the terminal
    board_size = os.get_terminal_size()
    rows = board_size.lines
    columns = board_size.columns

    # create a board:
    game_of_life_board = Board(rows,columns)
    game_of_life_board.draw_board()

    # The game will run unless it reaches a point where there are no longer cells to process
    while game_of_life_board.isAllDead() != True :
        game_of_life_board.update_board()
        game_of_life_board.draw_board()
        time.sleep(1)

    # In the incredibly unlikely case that there are no longer cells
    user_action = ''
    while user_action != 'q' :
        user_action = input('Everyone died! Press q + enter at any point to exit the program.')


main()