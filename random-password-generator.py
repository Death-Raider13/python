import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    result_var.set(password)

# Create window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")

# Label
tk.Label(root, text="Enter Password Length:").pack(pady=5)

# Entry box
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result display
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30).pack(pady=5)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())

# Copy to clipboard button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

# Run app
root.mainloop()