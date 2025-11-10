# Import Python standard libraries
import tkinter as tk
from tkinter import ttk

# Import project datamodel
from app.datamodel.Project import Project

# Import local ui modules
from app.ui.DocumentList import open_document_list_view

def open_document_list():
    open_document_list_view(project)

if __name__ == "__main__":    
    # Set up project
    project = Project("test", "sample")
    project.add_document("Doc1", "Content1")
    project.add_document("Doc2", "Content2")
    
    # Create the main window
    root = tk.Tk()
    root.title("Scramble")
    root.geometry("100x300")

    # Button to open document list
    open_button = tk.ttk.Button(root, text="Documents", command=open_document_list)
    open_button.pack()

    # Run the application
    root.mainloop()