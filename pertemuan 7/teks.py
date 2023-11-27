from PIL import Image
from pytesseract import pytesseract
import tkinter as tk
from tkinter import filedialog

# Define path to Tesseract executable
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from image
def extract_text():
    path_to_image = filedialog.askopenfilename()
    if path_to_image:
        # Point pytesseract to the Tesseract executable
        pytesseract.tesseract_cmd = path_to_tesseract

        # Open image with PIL
        img = Image.open(path_to_image)

        # Extract text from image
        text = pytesseract.image_to_string(img)

        # Display extracted text
        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, text)

# Create GUI window
window = tk.Tk()
window.title("Image to Text")

# Button to select image
select_button = tk.Button(window, text="Select Image", command=extract_text)
select_button.pack()

# Text area to display extracted text
text_display = tk.Text(window, height=10, width=50)
text_display.pack()

window.mainloop()
