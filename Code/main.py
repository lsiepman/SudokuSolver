# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:56:01 2020

@author: laura
"""

#%% IMPORTS

#%% DATA
test = {'A0': '6', 'B0': '', 'C0': '5', 'D0': '7', 'E0': '2', 'F0': '', 'G0': '',  'H0': '3', 'I0': '9', 'A1': '4', 'B1': '', 'C1': '', 'D1': '', 'E1': '', 'F1': '5', 'G1': '1', 'H1': '', 'I1': '', 'A2': '', 'B2': '2', 'C2': '', 'D2': '1', 'E2': '', 'F2': '', 'G2': '', 'H2': '', 'I2': '4', 'A3': '', 'B3': '9', 'C3': '', 'D3': '', 'E3': '3', 'F3': '', 'G3': '7',  'H3': '', 'I3': '6', 'A4': '1', 'B4': '', 'C4': '', 'D4': '8', 'E4': '', 'F4': '9', 'G4': '',  'H4': '', 'I4': '5', 'A5': '2', 'B5': '', 'C5': '4', 'D5': '', 'E5': '5', 'F5': '', 'G5': '',  'H5': '8', 'I5': '', 'A6': '8', 'B6': '', 'C6': '', 'D6': '', 'E6': '', 'F6': '3', 'G6': '', 'H6': '2', 'I6': '', 'A7': '', 'B7': '', 'C7': '2', 'D7': '9', 'E7': '', 'F7': '', 'G7': '', 'H7': '', 'I7': '1', 'A8': '3', 'B8': '5', 'C8': '', 'D8': '', 'E8': '6', 'F8': '7', 'G8': '4',  'H8': '', 'I8': '8'}

#%%
def FindRow(data, cell):
    _, row = list(cell)
    row_lst =  [key for key in data if key.endswith(row)]
    row_lst.remove(cell)
    return row_lst

def FindCol(data, cell):
    col, _ = list(cell)
    col_lst = [key for key in data if key.startswith(col)]
    col_lst.remove(cell)
    return col_lst

def FindSquare(cell):
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
        if cell in square:
            square.remove(cell)
            return square
    
    
FindSquare("A0")
