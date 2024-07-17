import tkinter
import customtkinter
from pytube import YouTube

def Download():
    # in this function, I get the link from label and download it, just audio. If is an error, this function say "Download Error"
    try:
        ytlink = url_link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        audio = ytObject.streams.get_audio_only()
        audio.download()
        finishLabel.configure(text = "Download complete!")
    except:
        finishLabel.configure(text = "Download Error!", text_color = 'red')


def on_progress(stream, bytes_remainings):
    # here I make the progress bar and progress text, functional
    size_file = stream.filesize
    bytes_downloads = size_file - bytes_remainings
    percentage = bytes_downloads / size_file * 100
    per = str(int(percentage))
    progressText.configure(text = per + '%')
    progressText.update()

    progressBar.set(float(percentage) / 100)


customtkinter.set_default_color_theme('blue')

# setting the app
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Downloader")

title = customtkinter.CTkLabel(app, text ='Youtube Download', font =('Impact', 30))
title.pack(padx = 10, pady = 10)

# url lable
url_link = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 400, height = 10, font =('Impact', 15), textvariable = url_link)
link.pack()

# progress bar/text
progressText = customtkinter.CTkLabel(app, text='0%')
progressText.pack()

progressBar = customtkinter.CTkProgressBar(app, width = 400)
progressBar.set(0)
progressBar.pack(padx = 10, pady = 5)

# finish massage or error message
finishLabel = customtkinter.CTkLabel(app, text = '')
finishLabel.pack()

# button for download
download = customtkinter.CTkButton(app, text='Download', command = Download)
download.pack(padx = 10, pady = 10)

# app loop
app.mainloop()