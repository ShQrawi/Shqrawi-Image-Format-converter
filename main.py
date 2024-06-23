import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image # type: ignore
import os


def convert_file():
    file_path = filedialog.askopenfilename()

    if file_path:
        try:
            output_format = format_var.get()

            image = Image.open(file_path)

            file_name, _ = os.path.splitext(file_path)
            output_file_path = f"{file_name}.{output_format}"

            image.save(output_file_path)

            messagebox.showinfo("Convert Completed", "File converted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("No File Selected", "Please select a file.")


window = tk.Tk()
window.geometry("400x600")
window.resizable(False, False)
window.title("Shqrawi's Image Format Converter")

format_label = tk.Label(window, text="Output Format:")
format_label.pack()

format_var = tk.StringVar(window)
format_dropdown = tk.OptionMenu(window, format_var, "png", "jpeg", "gif", "ico")
format_dropdown.pack()

convert_button = tk.Button(window, text="Convert", command=convert_file)
convert_button.pack()

window.mainloop()