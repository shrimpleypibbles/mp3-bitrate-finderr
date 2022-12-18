import tkinter as tk
from tkinter import filedialog
import eyed3

def get_bitrate(filename):
    audiofile = eyed3.load(filename)
    bitrate = audiofile.info.bit_rate[1]
    return bitrate

def select_file():
    file_path = filedialog.askopenfilename()
    bitrate = get_bitrate(file_path)
    label.config(text=f"Bitrate: {bitrate} kbps")

root = tk.Tk()
root.title("MP3 Bitrate")

button = tk.Button(root, text="Select MP3 File", command=select_file)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
