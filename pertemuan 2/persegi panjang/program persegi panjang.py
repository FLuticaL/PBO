import tkinter as tk
import math
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())
    
    L = pj * lb
    
    txtLuas.delete(0,END)
    txtLuas.insert(END,L)
    
def hitung_keliling():
    pj = float(txtpanjang.get())
    lb = float(txtlebar.get())
    
    K = 2 * (pj + lb)

    txtkeliling.delete(0,END)
    txtkeliling.insert(END,K)
    
def hitung():
    hitung_luas()
    hitung_keliling()

app = tk.Tk()
app.title("Program menghitung luas persegi panjang")

Frame = Frame(app)
Frame.pack(padx=30, pady=30)

panjang = Label(Frame, text='panjang: ')
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=10)

lebar = Label(Frame, text='lebar: ')
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=10)

txtpanjang = Entry(Frame)
txtpanjang.grid(row=0, column=1)

txtlebar = Entry(Frame)
txtlebar.grid(row=1, column=1)

hitung_button = Button(Frame, text="Hitung", command=hitung, bg = 'black', fg='white')
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

Luas = Label(Frame, text='Luas: ')
Luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

keliling = Label(Frame, text='keliling: ')
keliling.grid(row=4, column=0, sticky=W, padx=5, pady=10)

txtLuas = Entry(Frame)
txtLuas.grid(row=3, column=1)

txtkeliling = Entry(Frame)
txtkeliling.grid(row=4, column=1)

nama = Label(Frame, text=' ')
nama.grid(row=5, column=0, sticky=W, padx=5, pady=5)

nama = Label(Frame, text='Revan Fazry Huda ')
nama.grid(row=6, column=0, sticky=W, padx=5, pady=5)

NIM = Label(Frame, text='220511179')
NIM.grid(row=7, column=0, sticky=W, padx=5, pady=5)

program = Label(Frame, text='menghitung Luas dan')
program.grid(row=8, column=0, sticky=W, padx=5, pady=5)

program1 = Label(Frame, text='keliling Persegi Panjang')
program1.grid(row=8, column=1, sticky=W, padx=5, pady=5)

app.mainloop()

