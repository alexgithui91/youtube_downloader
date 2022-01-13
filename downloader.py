from pytube import YouTube

DOWNLOAD_FOLDER = "C:\\Users\\Agithui\\Downloads"

video_url = input("Please enter video url : ")

video_obj = YouTube(video_url)

stream = video_obj.streams.get_highest_resolution()

print("Downloading file...")

stream.download(DOWNLOAD_FOLDER)

print("Done...")
