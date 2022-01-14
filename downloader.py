from pytube import YouTube
from pytube.cli import on_progress

DOWNLOAD_FOLDER = "C:\\Users\\Agithui\\Downloads"

video_url = input("Please enter video url : ")

video_obj = YouTube(video_url, on_progress_callback=on_progress)

stream = video_obj.streams.get_highest_resolution()

print("Downloading file...")

stream.download(DOWNLOAD_FOLDER)
