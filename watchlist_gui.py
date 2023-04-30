import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.ttk as ttk
from web_scraping import get_rating

class Watchlist_GUI(ttk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid()

        #TODO: Gets the new watchlist
        self.watchlist = tk.StringVar()
        self.watchlist.set('Watchlist')

        #TODO: Make the needed widgets
        self.make_widgets()

    def make_widgets(self)->None:
        # Input field for new watchlist
        ttk.Label(self, text='New Watchlist:').grid(row=0, column=0)
        self.watchlist_box = tk.Text(self, width=40, height=10)
        self.watchlist_box.grid(row=1, column=0,columnspan=3)

        # Load resource (present + added new)
        ttk.Button(self, text='Load', command=self.load_resource).grid(row=0, column=3)
    
    def load_resource(self):
        #TODO: Load the resource
        pass

root = tk.Tk()
Watchlist_GUI(parent=root)
root.mainloop()