import tkinter as tk
from tkinter import filedialog

def tambah_jadwal():
    nama_mata_kuliah = entry_mata_kuliah.get()
    jam = entry_jam.get()
    hari = entry_hari.get()
    jadwal_listbox.insert(tk.END, f"Mata Kuliah: {nama_mata_kuliah}, Jam: {jam}, Hari: {hari}")
    entry_mata_kuliah.delete(0, tk.END)
    entry_jam.delete(0, tk.END)
    entry_hari.delete(0, tk.END)

def simpan_jadwal():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    with open(file_path, "w") as file:
        for i in range(jadwal_listbox.size()):
            file.write(jadwal_listbox.get(i) + "\n")

def buka_jadwal():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    jadwal_listbox.delete(0, tk.END)
    try:
        with open(file_path, "r") as file:
            for line in file:
                jadwal_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        jadwal_listbox.insert(tk.END, "File tidak ditemukan.")

app = tk.Tk()
app.title("Aplikasi Jadwal Kuliah")
app.geometry('550x550')
app['bg'] = 'blue'

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

label_mata_kuliah = tk.Label(frame, text="Nama Mata Kuliah:")
label_mata_kuliah.pack()

entry_mata_kuliah = tk.Entry(frame)
entry_mata_kuliah.pack()

label_jam = tk.Label(frame, text="Jam Kuliah:")
label_jam.pack()
entry_jam = tk.Entry(frame)
entry_jam.pack()

label_hari = tk.Label(frame, text="Hari Kuliah:")
label_hari.pack()
entry_hari = tk.Entry(frame)
entry_hari.pack()

tambah_button = tk.Button(frame, text="Tambah Jadwal", command=tambah_jadwal)
tambah_button.pack()

simpan_button = tk.Button(frame, text="Simpan Jadwal", command=simpan_jadwal)
simpan_button.pack()

buka_button = tk.Button(frame, text="Buka Jadwal", command=buka_jadwal)
buka_button.pack()

jadwal_listbox = tk.Listbox(frame, width=80, height=50)
jadwal_listbox.pack()

app.mainloop()
