# importing packages 
from pytube import YouTube 
import os 


def yt_to_mp3(url):
	video = yt.streams.filter(only_audio=True).first()
	print("Enter the destination (leave blank for current directory)") 
	destination = 'Videos/'

	# download the file 
	out_file = video.download(output_path=destination) 

	# save the file 
	base, ext = os.path.splitext(out_file) 
	new_file = base + '.mp3'
	os.rename(out_file, new_file) 
	print("newfile: " + new_file)
	# result of success 
	print(yt.title + " has been successfully downloaded.")
	return new_file
# url input from user 
yt = YouTube( 
	str(input("Enter the URL of the video you want to download: \n>> "))) 

# extract only audio 



