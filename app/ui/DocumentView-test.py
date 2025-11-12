import tkinter as tk
from tkinter import messagebox

def save_selection():
    try:
        # Get selected text
        selected_text = text_box.get(tk.SEL_FIRST, tk.SEL_LAST)
        # Store it in a variable (you can also make it global or pass it somewhere)
        saved_text.set(selected_text)
        messagebox.showinfo("Saved", f"Selected text saved:\n\n{selected_text}")
    except tk.TclError:
        # This error occurs if no text is selected
        messagebox.showwarning("No Selection", "Please select some text first.")

# Create main window
root = tk.Tk()
root.title("Select and Save Text")

# StringVar to store the saved text
saved_text = tk.StringVar()

# Text box
text_box = tk.Text(root, wrap="word", width=40, height=10)
text_box.pack(padx=10, pady=10)

# Insert sample text
text_box.insert("1.0", "Try selecting some of this text, then click 'Save Selection'.")

# Button to save selection
save_button = tk.Button(root, text="Save Selection", command=save_selection)
save_button.pack(pady=5)

# Label to show saved text (optional)
tk.Label(root, textvariable=saved_text, fg="blue").pack(pady=5)

root.mainloop()