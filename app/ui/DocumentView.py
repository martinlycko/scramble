# Import Python standard libraries
import tkinter as tk
from tkinter import ttk

# Import project datamodel
from ..datamodel.Project import Project

def open_document_view_window(project: Project, docID: int) -> None:
    def code_selection(theme: str) -> None:
        try:
            # Get selected text
            selected_text = text_box.get(tk.SEL_FIRST, tk.SEL_LAST)
            # Store it in a variable (you can also make it global or pass it somewhere)
            saved_text.set(selected_text)
            print("Selected text saved: "+selected_text)
        except tk.TclError:
            # This error occurs if no text is selected
            print("Please select some text first.") 
    
    doc = project.get_document_by_id(docID)
    
    new_window = tk.Toplevel()
    new_window.title("Document: " + doc.title)
    new_window.geometry("800x400")

    # Text box
    text_box = tk.Text(new_window, wrap="word")
    text_box.pack(fill="both", expand=True)

    # Insert sample text
    text_box.insert("1.0", doc.content)

    new_window = tk.Toplevel()
    new_window.title("Themes")
    new_window.geometry("200x400")

    frame = tk.Frame(new_window)
    frame.pack(padx=20, pady=20)

    # StringVar to store the saved text
    saved_text = tk.StringVar()

    for theme in project.themes:
        btn = tk.Button(frame,
                        text=theme,
                        width=20,
                        command=lambda thme=theme: code_selection(theme))
        btn.pack(pady=5)