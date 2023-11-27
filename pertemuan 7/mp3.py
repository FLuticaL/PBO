import tkinter as tk
from playsound import playsound

def play_audio():
    try:
        # Ganti path file audio sesuai dengan lokasi file Anda
        audio_path = "C:/Users/Revan/Documents/VSCode/PBO.py/pertemuan 5/Euy.mp3"
        playsound(audio_path, True)
    except Exception as e:
        status_label.config(text=f"Error: {e}")

# Membuat window
window = tk.Tk()
window.title("Pemutar Audio")

# Membuat tombol untuk memutar audio
play_button = tk.Button(window, text="Putar Audio", command=play_audio)
play_button.pack(pady=20)

# Label untuk status
status_label = tk.Label(window, text="")
status_label.pack()

# Menampilkan window
window.mainloop()
