# Import Python standard libraries
import tkinter as tk
from tkinter import ttk

# Import project datamodel
from ..datamodel.Project import Project

# Import other ui modules
from .DocumentAdd import open_add_document_view
from .DocumentView import open_document_view_window

def open_document_view(project: Project, id: int) -> None:
    open_document_view_window(project, id)

def open_add_document(project: Project) -> None:
    open_add_document_view(project)

def open_document_list_view(project: Project) -> None:
    new_window = tk.Toplevel()
    new_window.title("Documents")
    new_window.geometry("200x400")

    frame = tk.Frame(new_window)
    frame.pack(padx=20, pady=20)

    add_btn = tk.Button(frame,
                        text="Add Document",
                        width=20,
                        command=lambda: open_add_document(project))
    add_btn.pack(pady=5)

    for document in project.documents:
        btn = tk.Button(frame,
                        text=document.title,
                        width=20,
                        command=lambda i=document.id: open_document_view(project, i))
        btn.pack(pady=5)