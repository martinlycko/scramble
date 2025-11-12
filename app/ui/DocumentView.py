# Import Python standard libraries
import tkinter as tk
from tkinter import ttk

# Import project datamodel
from ..datamodel.Project import Project

def open_document_view_window(project: Project, docID: int) -> None:
    doc = project.get_document_by_id(docID)
    
    new_window = tk.Toplevel()
    new_window.title("Document: " + doc.title)
    new_window.geometry("800x400")

    # Text box
    text_box = tk.Text(new_window, wrap="word")
    text_box.pack(fill="both", expand=True)

    # Insert sample text
    text_box.insert("1.0", doc.content)