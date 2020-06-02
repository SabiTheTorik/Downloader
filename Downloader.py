from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import time
import os


win = Tk()

win.title("Downloader")

win.geometry("500x310")

win.configure(bg="#000000")

win.resizable(False, False)

ytdir = StringVar()
ytlink= StringVar()

def ytpage():
    global ytlink
    global ytdir
    yttop = Toplevel(bg="black")
    yttop.resizable(False,False)
    # yttop.geometry("500x200")
    ytdirlbl = Label(yttop, text="Directory:", bg="black", fg="red", font=30)
    ytdirlbl.grid(row=1,column=0)
    ytdirent = Entry(yttop, textvariable=ytdir, font=15, width=50)
    ytdirent.grid(row=1,column=1)
    ytbrowse = Button(yttop, text="Browse", bg="red", font=20, command=ytbrowsego)
    ytbrowse.grid(row=1, column=2, padx=10)
    ytlabel = Label(yttop, text="Youtube Link:", bg="black", fg="red", font=30)
    ytlabel.grid(row=2, column=0)
    ytent = Entry(yttop, font=15, width=50, textvariable=ytlink)
    ytent.grid(row=2, column=1)
    ytlinkbtn = Button(yttop, text="Go!", bg="red", font=20, command=ytgo)
    ytlinkbtn.grid(row=2, column=2, padx=10, pady=10)
    ytwarninglbl = Label(yttop, text="Please wait until 'Go' button turns red after pressing it!", fg="red", bg="black", font=30)
    ytwarninglbl.grid(row=3, column=1)
    icon = PhotoImage(file="multimedia.png")
    yttop.tk.call("wm", "iconphoto", yttop._w, icon)


def ytgo():
    global ytlink
    global ytdir
    youtubevid = YouTube(ytlink.get())
    ytstream = youtubevid.streams[1]
    ytstream.download(ytdir.get())
    

def ytbrowsego():
    global ytdir
    selectytdir = filedialog.askdirectory()
    ytdir.set(selectytdir)
    
    
instadirectory = StringVar()
instatoken = StringVar()

def askdir():
    global instadirectory
    selecteddir = filedialog.askdirectory()
    instadirectory.set(selecteddir)

def instapage():
    global instatoken
    global instadirectory
    instatop = Toplevel()
    instatop.resizable(False,False)
    instatop.configure(bg="black")
    instalabel = Label(instatop, text="Instagram Post Token:", bg="black", fg="#FA19C6", font=30)
    instalabel.grid(row=2, column=0)
    instaentry = Entry(instatop, font=15, width=50, textvariable=instatoken)
    instaentry.grid(row=2, column=1)
    instabuton = Button(instatop, text="Go!", bg="#FA19C6", font=20,command=instago)
    instabuton.grid(row=2,column=2, padx=10, pady=5)
    instabutonhelp = Button(instatop, text="Help", bg="#FA19C6", font=10, command=instahelp)
    instabutonhelp.grid(row=2,column=3)
    instadirectorylbl = Label(instatop, text="Directory: ", bg="black", fg="#FA19C6", font=30)
    instadirectorylbl.grid(row=1,column=0)
    instaentry = Entry(instatop, font=15, width=50, textvariable=instadirectory)
    instaentry.grid(row=1, column=1)
    instabrowsebuton = Button(instatop, text="Browse", bg="#FA19C6", font=20, command=askdir)
    instabrowsebuton.grid(row=1, column=2, padx=10)
    icon = PhotoImage(file="multimedia.png")
    instatop.tk.call("wm", "iconphoto", instatop._w, icon)    

def instago():
    global instatoken
    global instadirectory
    os.system("pip install instalooter")
    # os.system('mkdir "Downloaded Instagram Posts"')
    # os.system("cd Downloaded Instagram Posts")
    os.system(f"instalooter post {instatoken.get()} {instadirectory.get()}")

def instahelp():
    instahelptop = Toplevel(bg="black")
    instahelptop.resizable(False,False)
    instahelplabel = Label(instahelptop, text="Where is the Token?", bg="black", fg="#FA19C6", font=30)
    instahelplabel.grid(row=1, column=0)
    instatokenimg = ImageTk.PhotoImage(Image.open("Instatoken.png"))
    instatokenlblimg = Label(instahelptop, image=instatokenimg, bg="#000000")
    instatokenlblimg.image = instatokenimg
    instatokenlblimg.grid()
    


    
    
icon = PhotoImage(file="multimedia.png")

win.tk.call("wm", "iconphoto", win._w, icon)

img = ImageTk.PhotoImage(Image.open("arrows.png").resize((120,120)))
lbl2 = Label(win,image=img, bg="#000000")
lbl2.place(x=398)

img1 = ImageTk.PhotoImage(Image.open("arrows.png").resize((120,120)))
lbl3 = Label(win,image=img, bg="#000000")
lbl3.place(x=0)


lbl1 = Label(win,text="Downloader", fg="#04F3FC", bg="black", font=("Helvetica",40, "bold"), justify="center")
lbl1.place(x=100, y=20)

ytbtn = Button(win, text="Youtube", bg="red", font=("Helvetica", 32), command=ytpage)
ytbtn.grid(row=2, column=0)
ytbtn.place(x=20 ,y=150)

insabtn = Button(win, text="Instagram", bg="#FA19C6", font=("Helvetica", 32), command=instapage)
insabtn.grid(row=2, column=1)
insabtn.place(x=255,y=150)

line = Label(win, text="______________________________________________", font=("Helvetica"), bg="black", fg="#04F3FC")
line.place(x=0, y=230)

flwmebtn = Label(win, text="Follow Me:", fg="#04F3FC", font=("Helvetica", 16), bg="black")
flwmebtn.place(x=5, y=265)


def myinsta():
    webbrowser.open("https://www.instagram.com/sabi_yomtov/")

def myfb():
    webbrowser.open("https://www.facebook.com/sabi.yomtov.9")

def mygit():
    webbrowser.open("https://github.com/SabiTheTorik")

def myyt():
    webbrowser.open("https://www.youtube.com/channel/UCoKoFJzyUZ26Hp28LVfsRlA?view_as=subscriber")

def mytwt():
    webbrowser.open("https://twitter.com/Sabi82419751")

def myst():
    webbrowser.open("https://steamcommunity.com/profiles/76561198890803904")

insimg = ImageTk.PhotoImage(Image.open("instagram.png").resize((40,40)))
instaimgbtn = Button(win, image=insimg, bg="black", border="0", command=myinsta)
instaimgbtn.place(x=120, y=260)

fbimg = ImageTk.PhotoImage(Image.open("facebook.png").resize((40,40)))
fbimgbtn = Button(win, image=fbimg, bg="black", border="0", command=myfb)
fbimgbtn.place(x=180, y=260)

gitimg = ImageTk.PhotoImage(Image.open("github.png").resize((40,40)))
gitimgbtn = Button(win, image=gitimg, bg="black", border="0", command=mygit)
gitimgbtn.place(x=240, y=260)

ytimg = ImageTk.PhotoImage(Image.open("youtube.png").resize((40,40)))
ytimgbtn = Button(win, image=ytimg, bg="black", border="0", command=myyt)
ytimgbtn.place(x=300, y=260)

twtimg = ImageTk.PhotoImage(Image.open("twitter.png").resize((40,40)))
twtimgbtn = Button(win, image=twtimg, bg="black", border="0", command=mytwt)
twtimgbtn.place(x=360, y=260)

stimg = ImageTk.PhotoImage(Image.open("steam.png").resize((40,40)))
stimgbtn = Button(win, image=stimg, bg="black", border="0", command=myst)
stimgbtn.place(x=420, y=260)













win.mainloop()
