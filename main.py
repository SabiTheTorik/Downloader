from tkinter import *
from PIL import Image,ImageTk
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


win = Tk()

win.title("Downloader")

win.geometry("220x100")

win.configure(bg="#000000")

win.resizable(False, False)

ytlink= StringVar()

def ytpage():
    global ytlink
    yttop = Toplevel(bg="black")
    yttop.resizable(False,False)
    # yttop.geometry("500x200")
    ytlabel = Label(yttop, text="Youtube Link:", bg="black", fg="red", font=30)
    ytlabel.grid(row=1, column=0)
    ytent = Entry(yttop, font=15, width=50, textvariable=ytlink)
    ytent.grid(row=1, column=1)
    ytlinkbtn = Button(yttop, text="Go!", bg="red", font=20, command=ytgo)
    ytlinkbtn.grid(row=1, column=2, padx=10)
    
def ytgo():
    global ytlink
    youtubevid = YouTube(ytlink.get())
    ytstream = youtubevid.streams.first()
    ytstream.download("./Downloaded Youtube Videos")
    
instadirectory = StringVar()
instatoken = StringVar()

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
    instabutonhelp.grid(row=1,column=2)
    instadirectorylbl = Label(instatop, text="Directory: ", bg="black", fg="#FA19C6", font=30)
    instadirectorylbl.grid(row=1,column=0)
    instaentry = Entry(instatop, font=15, width=50, textvariable=instadirectory)
    instaentry.grid(row=1, column=1)

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
    


# fblink = StringVar()

# def fbpage():
#     global fblink
#     fbtop = Toplevel(bg="black")
#     fblbl = Label(fbtop, text="Facebook Video Link: ", bg="black", fg="#0A0AF7", font=30)
#     fblbl.grid(row=1, column=0)
#     fbentry = Entry(fbtop, font=15, width=50, textvariable=fblink)
#     fbentry.grid(row=1, column=1)
#     fbvidgo = Button(fbtop, text="Go!", font=30, bg="#0A0AF7", command=fbgo)
#     fbvidgo.grid(row=1,column=2, padx=10)

# def fbgo():
#     global fblink
#     options = webdriver.ChromeOptions()

#     options.add_argument("--headless")

#     driver = webdriver.Chrome(options=options)

#     driver.get("https://getfbstuff.com/")

#     fbinput = driver.find_element_by_xpath("/html/body/section/div/div/div/div[1]/div/form/div/div/input")

#     fbinput.send_keys(str(fblink.get()))

#     fbdown1 = driver.find_element_by_xpath("/html/body/section/div/div/div/div[1]/div/form/div/div/center/button")

#     fbdown1.click()

#     time.sleep(5)

#     fbdown2 = driver.find_element_by_xpath("/html/body/section/div/div/div/div/div/div[1]/div/div/div[2]/div[1]/center/a")

#     fbdown2.click()

#     time.sleep(5)

#     fbvid = driver.find_element_by_xpath("/html/body/video")

#     fbvid.send_keys(Keys.CONTROL + "s")

#     fbvid.send_keys(Keys.ENTER)



    


    
    
icon = PhotoImage(file="multimedia.png")

win.tk.call("wm", "iconphoto", win._w, icon)

img = ImageTk.PhotoImage(Image.open("arrows.png").resize((50,50)))
lbl2 = Label(win,image=img, bg="#000000")
lbl2.place(x=100)


lbl1 = Label(win,text="Downloader", fg="#04F3FC", bg="black", font=80, justify="center")
lbl1.grid(row=1, column=0)

ytbtn = Button(win, text="Youtube", bg="red", font=15, command=ytpage)
ytbtn.grid(row=2, column=0)
ytbtn.place(y=60)

insabtn = Button(win, text="Instagram", bg="#FA19C6", font=15, command=instapage)
insabtn.grid(row=2, column=1)
insabtn.place(x=110,y=60)

# fbbtn = Button(win, text="Facebook", bg="#0A0AF7", font=15, command=fbpage)
# fbbtn.grid(row=2, column=3, padx=10)
# fbbtn.place(x=240,y=60)










win.mainloop()
