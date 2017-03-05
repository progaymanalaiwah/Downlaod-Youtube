#!/usr/bin/env python
#[*]programer:Ayman Mahmoud Mohammed Alaiwah
#[*]Name Tool:Download_RooT_Youtube
#[*]Python 3.5

#Error
#sudo pip3 install youtube-dl

#import lib
from termcolor import colored
import pafy
import os

print("")
print(colored("[*]Your Type Download ?","green"))
print(colored("     [1] Video","blue"))
print(colored("     [2] Playlist","blue"))
print("")
type = str(input(colored("[*]Enter The Nember Type[q:exit]:","green")))

if type == "q":
    exit()

while type == "" or type.isnumeric() == False:
    type = str(input(colored("[*]Enter The Nember Type[q:exit]:", "green")))
    if type == "q":
        exit()

#Download One Video
if type == "1":
    url = str(input(colored("[*] Enter Url Video Youtube:", "green")))
    video = pafy.new(url)
    title = video.title
    best = video.getbest(preftype='mp4')
    filename = best.download(filepath="./" + title + best.extension)
    print("")
    print(colored("Successful Download Video Youtube","green"))

#Download Playlist
elif type == "2":
    url = str(input(colored("[*]Enter Url Playlist Youtube:", "green")))
    playlist = pafy.get_playlist(url)
    videos = playlist['items']
    direc = "./" + playlist['title']

    #Create File Name PlayList
    if not os.path.exists(direc):
        os.mkdir(direc)

    numberV = 0 #Value Calcu Number Video
    for v in videos:
        numberV+=1
        play = v['pafy']
        best = play.getbest(preftype='mp4')
        print(colored("[","green") + str(numberV) + colored("]","green") + colored(play.title,"yellow"))
        videopath = direc +"/"+ best.title + best.extension
        best.download(filepath=videopath)

    print("")
    print(colored("Successful Download PlayList Youtube " + colored("[","yellow") + str(numberV) + colored("]","yellow") + " Video", "green"))

else:
    print(colored("Not Number " + "[" + type + "]" ,"red"))