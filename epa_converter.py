# Standard library
import os

# Third party
from tkinter import *
from tkinter import ttk
import pandas as pd


def clean_data():
    path = os.path.abspath(os.path.join('Katologübersicht.csv'))
    data = pd.read_csv(path, delimiter=",")

    new_data = data[['Katalog', 'CODE', 'Klarname']].copy()
    return new_data

def main(*args, **kwargs):
    
    # Main App
    app = Tk()
    app.title("EPA String Generator")
    app.geometry("320x200")
            
    # Create new Frame
    frame = ttk.Frame(app, padding=10)
    frame.grid()
    
    # Menübar
    menubar = Menu(app)
    app.config(menu=menubar)
        
    # Filemenu
    file_menu = Menu(menubar, tearoff=0)
    
    file_menu.add_command(
        label="Datei öffnen",
    )
    
    file_menu.add_separator()
    
    file_menu.add_command(
        label="Quit",
        command=app.destroy
    )
    
    # Menu einrichten
    menubar.add_cascade(label="Datei", menu=file_menu)

    ttk.Label(frame, text="Create String").grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=app.destroy).grid(column=0, row=1)
    
    return app

if __name__ == "__main__":
    
    root = main()
    root.mainloop()
    