from pytube import YouTube


link = input("Past Video Link : ")
youtube_1 = YouTube(link)
youtubeTitle = youtube_1.title
youtube_dwt = "Now Downloading "
videoTitle = youtube_dwt+youtubeTitle
print(videoTitle)
#print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all() # All Formates
#videos = youtube_1.streams.filter(only_audio=True) # Only Audio Formates
vid = list(enumerate(videos))
for i in vid:
	print(i)
strm = int(input("Select Formate : "))
videos[strm].download()
print('Successfully Downloaded...')
