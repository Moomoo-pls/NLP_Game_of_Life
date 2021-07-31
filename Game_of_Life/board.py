from Game_of_Life.cell import Cell
from random import randint

class Board:
    def __init__(self, rows, columns):
        # The rows and columns will be initialized by the size of the console
        self.rows = rows
        self.columns = columns
        self.allDead = False

        # initialize a cell object in every row
        self.grid = [[Cell() for column_cells in range(self.columns)] for row_cells in range(self.rows)]
        

        self.generate_board()

    def isAllDead(self):
        '''
        Check to see if all the cells died
        Only returns true if they all died.
        '''
        for row in self.grid:
            for column in row:
                if column.is_alive() == True:
                    return False
        return True

    def generate_board(self):
        '''
        Goes through each row and randomly sets a cell alive
        '''
        for row in self.grid:
            for column in row:
                #there is a 20% chance the cells spawn alive.
                chance_number = randint(0,4)
                if chance_number == 1:
                    column.set_alive()
    
    def draw_board(self):
        '''
        Draw the current state of the board in the terminal
        '''
        for row in self.grid:
            for column in row:
                print (column.print_status_character(),end='')
            print () # to create a new line pr. row.

    def update_board(self):
        '''
        Updates the state of the board based on
        the check of each cell. The cells react according
        to the state they were in on the board, not dynamically.

        Ex. If a cell flips, it's neighbours still process it in
        it's unflipped state.
        '''

        #cells list for living cells to kill and cells to resurrect or keep alive
        goes_alive = []
        gets_killed = []

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                # Check neighbour square:
                check_neighbour = self.find_neighbour(row , column)
                
                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    # Check live status for neighbour_cell:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self.grid[row][column]
                status_main_cell = cell_object.is_alive()

                #If the cell is alive, check the neighbour status.
                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

        # Set cell statuses
        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()
    
    def find_neighbour(self,check_row,check_column):
        '''
        method that checks all the neighbours for all the cells
        and returns the list of the valid neighbours so the update 
        method can set the new status
        '''

        # To only search neighbouring cells, we search through -1 to 1.
        search_min = -1
        search_max = 2

        neighbour_list = []

        # Neighbors are only invalid if they are outside the boards bounds
        # This logic basically filters them out.
        for row in range(search_min,search_max):
            for column in range(search_min,search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column 
                
                valid_neighbour = True

                if (neighbour_row) == check_row and (neighbour_column) == check_column:
                    valid_neighbour = False

                if (neighbour_row) < 0 or (neighbour_row) >= self.rows:
                    valid_neighbour = False

                if (neighbour_column) < 0 or (neighbour_column) >= self.columns:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(self.grid[neighbour_row][neighbour_column])
        return neighbour_list