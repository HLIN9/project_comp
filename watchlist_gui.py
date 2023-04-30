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
        self.watchlist.set('Type in new watchlist')

        #TODO: Make the needed widgets
        self.make_widgets()

    def make_widgets(self)->None:
        # Input field for new watchlist
        ttk.Label(self, text='New Watchlist:').grid(row=0, column=0)
        self.watchlist_box = tk.Text(self, width=40, height=10)
        self.watchlist_box.grid(row=1, column=0,columnspan=3)
        self.watchlist_box.insert('1.0', self.watchlist.get())
        self.watchlist_box.bind('<Control-Return>', 
                                self.load_resource)

        # Load resource (present + added new)
        ttk.Button(self, text='Load Watchlist', command=self.load_resource).grid(row=0, column=1)
        ttk.Button(self, text='Help', command=self.get_help).grid(row=0, column=2)
    
    def load_resource(self, 
                      event=None)->None:
        #TODO: # Set the value of self.watchlist to the contents of the Text widget
        self.watchlist.set(self.watchlist_box.get('1.0', 'end-1c'))
        messagebox.showinfo('Resource', self.watchlist.get())
    
    def get_help(self)->None:
        #TODO: Show the help messagebox
        messagebox.showinfo('Help', 'This is a test')

root = tk.Tk()
Watchlist_GUI(parent=root)
root.mainloop()