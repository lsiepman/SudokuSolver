# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 23:49:18 2020

@author: laura
"""

# IMPORTS

class FindValues:
    """Find a cell without a value and check if a value can be filled in."""

    def __init__(self, data):
        self.data = data
        self.row = None
        self.col = None
        self.square = None

    def select_cell(self):
        """For all cells, try to find a value once."""
        for i in self.data:
            if self.data[i] == "":
                self.cell = i

                self.find_col()
                self.find_row()
                self.find_square()
                self.find_possible_values()

    def find_row(self):
        """Find all corresponding cells in the row."""
        _, row = list(self.cell)
        row_lst = [key for key in self.data if key.endswith(row)]
        row_lst.remove(self.cell)
        self.row = row_lst

    def find_col(self):
        """Find all corresponding cells in the column."""
        col, _ = list(self.cell)
        col_lst = [key for key in self.data if key.startswith(col)]
        col_lst.remove(self.cell)
        self.col = col_lst

    def find_square(self):
        """Find all corresponding cells for the input."""
        sq1 = ["A0", "B0", "C0", "A1", "B1", "C1", "A2", "B2", "C2"]
        sq2 = ["D0", "E0", "F0", "D1", "E1", "F1", "D2", "E2", "F2"]
        sq3 = ["G0", "H0", "I0", "G1", "H1", "I1", "G2", "H2", "I2"]
        sq4 = ["A3", "B3", "C3", "A4", "B4", "C4", "A5", "B5", "C5"]
        sq5 = ["D3", "E3", "F3", "D4", "E4", "F4", "D5", "E5", "F5"]
        sq6 = ["G3", "H3", "I3", "G4", "H4", "I4", "G5", "H5", "I5"]
        sq7 = ["A6", "B6", "C6", "A7", "B7", "C7", "A8", "B8", "C8"]
        sq8 = ["D6", "E6", "F6", "D7", "E7", "F7", "D8", "E8", "F8"]
        sq9 = ["G6", "H6", "I6", "G7", "H7", "I7", "G8", "H8", "I8"]

        for square in [sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9]:
            if self.cell in square:
                square.remove(self.cell)
                self.square = square

    def find_possible_values(self):
        """Find all possible values for a cell.

        If one value remains, assign it to the cell.
        """
        possible_vals = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        corresponding_cells = self.col + self.row + self.square
        corresponding_cells = list(set(corresponding_cells))

        taken_vals = []
        for i in corresponding_cells:
            val = self.data[i]
            if val not in taken_vals:
                taken_vals.append(val)

        remaining_vals = [x for x in possible_vals if x not in taken_vals]

        if len(remaining_vals) == 1:
            self.data[self.cell] = remaining_vals[0]
