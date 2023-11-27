from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class LimasSegitiga:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        Label(mainFrame, text='Alas Segitiga:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text='Tinggi Segitiga:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text='Tinggi Limas:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Volume:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Luas Permukaan:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtalas = Entry(mainFrame) 
        self.txtalas.grid(row=0, column=1, padx=5, pady=5)  

        self.txttinggisegitiga = Entry(mainFrame) 
        self.txttinggisegitiga.grid(row=1, column=1, padx=5, pady=5)  
        
        self.txttinggilimas = Entry(mainFrame) 
        self.txttinggilimas.grid(row=2, column=1, padx=5, pady=5)  
        
        self.txtvolume = Entry(mainFrame) 
        self.txtvolume.grid(row=4, column=1, padx=5, pady=5)
        
        self.txtluaspermukaan = Entry(mainFrame) 
        self.txtluaspermukaan.grid(row=5, column=1, padx=5, pady=5) 
        
        self.btnHitungVolume = Button(mainFrame, text='Hitung Volume',
            command=self.hitung_volume)
        self.btnHitungVolume.grid(row=3, column=1, padx=5, pady=5)
 
        self.btnHitungLuasPermukaan = Button(mainFrame, text='Hitung Luas Permukaan',
            command=self.hitung_luas_permukaan)
        self.btnHitungLuasPermukaan.grid(row=3, column=2, padx=5, pady=5)        
           
    def hitung_volume(self, event=None):
        alas = float(self.txtalas.get())
        tinggisegitiga = float(self.txttinggisegitiga.get())
        tinggilimas = float(self.txttinggilimas.get())
        V = (1/3) * (alas * tinggisegitiga) * tinggilimas  # Menghitung volume limas segitiga
        self.txtvolume.delete(0, END)
        self.txtvolume.insert(END, V)
        
    def hitung_luas_permukaan(self, event=None):
        alas = float(self.txtalas.get())
        tinggisegitiga = float(self.txttinggisegitiga.get())
        tinggilimas = float(self.txttinggilimas.get())
        lp = (alas * tinggisegitiga) + (3 * (0.5 * alas * tinggilimas))  # Menghitung luas permukaan limas segitiga
        self.txtluaspermukaan.delete(0, END)
        self.txtluaspermukaan.insert(END, lp)
                   
            
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = LimasSegitiga(root, "Program Volume dan Luas Permukaan Limas Segitiga")
    root.mainloop()
