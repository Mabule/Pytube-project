from pytube import YouTube
import os
import glob
url = input("Lien vers la vidéo youtube : ")
print(f"Accès à l'url : {url} ...")
yt = YouTube(str(url))
name = yt.title
ext = str(input("Voulez vous un fichier mp3 ou mp4 ?"))
if ext != "mp3" and ext != "mp4":
    i = 1
    while ext != "mp3" and ext != "mp4":
        ext = str(input(f"Je {'re '*i}répète, tu veux un fichier mp3 ou mp4 ?"))
        i = i + 1
if ext == "mp3":
    path = 'C:/Users/drake/Music/musique'
elif ext == "mp4":
    path = 'C:/Users/drake/Videos'
print(f"{name} en cours de téléchargement ...")
yt.streams.first().download(path)
if ext == "mp3":
    for filename in glob.iglob(os.path.join(path, "*.mp4")):
        os.rename(filename, filename[:-4] + ".mp3")
print("Fichier téléchargé")