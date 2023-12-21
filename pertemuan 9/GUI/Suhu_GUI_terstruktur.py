import tkinter as tk

def konversi_temperatur():
    try:
        selected_option = option_menu.get()
        suhu = float(entry.get())
        hasil = 0
        
        if selected_option == "Celsius ke Reamur":
            hasil = suhu * 4/5
        elif selected_option == "Celsius ke Fahrenheit":
            hasil = (suhu * 9/5) + 32
        elif selected_option == "Celsius ke Kelvin":
            hasil = suhu + 273
        elif selected_option == "Reamur ke Celsius":
            hasil = suhu * 5/4
        elif selected_option == "Reamur ke Fahrenheit":
            hasil = (suhu * 9/4) + 32
        elif selected_option == "Reamur ke Kelvin":
            hasil = (suhu * 5/4) + 273
        elif selected_option == "Fahrenheit ke Celsius":
            hasil = (suhu - 32) * 5/9
        elif selected_option == "Fahrenheit ke Reamur":
            hasil = (suhu - 32) * 4/9
        elif selected_option == "Fahrenheit ke Kelvin":
            hasil = ((suhu - 32) * 5/9) + 273
        elif selected_option == "Kelvin ke Celsius":
            hasil = suhu - 273
        elif selected_option == "Kelvin ke Reamur":
            hasil = (suhu - 273) * 4/5
        elif selected_option == "Kelvin ke Fahrenheit":
            hasil = ((suhu - 273) * 9/5) + 32

        result_label.config(text=f"{suhu} ° = {hasil} °")
    except ValueError:
        result_label.config(text="Coba lagi")

# Creating the main window
root = tk.Tk()
root.title("Konversi Suhu")
root.geometry('250x200')

# Creating labels
title_label = tk.Label(root, text="Konversi Suhu", font=( 16))
title_label.grid(row=0, column=0, columnspan=2)

entry_label = tk.Label(root, text="Masukkan Suhu:")
entry_label.grid(row=1, column=0)

# Creating entry field
entry = tk.Entry(root)
entry.grid(row=1, column=1)

# Creating dropdown menu
options = ["Celsius ke Reamur", "Celsius ke Fahrenheit", "Celsius ke Kelvin", "Reamur ke Celsius", "Reamur ke Fahrenheit", "Reamur ke Kelvin",
           "Fahrenheit ke Celsius", "Fahrenheit ke Reamur", "Fahrenheit ke Kelvin", "Kelvin ke Celsius", "Kelvin ke Reamur", "Kelvin ke Fahrenheit"]
option_menu = tk.StringVar(root)
option_menu.set(options[0])
option_dropdown = tk.OptionMenu(root, option_menu, *options)
option_dropdown.grid(row=2, column=0, columnspan=2)

# Creating convert button
convert_button = tk.Button(root, text="Convert", command=konversi_temperatur)
convert_button.grid(row=3, column=0, columnspan=2)

# Creating label for displaying result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2)

name_label = tk.Label(root, text="Revan Fazry Huda")
name_label.grid(row=5, column=0)

class_label = tk.Label(root, text="TI22D")
class_label.grid(row=6, column=0)

nim_label = tk.Label(root, text="220511179")
nim_label.grid(row=7, column=0)

root.mainloop()
