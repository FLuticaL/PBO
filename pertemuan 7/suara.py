from gtts import gTTS 
from playsound import playsound
import tkinter as tk

def convert_text_to_speech():
    mytext = text_entry.get()
    language = 'ja'  # Set language code for Indonesian
    myobj = gTTS(text=mytext, lang=language, slow=False) 

    output_file = "selamat.mp3"
    myobj.save(output_file)
    playsound(output_file, True)

# Membuat window
window = tk.Tk()
window.title("Text to Speech")

# Label untuk input teks
label = tk.Label(window, text="Masukkan teks:")
label.pack()

# Entry untuk memasukkan teks
text_entry = tk.Entry(window)
text_entry.pack()

# Tombol untuk mengonversi teks menjadi suara
convert_button = tk.Button(window, text="Convert", command=convert_text_to_speech)
convert_button.pack()

# Menampilkan window
window.mainloop()
