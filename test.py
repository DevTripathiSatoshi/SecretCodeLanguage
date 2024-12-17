import customtkinter as ctk

def convert_code():
    input_text = text_entry.get("1.0", ctk.END).strip()
    selected_language = language_var.get()
    
    if selected_language == "English to CPT":
        output_text = shift_text(input_text, 3)
    elif selected_language == "CPT to English":
        output_text = shift_text(input_text, -3)
    else:
        output_text = "Please select a valid conversion."

    result_label.configure(text=output_text)

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

# Configure customtkinter appearance
ctk.set_appearance_mode("System")  # Modes: "System", "Light", "Dark"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

# Create the main window
root = ctk.CTk()
root.title("Code Converter")
root.geometry("500x400")

# Create a title label
title_label = ctk.CTkLabel(root, text="Code Converter", font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=20)

# Create a text entry area
text_entry = ctk.CTkTextbox(root, height=10, width=400, corner_radius=8, fg_color="black", text_color="white")
text_entry.pack(pady=10)
text_entry.insert(ctk.END, "Enter your text here...")

# Create a dropdown list
language_var = ctk.StringVar(value="Select Language")
language_dropdown = ctk.CTkComboBox(root, variable=language_var, values=("English to CPT", "CPT to English"))
language_dropdown.pack(pady=10)

# Create a convert button
convert_button = ctk.CTkButton(root, text="Convert", command=convert_code, fg_color="gray")
convert_button.pack(pady=10)

# Create a label to display the result
result_label = ctk.CTkLabel(root, text="", wraplength=400, font=ctk.CTkFont(size=14))
result_label.pack(pady=20)

# Run the application
root.mainloop()
