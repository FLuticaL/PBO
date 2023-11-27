from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from math import pi

class Bola:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Jari-jari:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Volume:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Luas Permukaan:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)   
        
        Label(mainFrame, text="Revan Fazry Huda").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)      
        
        Label(mainFrame, text="220511179").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)                  

        # pasang textbox
        self.txtJarijari = Entry(mainFrame) 
        self.txtJarijari.grid(row=0, column=1, padx=5, pady=5)  
        
        self.txtvolume = Entry(mainFrame) 
        self.txtvolume.grid(row=3, column=1, padx=5, pady=5)
        
        self.txtluaspermukaan = Entry(mainFrame) 
        self.txtluaspermukaan.grid(row=4, column=1, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung Volume',
            command=self.hitung_volume,bg = 'green')
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
 
        self.btnHitung = Button(mainFrame, text='Hitung luas permukaan',
            command=self.hitung_luaspermukaan,bg = 'yellow')
        self.btnHitung.grid(row=2, column=2, padx=5, pady=5)        
           
        
    def hitung_volume(self, event=None):
        jarijari = float(self.txtJarijari.get())
        V = round((4/3) * pi * jarijari**3 ,2)
        self.txtvolume.delete(0,END)
        self.txtvolume.insert(END,V)   
 
    def hitung_luaspermukaan(self, event=None):
        jarijari = float(self.txtJarijari.get())
        lp = round(4*pi*jarijari*jarijari,2)
        self.txtluaspermukaan.delete(0,END)
        self.txtluaspermukaan.insert(END,lp)                
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = Bola(root, "Program Volume dan luas permukaan bola")
    root.mainloop() 