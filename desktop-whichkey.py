# Usage: python menu-json.py mode_name
import os
import sys
import tkinter as tk
import json

# Change the working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
jsonfile = "keybindings.json"

from tkinter import font

# Create a temporary window to get font metrics
FONT = ("Monospace", 10)
root_temp = tk.Tk()
font_obj = font.Font(family=FONT[0], size=FONT[1])
LINE_HEIGHT = font_obj.metrics("linespace")  # Exact line height
root_temp.destroy()

# Bar configuration
BACKGROUND_COLOR = "#2E3440"
TEXT_COLOR = "#D8DEE9"
MODE_COLOR = "#81A1C1"  # Color for the mode (bold)

# Read the JSON file
def load_configuration(mode):
    with open(jsonfile, "r") as f:
        data = json.load(f)
    if mode in data:
        return data[mode]
    else:
        print(f"Mode '{mode}' not found in the JSON file.")
        sys.exit(1)

# Get the mode from the command line arguments
if len(sys.argv) < 2:
    print("Please provide a mode (e.g., 'applications' or 'rofi').")
    sys.exit(1)

selected_mode = sys.argv[1]
configuration = load_configuration(selected_mode)

# Extract mode and bindings from the loaded configuration
mode = configuration["mode"]
keybindings = configuration["bindings"]

# Sort keybindings alphabetically by the associated key
keybindings = dict(sorted(keybindings.items()))

# Text to be displayed in the bar
text = "   ".join([f"{app}" for key, app in keybindings.items()])
text = mode + " " + text

# Calculate the number of lines required based on the wraplength
def calculate_number_of_lines(text, wraplength):
    # Create a temporary Label to simulate the text over multiple lines
    temp_label = tk.Label(root, text=text, font=FONT, wraplength=wraplength)
    temp_label.pack()  # Temporarily add it to the window
    root.update_idletasks()  # Update the window to get the correct height
    num_lines = temp_label.winfo_height() // LINE_HEIGHT  # Calculate the number of lines
    # print(f"temp_label.winfo_height(): {temp_label.winfo_height()}")
    temp_label.destroy()  # Remove the temporary Label
    return num_lines

# Create the window
root = tk.Tk()
root.overrideredirect(True)  # Remove borders and decorations

# Adjust the text over multiple lines according to the screen width
wraplength = root.winfo_screenwidth() - 20  # Set the maximum text width (with a 20px margin)
number_of_lines = max(1, calculate_number_of_lines(text, wraplength))
# print(f"wraplength: {wraplength}")
# print(f"number of lines: {number_of_lines}")

# Adjust the window height proportionally to the number of lines
root.geometry(f"{root.winfo_screenwidth()}x{LINE_HEIGHT * number_of_lines}+0+0")  # Top of the screen
# print(f"winfo screenwidth: {root.winfo_screenwidth()}")
 
root.configure(bg=BACKGROUND_COLOR)

# Create a frame to hold the text and center it vertically
frame = tk.Frame(root, bg=BACKGROUND_COLOR)
frame.pack(fill="both", expand=True)

# Create a text widget for the formatted mode
text_widget = tk.Text(
    frame,
    bg=BACKGROUND_COLOR,
    fg=TEXT_COLOR,
    font=FONT,
    wrap="word",  # Automatically adjust text to wrap at word boundaries
    height=number_of_lines,  # Number of required lines
    padx=10,  # Horizontal padding
    pady=0,  # Vertical padding
    bd=0,  # Remove the border
    highlightthickness=0  # Remove the highlighted outline
)

# Insert the mode with a different color and bold font
text_widget.insert("1.0", mode)  # Insert the mode
text_widget.tag_add("mode", "1.0", "1.end")
text_widget.tag_configure("mode", foreground=MODE_COLOR, font=("Monospace", 10, "bold"))

# Insert the rest of the text (on the same line)
text_widget.insert("end", " " + text[len(mode):])  # Insert text after the mode

# Configure the appearance of the text and add it to the window
text_widget.configure(state="disabled")  # Make the text non-editable
text_widget.pack(expand=True, fill="both")

# Display the window
root.mainloop()

