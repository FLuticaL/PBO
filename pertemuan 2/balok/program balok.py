import tkinter as tk
from tkinter import Frame, Label, Entry, Button,END, W
from math import pi


def hitung_volume():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())
    t = float(txttinggi.get())
    
    V = p * l * t
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,V)
    
def hitung_luaspermukaan():
    p = float(txtpanjang.get())
    l = float(txtlebar.get())
    t = float(txttinggi.get())
    
    lp = 2*((p*l) + (p*t) + (l*t))
    
    txtluaspermukaan.delete(0,END)
    txtluaspermukaan.insert(END,lp)

def hitung():
    hitung_volume()
    hitung_luaspermukaan()
    
app = tk.Tk()
app.title("Program Menghitung volume dan luas permukaan")

Frame = Frame(app)
Frame.pack(padx=30, pady=30)

name = Label(Frame, text='Balok: ')
name.grid(row=0, column=0, sticky=W, padx=5, pady=5)

panjang = Label(Frame, text='Panjang: ')
panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)

lebar = Label(Frame, text='Lebar: ')
lebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)

Tinggi = Label(Frame, text='Tinggi: ')
Tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

volume = Label(Frame, text='Volume: ')
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

lp = Label(Frame, text='Luas Permukaan: ')
lp.grid(row=7, column=0, sticky=W, padx=5, pady=5)

hitung_button = Button(Frame, text="Hitung Volume", command = hitung_volume, bg = 'blue')
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

hitunglp_button = Button(Frame, text="Hitung Luas permukaan", command = hitung_luaspermukaan, bg = 'red')
hitunglp_button.grid(row=5, column=1, sticky=W, padx=5, pady=5)

txtpanjang = Entry(Frame)
txtpanjang.grid(row=1, column=1)

txtlebar = Entry(Frame)
txtlebar.grid(row=2, column=1)

txttinggi = Entry(Frame)
txttinggi.grid(row=3, column=1)

txtvolume = Entry(Frame)
txtvolume.grid(row=6, column=1)

txtluaspermukaan = Entry(Frame)
txtluaspermukaan.grid(row=7, column=1)

nama = Label(Frame, text=' ')
nama.grid(row=8, column=0, sticky=W, padx=5, pady=5)

nama = Label(Frame, text='Revan Fazry Huda ')
nama.grid(row=9, column=0, sticky=W, padx=5, pady=5)

NIM = Label(Frame, text='220511179')
NIM.grid(row=10, column=0, sticky=W, padx=5, pady=5)

app.mainloop()

