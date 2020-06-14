# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:22:33 2020

@author: laura
"""

#%% IMPORTS
import tkinter as tk
from functools import partial
   
#%%
class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(fill='both', expand=True)
        
        self.frames = {}

        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(column = 0, row=0, sticky='nsew')
        
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, _controller):
        tk.Frame.__init__(self, parent)

        self.entries = list()
        columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        for row in range(9):
            for col in columns:
                entry = tk.Entry(self, width = 5)
                entry.grid(row = row, column = columns.index(col))
                rowcol = col + str(row)
                if rowcol in ["A0", "B0", "C0",     "G0", "H0", "I0", 
                              "A1", "B1", "C1",     "G1", "H1", "I1",
                              "A2", "B2", "C2",     "G2", "H2", "I2",
                                        "D3", "E3", "F3", 
                                        "D4", "E4", "F4",
                                        "D5", "E5", "F5",
                              "A6", "B6", "C6",     "G6", "H6", "I6",
                              "A7", "B7", "C7",     "G7", "H7", "I7",
                              "A8", "B8", "C8",     "G8", "H8", "I8"]:
                    entry.configure({"background": "#C0C0C0"})
                else:
                    entry.configure({"background": "white"})
                
                self.entries.append([col + str(row), entry])

        self.submit = tk.Button(self, text= 'Submit', command = self.collect_entries)
        self.submit.grid(row = 9, column = 0, columnspan = 3)
    
        self.clear = tk.Button(self, text = "Clear", command = self.clear_text)
        self.clear.grid(row = 9, column = 3, columnspan = 3)
        
        self.quit = tk.Button(self, text="Quit", fg="red", command= lambda: _controller.destroy())
        self.quit.grid(row = 9, column = 6, columnspan = 3)        
    
    def collect_entries(self):
        global output
        output = {rowcol: entry.get() for rowcol, entry in self.entries}
          
    def clear_text(self):
        for entry in self.entries:
            entry[1].delete(0, tk.END)

app = App()
app.title('Sudoku')
app.mainloop()