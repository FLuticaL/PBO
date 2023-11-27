import tkinter as tk
from tkinter import Menu
from segi import *
from tiga import *
from ling import *
from bola import *
from balok import *
from kerucut import *
from kubus import*
from tabung import *
from limassegitiga import *
from limassegiempat import *
from prismasegitiga import *
from translator import *


# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)
program_menu = Menu(menubar)
Translator_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='App Persegi', command= lambda: new_window("Luas Persegi", FrmPersegi)
)
app_menu.add_command(
    label='App Segitiga', command= lambda: new_window("Luas Segitiga", FrmSegitiga)
)
app_menu.add_command(
    label='App Lingkaran', command= lambda: new_window("Luas Lingkaran", FrmLingkaran)
)

program_menu.add_command(
    label='Program Bola', command = lambda: new_window("Volume dan luas Permukaan Bola", Bola)
)

program_menu.add_command(
    label='Program Balok', command = lambda: new_window("Volume dan luas Permukaan Balok", Balok)
)

program_menu.add_command(
    label='Program Kerucut', command = lambda: new_window("Volume dan luas Permukaan Kerucut", Kerucut)
)

program_menu.add_command(
    label='Program Kubus', command = lambda: new_window("Volume dan luas Permukaan Kubus", Kubus)
)

program_menu.add_command(
    label='Program Tabung', command = lambda: new_window("Volume dan luas Permukaan Tabung", Tabung)
)

program_menu.add_command(
    label='Program Limas Segitiga', command = lambda: new_window("Volume dan luas Permukaan Limas Segitiga", LimasSegitiga)
)

program_menu.add_command(
    label='Program Limas Segiempat', command = lambda: new_window("Volume dan luas Permukaan Limas Segiempat", LimasSegiEmpat)
)

program_menu.add_command(
    label='Program Prisma Segitiga', command = lambda: new_window("Volume dan luas Permukaan Prisma Segitiga", PrismaSegitiga)
)
Translator_menu.add_command(
    label='Translate', command = lambda: new_window("Translator!", FrmTranslator)
)

def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)
menubar.add_cascade(
    label="Program", menu=program_menu
)
menubar.add_cascade(
    label="Translator", menu=Translator_menu
)
    
root.mainloop()