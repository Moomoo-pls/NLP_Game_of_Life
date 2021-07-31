class Cell:
    def __init__(self):
        '''
        By default a cell starts off as dead
        '''
        self.status = 'Dead'

    def set_dead(self):
        '''
        Setter to set cell's status as dead.
        '''
        self.status = 'Dead'

    def set_alive(self):
        '''
        Setter to set cell's status as alive.
        '''
        self.status = 'Alive'

    def is_alive(self):
        '''
        Method to check if the cell is alive.
        Returns true for alive, false for dead.
        '''
        if self.status == 'Alive':
            return True
        return False

    def print_status_character(self):
        '''
        Method to display an X if the cell is alive, 
        otherwise fill the display with -
        '''
        if self.is_alive():
            return 'X'
        return '-'
