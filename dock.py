import tkinter as tk
import os
import psutil
# Create the main application window
root = tk.Tk()

# Remove the window border
root.overrideredirect(True)
root.attributes("-topmost", True)
# Set the window size and position
root.geometry(f"1200x100+{(1920 - 1500) // 2}+{1080 // 2 + 200}")  # Centered on Y and bottom on X
root.configure(bg="black")  # Set the background color to black
# Load the image
image = tk.PhotoImage(file="app.png")
image2 = tk.PhotoImage(file="app2.png")
image3 = tk.PhotoImage(file="app3.png")

# Create a label to display the image
def finder_opened():
    
    if os.name == "nt":
        os.startfile("C:\\Windows\\explorer.exe")
    elif "macos" or "osx" in os.name:
        os.system("open /System/Applications/Finder.app")

    # Function to display active apps as options

def open_settings():
    os.system("pyw settings.pyw")

def open_textedit():
    os.system("pyw textedit.pyw")

image_label = tk.Label(root, image=image, borderwidth=0)
image_label.bind("<Button-1>", lambda event: finder_opened())
image_label2 = tk.Label(root, image=image2, borderwidth=0)
image_label2.bind("<Button-1>", lambda event: open_settings())
image_label3 = tk.Label(root, image=image3, borderwidth=0)
image_label3.bind("<Button-1>", lambda event: open_textedit())

# Place the image on the left
image_label.pack(side="left")
image_label2.pack(side="right")
image_label3.pack(side="left")

root.mainloop()