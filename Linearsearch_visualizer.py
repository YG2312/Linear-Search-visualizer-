import tkinter as tk
from tkinter import messagebox
import time

# Function for linear search visualization
def linear_search_visualization(arr, target):
    n = len(arr)
    
    for i in range(n):
        # Highlight the current element being checked
        highlight_element(i, "yellow")
        root.update()
        time.sleep(0.2)  # Add a delay for visualization
        
        if arr[i] == target:
            highlight_element(i, "green")  # Highlight if found
            messagebox.showinfo("Result", f"Element found at index {i}")
            return
        else:
            highlight_element(i, "red")  # Mark as incorrect
    
    messagebox.showinfo("Result", "Element not found")  # If target not found

# Highlight the current element (box) in the GUI
def highlight_element(index, color):
    canvas.itemconfig(rects[index], fill=color)
    canvas.itemconfig(labels[index], fill="white" if color == "green" else "black")

# Function to start the search
def start_search():
    try:
        arr = list(map(int, entry_array.get().split(',')))
        target = int(entry_target.get())
        draw_array(arr)  # Draw the array on canvas
        root.update()
        
        linear_search_visualization(arr, target)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers.")

# Function to draw array as blocks on the canvas
def draw_array(arr):
    global rects, labels
    canvas.delete("all")  # Clear previous drawings
    rects = []
    labels = []
    
    for i, num in enumerate(arr):
        x1, y1 = 50 + i * 60, 100
        x2, y2 = x1 + 50, y1 + 50
        rect = canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray")
        label = canvas.create_text(x1 + 25, y1 + 25, text=str(num), font=('Arial', 16))
        
        rects.append(rect)
        labels.append(label)

# Setting up the Tkinter GUI
root = tk.Tk()
root.title("Linear Search Visualization")

# Array input label and entry
label_array = tk.Label(root, text="Enter Array (comma-separated integers):")
label_array.pack(pady=5)
entry_array = tk.Entry(root, width=50)
entry_array.pack(pady=5)

# Target input label and entry
label_target = tk.Label(root, text="Enter Target Value:")
label_target.pack(pady=5)
entry_target = tk.Entry(root, width=20)
entry_target.pack(pady=5)

# Canvas for visualizing the search
canvas = tk.Canvas(root, width=600, height=200)
canvas.pack(pady=20)

# Search button
btn_search = tk.Button(root, text="Start Search", command=start_search)
btn_search.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
