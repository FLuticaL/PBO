import tkinter as tk
from tkinter import Entry,Button,END,filedialog,Text,LEFT,RIGHT,X
def openfile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/Revan/Documents/VSCode",
        title = "Open Text File",
        filetypes=(("Text Files", "*.txt"),)
    )
    pathh.insert(END, tf)
    tf = open(tf)
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

def savefile():
    teks = pathh.get()
    with open(pathh.get(),"w") as file1:
        file1.write(txtarea.get(1.0, "end-1c"))
        
    txtarea.delete("1.0", "end")
    file1.close()
    
app = tk.Tk()
app.title("Aplikasi Buka FIle")
app['bg'] = 'pink'
txtarea = Text (app, width=40, height=20)
txtarea.pack(padx = 30, pady= 30)
pathh = Entry(app)
pathh.pack(side= LEFT, expand=True, fill=X, padx=30, pady = 30)
Button(
    app,
    text="Open File",
    command= openfile
).pack(side= LEFT, expand=True, fill=X, padx=20)
Button(
    app,
    text="Save File",
    command= savefile
).pack(side= LEFT, expand=True, fill=X, padx=20)
app.mainloop()