from PIL import Image
from pytesseract import pytesseract

# Path ke file tesseract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path ke gambar
path_to_image = 'C:/Users/Revan/Documents/VSCode/PBO.py/pertemuan 5/images/gambar3.jpg'

# Set path untuk tesseract_cmd ke tesseract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Buka gambar dengan PIL
img = Image.open(path_to_image)

# Ekstrak teks dari gambar (dalam bahasa Indonesia)
text = pytesseract.image_to_string(img, lang='id')

# Tampilkan teks hasil ekstraksi
print(text)

# Simpan teks ke dalam file teks
with open("hasil_ekstraksi.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Teks hasil ekstraksi disimpan dalam 'hasil_ekstraksi.txt'")
