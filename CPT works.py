import tkinter as tk
from tkinter import ttk

def convert_code():
    input_text = text_entry.get("1.0", tk.END).strip()
    selected_language = language_var.get()
    
    if selected_language == "English to CPT":
        output_text = shift_text(input_text, 3)
    elif selected_language == "CPT to English":
        output_text = shift_text(input_text, -3)
    else:
        output_text = "Please select a valid conversion."

    result_label.config(text=output_text)

def shift_text(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

# Create the main window
root = tk.Tk()
root.title("Code Converter")
root.geometry("400x300")
root.configure(bg='black')

# Create a text entry area
text_entry = tk.Text(root, height=10, width=40, bg='black', fg='white', insertbackground='white')
text_entry.pack(pady=10)

# Create a dropdown list
language_var = tk.StringVar(value="Select Language")
language_dropdown = ttk.Combobox(root, textvariable=language_var, state='readonly')
language_dropdown['values'] = ('English to CPT', 'CPT to English')
language_dropdown.pack(pady=5)

# Create a convert button
convert_button = tk.Button(root, text="Convert", command=convert_code, bg='grey', fg='white')
convert_button.pack(pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="", bg='black', fg='white')
result_label.pack(pady=10)

# Run the application
root.mainloop()
