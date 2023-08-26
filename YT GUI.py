from tkinter import *
from pytube import YouTube
class Win1:
    def __init__(self):
        self.rt = Tk()
        self.rt.title("YT VIDEO DOWNLOADER")
        self.rt.geometry('400x400')
        self.e = Entry(self.rt, font = ("calibri", 14), width = 40)
        self.e.pack()
        #link = "https://www.youtube.com/watch?v=16y1AkoZkmQ"
        self.s = Button(self.rt, text = 'DOWNLOAD', font = ("calibri", 14), command = self.d).pack()
        self.rt.mainloop()

    def d(self):
        self.link = self.e.get().strip()
        for i in self.rt.winfo_children():
            i.destroy()
        self.s1 = Button(self.rt, text = 'High Resolution', font = ("calibri", 14), command = self.w1).pack()
        self.s2 = Button(self.rt, text = 'Low Resolution', font = ("calibri", 14), command = self.w2).pack()

    def w2(self):
        yt = YouTube(self.link)
        stream = yt.streams.get_lowest_resolution()
        stream.download(output_path="OMG.py")
        self.l = Label(self.rt, text = "DONE", font = ('cambria', 10)).pack()
    
    def w1(self):
        yt = YouTube(self.link)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path="OMG.py")
        self.l = Label(self.rt, text = "DONE", font = ('cambria', 10)).pack()

Win1()
'''
from pytube import YouTube


link = 'https://youtu.be/nfs8NYg7yQM?feature=shared'
yt = YouTube(link)
stream = yt.streams
for i in stream:
    if "video/mp4" in str(i):
        print(str(i).split("="))'''



a = """ 


Version 1 - Vid Downloader - Text based (console)


Version 2 - Vid Downloader
             -> GUI
             -> to choose between high/low vid resolutions

Version 3 - Vid Downloader
             -> GUI
             -> to choose between VID/AUD files
             >> if vid:    options for vid resolutions
             >> if aud:    options for aud bitrates/quality
             -> Between mp4/webm format for saving



"""