from gtts import gTTS 
from playsound import playsound

mytext = 'Selamat Belajar ya!'
language = 'ja'
myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("C:/Users/Revan/Documents/VSCode/PBO.py/pertemuan 5/selamat.mp3") 
playsound("C:/Users/Revan/Documents/VSCode/PBO.py/pertemuan 5/selamat.mp3", True)