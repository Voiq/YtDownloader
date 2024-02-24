from tkinter.messagebox import showinfo
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

YELLOW = "#f7f5dd"

#-----FUNCTIONS-----# 
def download():
    try:
        yt = YouTube(url_entry.get())
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_vid = streams.get_highest_resolution()
        highest_res_vid.download(output_path=path_entry.get())
        showinfo("Video Downloaded Successfully!", "Video Downloaded Successfully!")
    except Exception as error:
        print(error)


def select_path():
    save_path = filedialog.askdirectory()
    if save_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, save_path)
        showinfo("Folder Selected", f"Selected Folder: {save_path}")
    return save_path    

#------GUI------#
app = tk.Tk()
app.title("YouTube Video Downloader")
app.config(padx=50 ,pady=50,bg=YELLOW)


label = tk.Label(text="Enter the YouTube video URL: ",bg=YELLOW)
label.grid(row=1,column=1)


url_entry= tk.Entry()
url_entry.grid(row=2,column=1)


download_button = tk.Button(text="Download",command=download)
download_button.grid(row=3,column=2)


path_entry=tk.Entry()
path_button = tk.Button(text="Select Path",command=select_path)
path_button.grid(row=3,column=0)

#------End of GUI-----#


app.mainloop()
