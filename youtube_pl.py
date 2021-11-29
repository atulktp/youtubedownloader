from pytube import Playlist

link = input("Past Playlist Link : ")
youtube_1 = Playlist(link)
youtubeTitle = youtube_1.title
youtube_dwt = "Now Downloading "
videoTitle = youtube_dwt+youtubeTitle
print(videoTitle)

pl = Playlist(link)

print(f'Downloading : {pl.title}')

for video in pl.videos:
	video.streams.first().download()