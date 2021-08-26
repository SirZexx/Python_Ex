# 1. Write a program to Download you-tube Video on specific location by pasting it's URL as input

import pytube

# to paste video url just copy it and then right click on terminal it will automatically paste it
url = input("Enter URL of Video Here :")

youtube= pytube.YouTube(url) #this will load user given url into function

video = youtube.streams.get_highest_resolution() #this will select highest resolution of given video

video.download("F:\Work\Python Lessons\Exercise\Module Exercise\YT\yt_downloads") #save_path

