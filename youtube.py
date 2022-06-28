import os
from pytube import YouTube

#os clear screen
os.system("cls")

atulktp='''
          _             _   _      _           
         | |           | | | |    | |          
   __ _  | |_   _   _  | | | | __ | |_   _ __  
  / _` | | __| | | | | | | | |/ / | __| | '_ \ 
 | (_| | | |_  | |_| | | | |   <  | |_  | |_) |
  \__,_|  \__|  \__,_| |_| |_|\_\  \__| | .__/ 
                                        | |    
                                        |_|    


 \u001b[31m Instagram \u001b[37m - \u001b[32m https://instagram.com/atulktp \u001b[37m
 \u001b[31m Github    \u001b[37m - \u001b[32m https://github.com/atulktp    \u001b[37m
'''
print(atulktp)

def on_complete(stream, filepath):
    print('download complete')
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100-bytes_remaining*100/stream.filesize)}%'
    print(progress_string)

link = input('\u001b[31m Youtube Link:- \u001b[37m ')
video_obj = YouTube(link, on_complete_callback = on_complete, on_progress_callback=on_progress)

print(f'\u001b[31m title: \u001b[37m    {video_obj.title}')
print(f'\u001b[31m length: \u001b[37m   {round(video_obj.length/60, 2)} Minutes')
print(f'\u001b[31m videws: \u001b[37m   {video_obj.views/100000} Lakh')
print(f'\u001b[31m author: \u001b[37m   {video_obj.author}')

# download
print('\u001b[31m download: \u001b[37m \u001b[32m (b)est \u001b[37m | \u001b[31m (w)orst \u001b[37m | \u001b[34m (a)udio \u001b[37m |  (e)xit')
download_choice = input('\u001b[31m download choice: \u001b[37m')

if download_choice=='b':
    video_obj.streams.get_highest_resolution().download()
elif download_choice=='w':
    video_obj.streams.get_lowest_resolution().download()
elif download_choice=='a':
    video_obj.streams.get_audio_only().download()
elif download_choice=='e':
    exit
else:
    print('Please!, choose from given options.')