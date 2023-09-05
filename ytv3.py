from pytube import YouTube
import tkinter as tk
link = "https://youtu.be/PrYfOzRYwFc?feature=shared"
obj = YouTube(link)
resolutions = obj.streams.filter(file_extension='mp4')

rt = tk.Tk()
rt.geometry("400x400")

list_streams_all = []
for i in resolutions:
    str_i = str(i)
    str_i2 = str_i.split('"')
    i_tag_num = str_i2[1]
    res_num = str_i2[5]
    list_streams_all.append((res_num, i_tag_num))
    
def stream_download(stream_tuple):
    video = resolutions.get_by_itag(stream_tuple[1])
    video.download(output_path = 'FINAL VIDEO DOWNLOADED')

for i in list_streams_all:
    quality = i[0]
    if "kbps" not in quality:
        def temp(arg = i):
            stream_download(arg)
        buttons_res = tk.Button(rt, text = quality, command = temp)
        buttons_res.pack()

rt.mainloop()











#print(resolutions)
# streams_all = ['<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="8fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">', 
#                '<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">',
#                 '<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">', 
#                 '<Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">', 
#                 '<Stream: itag="248" mime_type="video/webm" res="1080p" fps="30fps" vcodec="vp9" progressive="False" type="video">', 
#                 '<Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">',
#                 '<Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressive="False" type="video">',
#                 '<Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">',
#                 '<Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">',
#                 '<Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">', 
#                 '<Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="video">', 
#                 '<Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False" type="video">', 
#                 '<Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9" progressive="False" type="video">', 
#                 '<Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">',
#                 '<Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9" progressive="False" type="video">', 
#                 '<Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">', 
#                 '<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">', 
#                 '<Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">',
#                 '<Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">',
#                 '<Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">'] # A list of Strings
#for i in resolutions:
#    streams_all.append( str(i) )

#print(streams_all)










#option = '<Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False" type="video">'
# for i in resolutions:
#     i = str(i)
#     option_list = i.split()
#     resolution_full = option_list[3]
#     resolution = resolution_full.split('"')[1]
#     print(resolution)