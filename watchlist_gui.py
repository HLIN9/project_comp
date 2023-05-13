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

        #TODO: Gets the watchlist type
        self.watchlist_type = tk.StringVar()
        self.watchlist_type.set('Anime/Manga')

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

        self.type = ttk.Entry(self, textvariable=self.watchlist_type)
        self.type.grid(row=0, column=1)

        # Load resource (present + added new)
        ttk.Button(self, text='Load Watchlist', command=self.load_resource).grid(row=0, column=2)
        ttk.Button(self, text='Help', command=self.get_help).grid(row=0, column=3)
    
    def load_resource(self, 
                      event=None) -> None:
        """
        This function gets the new watchlist from the Textbox and loads it to the appropriate watchlist table in the database.
        """
        # Get the new watchlist
        new_watchlist = self.watchlist_box.get('1.0', tk.END)

        # Get the watchlist type
        watchlist_type = self.watchlist_type.get()

        # Connect to the database
        import sqlite3
        conn = sqlite3.connect('watchlist.sqlite')
        c = conn.cursor()

        # Choose the appropriate table based on the watchlist type
        if watchlist_type.lower() == 'anime':
            table_name = 'anime_watchlist'
        elif watchlist_type.lower() == 'manga':
            table_name = 'manga_watchlist'
        else:
            messagebox.showerror('Invalid Watchlist Type', 'Please choose a valid watchlist type (Anime or Manga)')
            return

        # Get the existing titles in the table
        existing_titles = [row[0] for row in c.execute(f"SELECT Name FROM {table_name}")]
        
        # Add new titles to the table
        for title in new_watchlist.split('\n'):
            title = ''.join(c for c in title if c.isalnum()).lower()
            if title and title not in existing_titles:
                c.execute(f"INSERT INTO {table_name} (Name, Status) VALUES (?, 'Unread')", (title,))
        conn.commit()
        conn.close()

        # Confirm that the new titles were added to the table
        messagebox.showinfo('Watchlist Updated', 'The new titles were added to the watchlist successfully.')

    def get_help(self)->None:
        pass

root = tk.Tk()
Watchlist_GUI(parent=root)
root.mainloop()