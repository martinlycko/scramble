# Import Python standard libraries
import tkinter as tk
from tkinter import ttk

# Import project datamodel
from ..datamodel.Project import Project


def open_add_document_view(project: Project) -> None:
    def save_and_close():
        nonlocal title_text, body_text
        title_text = title_entry.get()
        body_text = text_box.get("1.0", tk.END).strip()
        project.add_document(title_text, body_text)
        new_window.destroy()

    new_window = tk.Toplevel()
    new_window.title("Documents")
    new_window.geometry("600x400")

    # Title label + entry
    tk.Label(new_window, text="Title:").pack(pady=(10, 0))
    title_entry = tk.Entry(new_window, width=50)
    title_entry.pack(pady=5)

    # Text label + text box
    tk.Label(new_window, text="Text:").pack(pady=(10, 0))
    text_box = tk.Text(new_window, width=60, height=10)
    text_box.pack(pady=5)

    # Save & Close button
    tk.Button(new_window, text="Save & Close", command=save_and_close).pack(pady=10)

     # Variables to store results
    title_text = ""
    body_text = ""