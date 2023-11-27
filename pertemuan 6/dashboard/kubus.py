from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W


class Kubus:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Sisi:').grid(row=0, column=0,
        sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Volume:").grid(row=2, column=0,
        sticky=W, padx=5, pady=5)

        Label(mainFrame, text="Luas Permukaan:").grid(row=3, column=0,
        sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Revan Fazry Huda").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)      
        
        Label(mainFrame, text="220511179").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)             

        self.txtsisi = Entry(mainFrame)
        self.txtsisi.grid(row=0, column=1, padx=5, pady=5)

        self.txtvolume = Entry(mainFrame)
        self.txtvolume.grid(row=2, column=1, padx=5, pady=5)

        self.txtluaspermukaan = Entry(mainFrame)
        self.txtluaspermukaan.grid(row=3, column=1, padx=5, pady=5)

        self.btnHitungVolume = Button(mainFrame, text='Hitung Volume',
         command=self.hitung_volume,bg='pink')
        self.btnHitungVolume.grid(row=1, column=1, padx=5, pady=5)

        self.btnHitungLuasPermukaan = Button(mainFrame, text='Hitung luas permukaan',
        command=self.hitung_luas_permukaan,bg = 'red')
        self.btnHitungLuasPermukaan.grid(row=1, column=2, padx=5, pady=5)

    def hitung_volume(self, event=None):
        sisi = float(self.txtsisi.get())
        V = sisi ** 3 
        self.txtvolume.delete(0, END)
        self.txtvolume.insert(END, V)

    def hitung_luas_permukaan(self, event=None):
        sisi = float(self.txtsisi.get())
        lp = 6 * (sisi ** 2) 
        self.txtluaspermukaan.delete(0, END)
        self.txtluaspermukaan.insert(END, lp)

    def onKeluar(self, event=None):
        self.parent.destroy()


if __name__ == '__main__':
    root = Tk()
    aplikasi = Kubus(root, "Program Volume dan Luas Permukaan Kubus")
    root.mainloop()
