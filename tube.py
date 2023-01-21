from pytube import YouTube

url = input('Send link: ')
yt = YouTube(url)
print('Started downloading, wait')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
