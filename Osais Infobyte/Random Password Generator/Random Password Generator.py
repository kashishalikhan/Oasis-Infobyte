import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    if not character_set:
        raise ValueError("At least one character type must be selected")

    return ''.join(random.choice(character_set) for _ in range(length))

def on_generate():
    try:
        length = int(length_entry.get())
        password = generate_password(length, letters_var.get(), numbers_var.get(), symbols_var.get())
        result_var.set(password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def on_copy():
    pyperclip.copy(result_var.get())
    messagebox.showinfo("Info", "Password copied to clipboard")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Label(root, text="Password Length:").pack(anchor="w", padx=20)
length_entry = tk.Entry(root)
length_entry.pack(padx=20)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor="w", padx=20)

tk.Button(root, text="Generate", command=on_generate).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, state='readonly').pack(padx=20, pady=5)

tk.Button(root, text="Copy to Clipboard", command=on_copy).pack(pady=10)

root.mainloop()
