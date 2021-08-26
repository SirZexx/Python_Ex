import shutil
import os

#for this program to work you will have to put this python file in startup folder of your computer which is located at 
#C:\Users\(your user name)\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\

# path will be the path of folder which you would like to delete on startup
path= ("E:\hello")
shutil.rmtree(path) #this will delete folder
os.mkdir(path) #this will recreate folder which is deleted (so you will get empty folder)
