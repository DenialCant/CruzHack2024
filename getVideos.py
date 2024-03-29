# importing packages 
from pytube import YouTube 
import os

def yt_to_mp3(url_text):
	try:
		URL =  YouTube(url_text)
	except Exception:
		print("hello")
		return 0, 0
	else:
		video = URL.streams.filter(only_audio=True).first()

		destination = 'Videos/'

		# download the file 
		out_file = video.download(output_path=destination) 

		# save the file 
		base, ext = os.path.splitext(out_file) 
		new_file = base + '.mp3'
		
		try:
			os.rename(out_file, new_file)
		except FileExistsError:
			try:
				os.remove(base + ext)
			finally:
				print("ERROR. MP3 not found")
			print("File alreadly exists. Pulling that file...")
		finally:
			# result of success 
			print(URL.title + " has been successfully downloaded.")
			return new_file, URL.title



