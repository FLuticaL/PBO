import tkinter as tk
from tkinter import filedialog
import cv2 
import numpy as np 

def play_video():
# Create a VideoCapture object and read from input file 
	cap = cv2.VideoCapture('C:/Users/Revan/Documents/VSCode/PBO.py/pertemuan 5/Media/ado.mp4') 

	# Check if camera opened successfully 
	if (cap.isOpened()== False): 
		print("Belum berhasil") 

	# Read until video is completed 
	while(cap.isOpened()): 

	# Capture frame-by-frame 
		ret, frame = cap.read() 
		if ret == True: 
		# Display the resulting frame 
			cv2.imshow('Frame', frame) 

		# Press Q on keyboard to exit 
			if cv2.waitKey(25) & 0xFF == ord('q'): 
				break

	# Break the loop 
		else: 
			break

	# When everything done, release 
	# the video capture object 
	cap.release() 

	# Closes all the frames 
	cv2.destroyAllWindows() 

window = tk.Tk()
window.title("Pemutar Video")

# Membuat tombol untuk memilih video
play_button = tk.Button(window, text="Putar Video", command=play_video)
play_button.pack(pady=20)

# Menampilkan window
window.mainloop()