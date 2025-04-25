import tkinter as tk

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
label = tk.Label(root, text="About this Mac:", font=("Arial", 16))
label.pack(expand=True)
text = tk.Text(root, wrap="word", font=("Arial", 12), bg="white", fg="black")
text.insert("1.0", "macOS Sequoia\n\nVersion 15.4.2 (22G91)\n\nMacBook Pro (Retina, 15-inch, Early 2025)\n\nProcessor: I.NFINITE GHz AMD Ryzen 8 IDK8700\n\nMemory: 16 GB 1600 MHz DDR3\n\nGraphics: NVIDIA GeForce RTX 5090\n\nApp Info:\n\nWindows iDock 1.0.0\n\nFlaticon Theme 1.0.0\n\nTextEdit 1.0.0\n\n")
text.config(state="disabled")  # Make the text widget read-only
text.pack(expand=True, fill="both", padx=10, pady=10)

# Function to close the window
def close_window():
    root.destroy()

# Function to minimize the window
def minimize_window():
    root.iconify()

# Add close button
close_button = tk.Button(title_bar, text="✕", bg="red", fg="white", command=close_window, bd=0, padx=5, pady=2)
close_button.pack(side="right", padx=5, pady=2)



close_button.config(text="", width=2, height=1, relief="flat", bg="red", highlightthickness=0, borderwidth=0)
close_button.pack(side="left", padx=5, pady=5)

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