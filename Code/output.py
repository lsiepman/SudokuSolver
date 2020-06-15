# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:55:47 2020

@author: laura
"""

import pandas as pd
import tkinter as tk

import matplotlib.pyplot as plt

test = {'A0': '6','B0': '','C0': '5','D0': '7','E0': '2','F0': '','G0': '',  'H0': '3', 'I0': '9', 'A1': '4', 'B1': '', 'C1': '', 'D1': '', 'E1': '', 'F1': '5', 'G1': '1', 'H1': '', 'I1': '', 'A2': '', 'B2': '2', 'C2': '', 'D2': '1', 'E2': '', 'F2': '', 'G2': '', 'H2': '', 'I2': '4', 'A3': '', 'B3': '9', 'C3': '', 'D3': '', 'E3': '3', 'F3': '', 'G3': '7',  'H3': '', 'I3': '6', 'A4': '1', 'B4': '', 'C4': '', 'D4': '8', 'E4': '', 'F4': '9', 'G4': '',  'H4': '', 'I4': '5', 'A5': '2', 'B5': '', 'C5': '4', 'D5': '', 'E5': '5', 'F5': '', 'G5': '',  'H5': '8', 'I5': '', 'A6': '8', 'B6': '', 'C6': '', 'D6': '', 'E6': '', 'F6': '3', 'G6': '', 'H6': '2', 'I6': '', 'A7': '', 'B7': '', 'C7': '2', 'D7': '9', 'E7': '', 'F7': '', 'G7': '', 'H7': '', 'I7': '1', 'A8': '3', 'B8': '5', 'C8': '', 'D8': '', 'E8': '6', 'F8': '7', 'G8': '4',  'H8': '', 'I8': '8'}


class ShowResult:
    """Show the solved sudoku."""

    def __init__(self, data):
        """Show result of the Sudoku Solver."""
        self.sudoku = data
        self.colour_table()

    def convert_to_table(self):
        """Convert solved sudoku dict into a pandas dataframe."""
        grid = []
        for row in range(9):
            grid.append([self.sudoku[i] for i in self.sudoku
                         if i.endswith(str(row))])

        self.numbers = grid

    def colour_table(self):
        """Create a table to colour the table."""
        grid = []
        for row in range(9):
            if row < 3 or row > 5:
                grid.append(["#C0C0C0", "#C0C0C0", "#C0C0C0",
                             "white", "white", "white",
                             "#C0C0C0", "#C0C0C0", "#C0C0C0"])
            else:
                grid.append(["white", "white", "white",
                             "#C0C0C0", "#C0C0C0", "#C0C0C0",
                             "white", "white", "white"])

        self.colours = grid

    def plot_table(self):
        """Create a matplotlib plot of the table."""
        fig, ax = plt.subplots()
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=self.numbers, loc='center',
                             cellColours=self.colours)

        plt.show()


t = ShowResult(test)
t.convert_to_table()
t.plot_table()
