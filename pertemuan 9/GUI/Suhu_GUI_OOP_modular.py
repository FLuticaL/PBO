import tkinter as tk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry('250x250')

        self.title_label = tk.Label(root, text="Konversi Suhu", font=(16))
        self.title_label.grid(row=0, column=0, columnspan=2)

        self.entry_label = tk.Label(root, text="Masukkan Suhu:")
        self.entry_label.grid(row=1, column=0)

        self.entry = tk.Entry(root)
        self.entry.grid(row=1, column=1)

        options = ["Celsius ke Reamur", "Celsius ke Fahrenheit", "Celsius ke Kelvin", "Reamur ke Celsius", "Reamur ke Fahrenheit",
                   "Reamur ke Kelvin", "Fahrenheit ke Celsius", "Fahrenheit ke Reamur", "Fahrenheit ke Kelvin",
                   "Kelvin ke Celsius", "Kelvin ke Reamur", "Kelvin ke Fahrenheit"]

        self.option_menu = tk.StringVar(root)
        self.option_menu.set(options[0])
        self.option_dropdown = tk.OptionMenu(root, self.option_menu, *options)
        self.option_dropdown.grid(row=2, column=0, columnspan=2)

        self.convert_button = tk.Button(root, text="Convert", command=self.konversi_temperatur)
        self.convert_button.grid(row=3, column=0, columnspan=2)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.grid(row=4, column=0, columnspan=2)

        self.name_label = tk.Label(root, text="Revan Fazry Huda")
        self.name_label.grid(row=5, column=0)

        self.class_label = tk.Label(root, text="TI22D")
        self.class_label.grid(row=6, column=0)

        self.nim_label = tk.Label(root, text="220511179")
        self.nim_label.grid(row=7, column=0)

    def konversi_temperatur(self):
        try:
            selected_option = self.option_menu.get()
            suhu = float(self.entry.get())
            hasil = 0

            if selected_option == "Celsius ke Reamur":
                hasil = suhu * 4 / 5
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


            self.result_label.config(text=f"{suhu}° = {hasil}°")
        except ValueError:
            self.result_label.config(text="Coba lagi")


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()
