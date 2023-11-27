from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class Kerucut:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Radius:').grid(row=0, column=0,
        sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Tinggi:").grid(row=1, column=0,
        sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Volume:").grid(row=4, column=0,
        sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Luas Permukaan:").grid(row=5, column=0,
        sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Revan Fazry Huda").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)      
        
        Label(mainFrame, text="220511179").grid(row=7, column=0,
            sticky=W, padx=5, pady=5)             

        self.txtradius = Entry(mainFrame)
        self.txtradius.grid(row=0, column=1, padx=5, pady=5)

        self.txttinggi = Entry(mainFrame)
        self.txttinggi.grid(row=1, column=1, padx=5, pady=5)

        self.txtvolume = Entry(mainFrame)
        self.txtvolume.grid(row=4, column=1, padx=5, pady=5)

        self.txtluaspermukaan = Entry(mainFrame)
        self.txtluaspermukaan.grid(row=5, column=1, padx=5, pady=5)

        self.btnHitungVolume = Button(mainFrame, text='Hitung Volume',
        command=self.hitung_volume,bg= 'cyan')
        self.btnHitungVolume.grid(row=3, column=1, padx=5, pady=5)

        self.btnHitungLuasPermukaan = Button(mainFrame, text='Hitung Luas Permukaan',
        command=self.hitung_luas_permukaan,bg='lime')
        self.btnHitungLuasPermukaan.grid(row=3, column=2, padx=5, pady=5)

    def hitung_volume(self, event=None):
        radius = float(self.txtradius.get())
        tinggi = float(self.txttinggi.get())
        V = (1/3) * math.pi * (radius ** 2) * tinggi 
        self.txtvolume.delete(0, END)
        self.txtvolume.insert(END, V)

    def hitung_luas_permukaan(self, event=None):
        radius = float(self.txtradius.get())
        tinggi = float(self.txttinggi.get())
        s = math.sqrt(radius**2 + tinggi**2) 
        lp = math.pi * radius * (radius + s) 
        self.txtluaspermukaan.delete(0, END)
        self.txtluaspermukaan.insert(END, lp)

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = Kerucut(root, "Program Volume dan Luas Permukaan Kerucut")
    root.mainloop()
