from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class LimasSegiEmpat:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        Label(mainFrame, text='Panjang Alas:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)

        Label(mainFrame, text='Lebar Alas:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text='Tinggi Segiempat:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text='Tinggi Limas:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Volume:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Luas Permukaan:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtpanjang = Entry(mainFrame) 
        self.txtpanjang.grid(row=0, column=1, padx=5, pady=5)  

        self.txtlebar = Entry(mainFrame) 
        self.txtlebar.grid(row=1, column=1, padx=5, pady=5)  
        
        self.txttinggisegiempat = Entry(mainFrame) 
        self.txttinggisegiempat.grid(row=2, column=1, padx=5, pady=5)  
        
        self.txttinggilimas = Entry(mainFrame) 
        self.txttinggilimas.grid(row=3, column=1, padx=5, pady=5)  
        
        self.txtvolume = Entry(mainFrame) 
        self.txtvolume.grid(row=5, column=1, padx=5, pady=5)
        
        self.txtluaspermukaan = Entry(mainFrame) 
        self.txtluaspermukaan.grid(row=6, column=1, padx=5, pady=5) 
        
        self.btnHitungVolume = Button(mainFrame, text='Hitung Volume',
            command=self.hitung_volume)
        self.btnHitungVolume.grid(row=4, column=1, padx=5, pady=5)
 
        self.btnHitungLuasPermukaan = Button(mainFrame, text='Hitung Luas Permukaan',
            command=self.hitung_luas_permukaan)
        self.btnHitungLuasPermukaan.grid(row=4, column=2, padx=5, pady=5)        
           
    def hitung_volume(self, event=None):
        panjang = float(self.txtpanjang.get())
        lebar = float(self.txtlebar.get())
        tinggisegiempat = float(self.txttinggisegiempat.get())
        tinggilimas = float(self.txttinggilimas.get())
        V = (panjang * lebar * tinggisegiempat) / 3  # Menghitung volume limas segiempat
        self.txtvolume.delete(0, END)
        self.txtvolume.insert(END, V)
        
    def hitung_luas_permukaan(self, event=None):
        panjang = float(self.txtpanjang.get())
        lebar = float(self.txtlebar.get())
        tinggisegiempat = float(self.txttinggisegiempat.get())
        tinggilimas = float(self.txttinggilimas.get())
        lp = (panjang * lebar) + (4 * (0.5 * panjang * tinggilimas))  # Menghitung luas permukaan limas segiempat
        self.txtluaspermukaan.delete(0, END)
        self.txtluaspermukaan.insert(END, lp)
                   
            
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = LimasSegiEmpat(root, "Program Volume dan Luas Permukaan Limas Segiempat")
    root.mainloop()
