from enum import Enum

class Direction(Enum):
   RIGHT = 1
   LEFT = 2

class Cell():
    def __init__(self, symbol, left_cell = None, right_cell = None):
        self.symbol = symbol
        self.right_cell = right_cell
        self.left_cell = left_cell

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_left_cell(self):
        return self.left_cell

    def set_left_cell(self, cell):
        self.left_cell = cell

    def get_right_cell(self):
        return self.right_cell

    def set_right_cell(self, cell):
        self.right_cell = cell


class Tape():
    def __init__(self, tape_input, blank_symbol):
        self.blank_symbol = blank_symbol

        self.head = Cell(blank_symbol)
        self.first_cell = self.head
        self.last_cell = self.head
        
        for i in tape_input:
            self.set_head_symbol(i,Direction.RIGHT)

        self.head = self.first_cell

    def get_head_symbol(self):
        return self.head.get_symbol()

    def set_head_symbol(self, symbol, direction):
        self.head.set_symbol(symbol)

        if direction == Direction.LEFT:
            if self.head.get_left_cell():
                self.head = self.head.get_left_cell()
            else:
                left_cell = Cell(self.blank_symbol, left_cell = None, right_cell = self.head)
                self.head.set_left_cell(left_cell)
                self.head = left_cell
                self.first_cell = self.head
            

        elif direction == Direction.RIGHT:
            if self.head.get_right_cell():
                self.head = self.head.get_right_cell()
            else:
                right_cell = Cell(self.blank_symbol, left_cell = self.head, right_cell = None)
                self.head.set_right_cell(right_cell)
                self.head = right_cell
                self.last_cell = self.head
        else:
            pass
        # ToDo: Error
    
    def print_configuration(self, state):
        cell = self.first_cell

        while cell != None:
            if cell == self.head:
                print("(", state, ")", sep="", end="")
            print(cell.get_symbol(), end="")
            cell = cell.get_right_cell()
            
        print()

    
