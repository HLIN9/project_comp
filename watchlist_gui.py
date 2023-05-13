import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinter.ttk as ttk
from web_scraping import get_rating
import sqlite3
import re

def clean_string(title):
    title = ''.join(c for c in title if c.isalnum() or c.isspace())
    title = title.title()
    title = title.strip()
    return title

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

        # Connect to database
        self.conn = sqlite3.connect('watchlist.sqlite')
        self.cur = self.conn.cursor()

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

    def load_resource(self, event=None) -> None:
        # Get the watchlist content from the text box
        watchlist_content = self.watchlist_box.get('1.0', 'end-1c')

        # Get the watchlist type from the entry bar
        watchlist_type = self.watchlist_type.get().lower()

        # Define the table name based on the watchlist type
        if watchlist_type == 'anime':
            table_name = 'anime_watchlist'
        elif watchlist_type == 'manga':
            table_name = 'manga_watchlist'
        else:
            messagebox.showerror('Error', 'Invalid watchlist type')
            return
        
        #Adding the new titles
        try:
            # Split the watchlist content into lines and clean up each line
            titles = [clean_string(line) for line in watchlist_content.split('\n')]
            # Remove any duplicates in the new list
            titles = list(set(titles))

            # Connect to the database and get the existing titles
            conn = sqlite3.connect('watchlist.sqlite')
            self.cur = conn.cursor()
            self.cur.execute(f"SELECT Name FROM {table_name}")
            existing_titles = [clean_string(row[0]) for row in self.cur.fetchall()]

            # Insert new titles into the database
            new_titles = [title for title in titles if title not in existing_titles]
            for title in new_titles:
                self.cur.execute(f"INSERT INTO {table_name} (Name, Status) VALUES (?, ?)", (title, 'Unread'))
        except:
            messagebox.showerror('Error', 'Error inserting titles into watchlist')
            return

        # Create a new window to display the contents of the table
        display_window = tk.Toplevel(self)
        display_window.title(f"{watchlist_type} Watchlist")
        display_window.geometry("800x600")

        # Connect to the database and extract the table contents
        rows = self.cur.execute(f"SELECT * FROM {table_name} ORDER BY Name ASC").fetchall()
        column_names = [description[0] for description in self.cur.description]

        # Create the treeview widget
        tree = ttk.Treeview(display_window, columns=column_names, show="headings")
        tree.pack(side="left", fill="both", expand=True)

        # Configure the scrollbars
        vsb = ttk.Scrollbar(display_window, orient="vertical", command=tree.yview)
        vsb.pack(side="right", fill="y")
        hsb = ttk.Scrollbar(display_window, orient="horizontal", command=tree.xview)
        hsb.pack(side="bottom", fill="x")
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Add the data to the treeview widget
        for row in rows:
            tree.insert("", "end", values=row)

        # Set the column headings
        for i, column_name in enumerate(column_names):
            tree.heading(i, text=column_name)       
        
        # Commit the changes and close the database connection
        conn.commit()
        conn.close()

        # Show a message box with the number of new titles added
        num_new_titles = len(new_titles)
        if num_new_titles > 0:
            messagebox.showinfo('Success', f'{num_new_titles} new titles added to {table_name}')
        else:
            messagebox.showinfo('Success', f'No new titles added to {table_name}')


    def get_help(self)->None:
        pass

root = tk.Tk()
Watchlist_GUI(parent=root)
root.mainloop()