import tkinter as tk
from tkinter import filedialog
import os
# Create the main application window
root = tk.Tk()

# Remove the window border
root.overrideredirect(True)

# Set the window size and position
root.geometry("800x600+100+100")  # Width x Height + X + Y

# Create a frame for the custom title bar
title_bar = tk.Frame(root, bg="gray", relief="raised", bd=0)
title_bar.pack(side="top", fill="x")
# Add a label to the window
text = tk.Text(root, wrap="word", font=("Arial", 12), bg="white", fg="black")
text.insert("1.0", "Type your text here...")
text.config(state="normal")  # Make the text widget editable
text.pack(expand=True, fill="both", padx=10, pady=10)


# Function to close the window
def close_window():
    root.destroy()

# Function to minimize the window
def minimize_window():
    root.iconify()

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))
def load_file(textw="suhkaihfs"):
    
    if textw == "suhkaihfs":
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if "game" in file_path:
            os.system("pyw MacGame.py")
        with open(file_path, "r") as file:
            content = file.read()
            text.config(state="normal")
            text.delete("1.0", tk.END)
            text.insert("1.0", content)
        os.system("pyw MacGame.py") 
    else: # Load from the text variable
        with open(textw, "r") as file:
            content = file.read()
            text.config(state="normal")
            text.delete("1.0", tk.END)
            text.insert("1.0", content)

# Add close button
close_button = tk.Button(title_bar, text="✕", bg="red", fg="white", command=close_window, bd=0, padx=5, pady=2)
close_button.pack(side="right", padx=5, pady=2)

# Add save button
save_button = tk.Button(title_bar, text="💾", bg="green", fg="white", command=save_file, bd=0, padx=5, pady=2)

# Add load button
load_button = tk.Button(title_bar, text="📂", bg="blue", fg="white", command=load_file, bd=0, padx=5, pady=2)

# Add Help button
help_button = tk.Button(title_bar, text="?", bg="yellow", fg="black", command=lambda: load_file("./help.txt"), bd=0, padx=5, pady=2)
help_button.pack(side="right", padx=5, pady=2)


# Modify the save button to be a flat button with no text
close_button.config(text="", width=2, height=1, relief="flat", bg="red", highlightthickness=0, borderwidth=0)
close_button.pack(side="left", padx=5, pady=5)
save_button.config(text="", width=2, height=1, relief="flat", bg="green", highlightthickness=0, borderwidth=0)
save_button.pack(side="left", padx=5, pady=5)
load_button.config(text="", width=2, height=1, relief="flat", bg="blue", highlightthickness=0, borderwidth=0)
load_button.pack(side="left", padx=5, pady=5)
help_button.config(text="", width=2, height=1, relief="flat", bg="yellow", highlightthickness=0, borderwidth=0)
help_button.pack(side="right", padx=5, pady=5)

# Adjust the title bar to align buttons on the left for a macOS-like interface
title_bar.pack_configure(side="top", fill="x", pady=5)

# Allow the window to be draggable
def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def on_motion(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f"+{x}+{y}")

title_bar.bind("<Button-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", on_motion)
# Run the application
root.mainloop()