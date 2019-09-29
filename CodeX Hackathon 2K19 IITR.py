try:
    from Tkinter import *
    import tkFileDialog as filedialog
except ImportError:
    from tkinter import *
    from tkinter import filedialog
import os
import PIL.Image
try:
    from Tkinter import *
    import tkFileDialog as filedialog
except ImportError:
    from tkinter import *
    from tkinter import filedialog
import PIL.Image
import PIL.ImageTk
import PIL.ImageTk
import threading
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter import filedialog
from tkinter import *
import math
from tkinter import ttk
from ttkthemes import themed_tk as tk
import tkinter.messagebox
from mutagen.mp3 import MP3
from pygame import mixer
import time
import webbrowser
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import Tk
from tkinter.ttk import Frame, Label
import sys
global img


class App(Frame):
    def chg_image(self):
        if self.im.mode == "1":  # bitmap image
            self.img = PIL.ImageTk.BitmapImage(self.im, foreground="black")
        else:  # photo image
            self.img = PIL.ImageTk.PhotoImage(self.im)
        self.la.config(image=self.img, bg="#000000",
                       width=self.img.width(), height=self.img.height())

    def open(self):
        filename = filedialog.askopenfilename()
        if filename != "":
            self.im = PIL.Image.open(filename)
        self.chg_image()
        self.num_page = 0
        self.num_page_tv.set(str(self.num_page + 1))

    def seek_prev(self):
        self.num_page = self.num_page - 1
        if self.num_page < 0:
            self.num_page = 0
        self.im.seek(self.num_page)
        self.chg_image()
        self.num_page_tv.set(str(self.num_page + 1))

    def seek_next(self):
        self.num_page = self.num_page + 1
        try:
            self.im.seek(self.num_page)
        except:
            self.num_page = self.num_page - 1
        self.chg_image()
        self.num_page_tv.set(str(self.num_page + 1))

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('PHOTOS')

        self.num_page = 0
        self.num_page_tv = StringVar()

        fram = Frame(self)
        Button(fram, text="OPEN FILE", command=self.open).pack(side=LEFT)
        Button(fram, text="PREV", command=self.seek_prev).pack(side=LEFT)
        Button(fram, text="NEXT", command=self.seek_next).pack(side=LEFT)
        Label(fram, textvariable=self.num_page_tv).pack(side=LEFT)
        fram.pack(side=TOP, fill=BOTH)

        self.la = Label(self)
        self.la.pack()

        self.pack()
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
def homescreen():
    global posx,posy,wall
    posy = 200
    posx = 200
    wall = Tk()

    def createbutton():
        global posx,posy,wall
        foldd = PhotoImage(file=r"folder.png")
        Neww= Button(wall, image=foldd,width=30,command=musicp)
        if posy >= 650:
            posy = 150
            posx = posx + 250
        Neww.place(relx=0, rely=0, x=posx, y=posy)
        posy += 150
        ii+=1


    def us():
        window = Tk()
        window.geometry("300x150")
        window.title("ABOUT US")

        details = Label(window, text="DEVELOPERS:\n\nARPIT PANDEY\nROHAN MALLICK\nKETAN SUHAAS\n\nCODEX, IIT ROORKEE")
        details.pack()


    def searchwall():
        i = search.get()
        webbrowser.open(i)




    class wallpaper(Frame):

        def __init__(self):
            super().__init__()
            self.loadImage()
            self.initUI()

        def loadImage(self):
            try:
                self.img = Image.open("wall.jpg")

            except IOError:
                print("Unable to load image")
                sys.exit(1)

        def initUI(self):

            self.master.title("Codex OS")
            tatras = ImageTk.PhotoImage(self.img)
            label = Label(self, image=tatras)
            label.image = tatras
            label.pack()
            self.pack()

        def setGeometry(self):
            w, h = self.img.size
            self.master.geometry(("1550x867+-7+-2"))




    wall.title("CodeX OS")
    wall.geometry("1366x900")
    wall.overrideredirect(True)
    app = FullScreenApp(wall)
    menu = Menu(wall)
    wall.config(menu=menu)

    filemenu = Menu(menu, bg="black")
    menu.add_cascade(label='File', menu=filemenu, background="black")
    filemenu.add_command(label='Create New Folder', foreground="white", command=createbutton)
    filemenu.add_command(label='Open', foreground="white")
    filemenu.add_separator()
    filemenu.add_command(label='Exit', foreground="white", command=wall.destroy)
    helpmenu = Menu(menu, bg="black")
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About', command=us, foreground="white")

    wallpap = wallpaper()
    wallpap.setGeometry()
    photo = PhotoImage(file=r"002-camera.png")
    video = PhotoImage(file=r"webb.png")
    music2 = PhotoImage(file=r"music.png")
    sett = PhotoImage(file=r"settings.jpg")
    mapp= PhotoImage(file=r"maps.png")
    shutd=PhotoImage(file=r"shutd.png")
    logd = PhotoImage(file=r"logd.png")
    cal=PhotoImage(file=r"calc.png")
    shut=Button(wall, text="SHUTDOWN", image=shutd, width=30,command=wall.destroy)
    shut.place(relx=1, rely=1,x=-120,y=-50, width=100,anchor=SW)
    def logo():
        wall.destroy()
        applock()
    log = Button(wall, text="SHUTDOWN", image=logd, width=30, command=logo)
    log.place(relx=1, rely=1, x=-120, y=-200, width=100, anchor=SW)
    photos = Button(wall, text="PHOTOS", image=photo, width=30,command=photoss)
    photos.place(relx=0, rely=0, x=50, y=50, width=100)
    videos = Button(wall, text="VIDEOS", image=video, width=30,command=browser)
    videos.place(relx=0, rely=0, x=50, y=200, width=100)
    settings = Button(wall, text="SETTINGS", width=30, image=cal,command=calc)
    settings.place(relx=0, rely=0, x=50, y=350, width=100)
    music = Button(wall, text="MUSIC", image=music2, width=30,command=musicp)
    music.place(relx=0, rely=0, x=50, y=500, width=100)
    maps=Button(wall,text="MAPS", image=mapp, width=30,command=mappp)
    maps.place(relx=0, rely=0, x=50, y=650, width=100)
    search=Entry(wall,width=80)
    search.place(relx=0.5,x=-200, rely=0,y=50)
    sear=PhotoImage(file=r"search.png")
    searchb=Button(wall,width=10,text="Search",imag=sear,command=searchwall)
    searchb.place(relx=0.5,x=-280, rely=0,y=35)
    s=Message(wall,text="Enter URL",bg="black",fg="white")
    s.place(relx=0.5,x=300, rely=0,y=50)
    gam=PhotoImage(file=r"g.png")
    gaming=Button(wall,width=30,image=gam,command=games)
    gaming.place(relx=0, rely=0, x=200, y=50, width=100)
    mainloop()
def applock():

    class Example(Frame):

        def __init__(self):
            super().__init__()
            self.loadImage()
            self.initUI()

        def loadImage(self):
            try:
                self.img = Image.open("abs.jpg")

            except IOError:
                print("Unable to load image")
                sys.exit(1)

        def initUI(self):

            self.master.title("CodeX USERS")
            tatras = ImageTk.PhotoImage(self.img)
            label = Label(self, image=tatras)
            label.image = tatras
            label.pack()
            self.pack()

        def setGeometry(self):
            w, h = self.img.size

            #important
            self.master.geometry(("1550x867+-7+-2"))


    def us():
        window=Tk()
        window.geometry("300x150")
        window.title("ABOUT US")
        window.configure(bg="black")
        details=Message(window,text="DEVELOPERS:\n\nARPIT PANDEY\nROHAN MALLICK\nKETAN SUHAAS\n\nCODEX, IIT ROORKEE",bg="black",fg="white")
        details.pack()

    master = Tk()
    master.title("CodeX USERS")
    master.overrideredirect(True)
    app = FullScreenApp(master)
    #master.geometry("1920x1080")
    img="abs.jpg"
    ex=Example()
    ex.setGeometry()


    def clicklog():
        master.destroy()
        loginx = Tk()
        C = Canvas(loginx, bg="blue", height=500, width=600)
        filename = PhotoImage(file=r"asb.png")
        background_label = Label(loginx, image=filename, width=100)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        #filename = PhotoImage(file=r"shut2.png")
        #shut = Button(loginx, image=filename, width=30)
        #shut.place(relx=0, rely=0, anchor=NW)
        loginx.title("CodeX LOGIN")
        loginx.overrideredirect(True)
        app = FullScreenApp(loginx)
        loginx.geometry(("1550x867+-7+-2"))
        # login.configure(bg="black")
        un = Message(loginx, text="USERNAME:",bg='black',fg="white",width=100)
        un.place(relx=0.5, rely=0.5, y=-100,x=-30, anchor=SE)
        entryname = Entry(loginx, width=20)
        entryname.place(relx=0.5, rely=0.5, y=-100, anchor=SW)
        ps = Message(loginx, text="PASSWORD:",bg='black',fg="white",width=100)
        ps.place(relx=0.5, rely=0.5, y=-100,x=-30, anchor=NE)
        paswd = Entry(loginx, width=20)
        paswd.place(relx=0.5, rely=0.5, y=-100, anchor=NW)
        def hint():
            w=Tk()
            w.title("HINT")
            w.configure(bg="black")
            w.geometry("600x400")
            messageVar = Message(w, text = "Hint - Both Username And Password Are 8 Digits Long!")
            messageVar.config(bg='black',fg="white")
            messageVar.place(relx=0.5,rely=0.5)
        fpass=Button(loginx,text="Forgot Password?",command=hint)
        fpass.place(relx=0.5, rely=0.5,x=80, y=-50, anchor=N)


        def input():
            f=1
            f1=f2="b"
            i=entryname.get()
            i=str(i)
            j=paswd.get()
            j=str(j)
            file=open("regu.txt","r")
            if(i=="a" and j=="a"):
                loginx.destroy()
                homescreen()

            else:
                if (len(i) is 8 and len(j) is 8):
                    while(f1!="" or f2!=""):
                        f1 = file.read(8)
                        f2 = file.read(8)


                        if (i) ==(f1) and (j) == (f2):
                            submit.configure(text="SUBMITTED")
                            f=0


                if(f==0):
                    loginx.destroy()
                    homescreen()

                else:
                    error=Tk()
                    error.title("ERROR")
                    error.configure(bg="black")
                    error.geometry("300x300")
                    err=Message(error,text="INVALID Details, Try Again!",bg='black',fg="white")
                    err.place(relx=0.5,rely=0.5,anchor=CENTER)

        submit = Button(loginx,text="SUBMIT",command=input)
        submit.place(relx=0.5, rely=0.5,x=-20, y=-50, anchor=N)
        loginx.mainloop()
    def set():

        master.destroy()
        login = Tk()
        login.overrideredirect(True)
        app = FullScreenApp(login)
        C = Canvas(login, bg="blue", height=500, width=600)
        filename = PhotoImage(file=r"abs.png")
        background_label = Label(login, image=filename, width=100)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        login.title("CodeX REGISTER")
        login.geometry(("1550x867+-7+-2"))
        un = Label(login, text="USERNAME:")
        entryname = Entry(login, width=20)
        entryname.place(relx=0.5, rely=0.5, y=-100, anchor=SW)
        un.place(relx=0.5, rely=0.5, y=-100, anchor=SE)
        ps = Label(login, text="PASSWORD:")
        ps.place(relx=0.5, rely=0.5, y=-100, anchor=NE)
        paswd = Entry(login, width=20)
        paswd.place(relx=0.5, rely=0.5, y=-100, anchor=NW)
        def input():
                global originalname
                global originalpaswd
                file=open("regu.txt","a")
                originalname=entryname.get()
                originalpaswd=paswd.get()
                file.write(originalname+originalpaswd)
                file.close()
                submit.configure(text="REGISTERED")
                login.destroy()
                applock()
        submit = Button(login, text="REGISTER", command=input)
        submit.place(relx=0.5, rely=0.5, y=-50, anchor=N)
        login.mainloop()
    log=PhotoImage(file=r"log.png")
    reg=PhotoImage(file=r"reg.png")


    b1 = Button(master, text="LOGIN",width=30,image=log,command=clicklog)
    b1.place(relx=0.5,rely=0.5, anchor=S)
    b3 = Button(master, text="REGISTER",width=30,image=reg,command=set)
    b3.place(relx=0.5, rely=0.5, y=50, anchor=N)
    ext = PhotoImage(file=r"shutd.png")
    b2 = Button(master, text="EXIT",width=30,image=ext,command=master.destroy)
    b2.place(relx=1, rely=1,x=-10, anchor=SE)
    mainloop()
def musicp():
    wall.destroy()
    global paused,muted
   # n=Tk()
    root = tk.ThemedTk()
    #root.get_themes()                 # Returns a list of all themes that can be set
    #root.set_theme("radiance")         # Sets an available theme

    # Fonts - Arial (corresponds to Helvetica), Courier New (Courier), Comic Sans MS, Fixedsys,
    # MS Sans Serif, MS Serif, Symbol, System, Times New Roman (Times), and Verdana
    #
    # Styles - normal, bold, roman, italic, underline, and overstrike.

    statusbar = ttk.Label(root, text="CodeX", relief=SUNKEN, anchor=W, font='Times 10 italic')
    statusbar.pack(side=BOTTOM, fill=X)

    # Create the menubar
    menubar = Menu(root,background='#374140',foreground="black",activebackground='#374140',activeforeground="black")
    root.config(menu=menubar)

    # Create the submenu

    subMenu = Menu(menubar, tearoff=0)

    playlist = []


    # playlist - contains the full path + filename
    # playlistbox - contains just the filename
    # Fullpath + filename is required to play the music inside play_music load function

    def browse_file():
        global filename_path
        filename_path = filedialog.askopenfilename()
        add_to_playlist(filename_path)

        mixer.music.queue(filename_path)


    def add_to_playlist(filename):
        filename = os.path.basename(filename)
        index = 0
        playlistbox.insert(index, filename)
        playlist.insert(index, filename_path)
        index += 1


    menubar.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Open", command=browse_file)
    subMenu.add_command(label="Exit", command=root.destroy)


    def about_us():
        tkinter.messagebox.showinfo('CodeX MUSIC', 'BUILT BY TEAM CodeX')


    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=subMenu)
    subMenu.add_command(label="About Us", command=about_us)

    mixer.init()  # initializing the mixer

    root.title("CodeX MUSIC")
    root.iconbitmap(r'images/melody.ico')

    # Root Window - StatusBar, LeftFrame, RightFrame
    # LeftFrame - The listbox (playlist)
    # RightFrame - TopFrame,MiddleFrame and the BottomFrame

    leftframe = Frame(root)
    leftframe.pack(side=LEFT, padx=30, pady=30)

    playlistbox = Listbox(leftframe)
    playlistbox.pack()

    addBtn = ttk.Button(leftframe, text="+ Add", command=browse_file)
    addBtn.pack(side=LEFT)


    def del_song():
        selected_song = playlistbox.curselection()
        selected_song = int(selected_song[0])
        playlistbox.delete(selected_song)
        playlist.pop(selected_song)


    delBtn = ttk.Button(leftframe, text="- Del", command=del_song)
    delBtn.pack(side=LEFT)

    rightframe = Frame(root)
    rightframe.pack(pady=30)

    topframe = Frame(rightframe)
    topframe.pack()

    lengthlabel = ttk.Label(topframe, text='Total Length : --:--')
    lengthlabel.pack(pady=5)

    currenttimelabel = ttk.Label(topframe, text='Current Time : --:--', relief=GROOVE)
    currenttimelabel.pack()


    def show_details(play_song):
        file_data = os.path.splitext(play_song)

        if file_data[1] == '.mp3':
            audio = MP3(play_song)
            total_length = audio.info.length
        else:
            a = mixer.Sound(play_song)
            total_length = a.get_length()

        # div - total_length/60, mod - total_length % 60
        mins, secs = divmod(total_length, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        lengthlabel['text'] = "Total Length" + ' - ' + timeformat

        t1 = threading.Thread(target=start_count, args=(total_length,))
        t1.start()


    def start_count(t):
        global paused
        # mixer.music.get_busy(): - Returns FALSE when we press the stop button (music stop playing)
        # Continue - Ignores all of the statements below it. We check if music is paused or not.
        current_time = 0
        while current_time <= t and mixer.music.get_busy():
            if paused:
                continue
            else:
                mins, secs = divmod(current_time, 60)
                mins = round(mins)
                secs = round(secs)
                timeformat = '{:02d}:{:02d}'.format(mins, secs)
                currenttimelabel['text'] = "Current Time" + ' - ' + timeformat
                time.sleep(1)
                current_time += 1


    def play_music():
        global paused

        if paused:
            mixer.music.unpause()
            statusbar['text'] = "Music Resumed"
            paused = FALSE
        else:
            try:
                stop_music()
                time.sleep(1)
                selected_song = playlistbox.curselection()
                selected_song = int(selected_song[0])
                play_it = playlist[selected_song]
                mixer.music.load(play_it)
                mixer.music.play()
                statusbar['text'] = "Playing music" + ' - ' + os.path.basename(play_it)
                show_details(play_it)
            except:
                tkinter.messagebox.showerror('File not found', 'CodeX MUSIC could not find the file. Please check again.')


    def stop_music():
        mixer.music.stop()
        statusbar['text'] = "Music Stopped"


    paused = FALSE


    def pause_music():
        global paused
        paused = TRUE
        mixer.music.pause()
        statusbar['text'] = "Music Paused"


    def rewind_music():
        play_music()
        statusbar['text'] = "Music Rewinded"


    def set_vol(val):
        volume = float(val) / 100
        mixer.music.set_volume(volume)
        # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1


    muted = FALSE


    def mute_music():
        global muted
        if muted:  # Unmute the music
            mixer.music.set_volume(0.7)
            volumeBtn.configure(image=volumePhoto)
            scale.set(70)
            muted = FALSE
        else:  # mute the music
            mixer.music.set_volume(0)
            volumeBtn.configure(image=mutePhoto)
            scale.set(0)
            muted = TRUE


    middleframe = Frame(rightframe)
    middleframe.pack(pady=30, padx=30)


    playPhoto = PhotoImage(file='images/play.png')
    playBtn = ttk.Button(middleframe, image=playPhoto, command=play_music)
    playBtn.grid(row=0, column=0, padx=10)

    stopPhoto = PhotoImage(file='images/stop.png')
    stopBtn = ttk.Button(middleframe, image=stopPhoto, command=stop_music)
    stopBtn.grid(row=0, column=1, padx=10)

    pausePhoto = PhotoImage(file='images/pause.png')
    pauseBtn = ttk.Button(middleframe, image=pausePhoto, command=pause_music)
    pauseBtn.grid(row=0, column=2, padx=10)

    # Bottom Frame for volume, rewind, mute etc.

    bottomframe = Frame(rightframe)
    bottomframe.pack()


    rewindPhoto = PhotoImage(file='images/rewind.png')
    rewindBtn = ttk.Button(bottomframe, image=rewindPhoto, command=rewind_music)
    rewindBtn.grid(row=0, column=0)

    mutePhoto = PhotoImage(file='images/mute.png')
    volumePhoto = PhotoImage(file='images/volume.png')
    volumeBtn = ttk.Button(bottomframe, image=volumePhoto, command=mute_music)
    volumeBtn.grid(row=0, column=1)

    scale = ttk.Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
    scale.set(70)  # implement the default value of scale when music player starts
    mixer.music.set_volume(0.7)
    scale.grid(row=0, column=2, pady=15, padx=30)


    def on_closing():
        stop_music()
        root.destroy()
        homescreen()


    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
def photo():
    class FullScreenApp(object):
        def __init__(self, master, **kwargs):
            self.master = master
            pad = 3
            self._geom = '200x200+0+0'
            master.geometry("{0}x{1}+0+0".format(
                master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
            master.bind('<Escape>', self.toggle_geom)

        def toggle_geom(self, event):
            geom = self.master.winfo_geometry()
            print(geom, self._geom)
            self.master.geometry(self._geom)
            self._geom = geom

    class App(Frame):
        def chg_image(self):
            if self.im.mode == "1":  # bitmap image
                self.img = PIL.ImageTk.BitmapImage(self.im, foreground="black")
            else:  # photo image
                self.img = PIL.ImageTk.PhotoImage(self.im)
            self.la.config(image=self.img, bg="#000000",
                           width=self.img.width(), height=self.img.height())

        def open(self):
            filename = filedialog.askopenfilename()
            if filename != "":
                self.im = PIL.Image.open(filename)
            self.chg_image()
            self.num_page = 0
            self.num_page_tv.set(str(self.num_page + 1))

        def seek_prev(self):
            self.num_page = self.num_page - 1
            if self.num_page < 0:
                self.num_page = 0
            self.im.seek(self.num_page)
            self.chg_image()
            self.num_page_tv.set(str(self.num_page + 1))

        def seek_next(self):
            self.num_page = self.num_page + 1
            try:
                self.im.seek(self.num_page)
            except:
                self.num_page = self.num_page - 1
            self.chg_image()
            self.num_page_tv.set(str(self.num_page + 1))

        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master.title('PHOTOS')

            self.num_page = 0
            self.num_page_tv = StringVar()

            fram = Frame(self)
            Button(fram, text="OPEN FILE", command=self.open).pack(side=LEFT)
            Button(fram, text="PREV", command=self.seek_prev).pack(side=LEFT)
            Button(fram, text="NEXT", command=self.seek_next).pack(side=LEFT)
            Label(fram, textvariable=self.num_page_tv).pack(side=LEFT)
            fram.pack(side=TOP, fill=BOTH)

            self.la = Label(self)
            self.la.pack()

            self.pack()
    wall.destroy()
    if __name__ == "__main__":
        app = App(); app.mainloop()

def mappp():
    wall.destroy()
    import pygmaps
    from cefpython3 import cefpython as cef
    import ctypes
    try:
        import tkinter as tk
    except ImportError:
        import Tkinter as tk
    import sys
    import os
    import platform
    import logging as _logging

    # Fix for PyCharm hints warnings
    WindowUtils = cef.WindowUtils()

    # Platforms
    WINDOWS = (platform.system() == "Windows")
    LINUX = (platform.system() == "Linux")
    MAC = (platform.system() == "Darwin")

    # Globals
    logger = _logging.getLogger("tkinter_.py")

    # Constants
    # Tk 8.5 doesn't support png images
    IMAGE_EXT = ".png" if tk.TkVersion > 8.5 else ".gif"

    class MainFrame(tk.Frame):

        def __init__(self, root):
            self.browser_frame = None
            self.navigation_bar = None

            # Root
            root.geometry("1500x820+20+0")
            tk.Grid.rowconfigure(root, 0, weight=1)
            tk.Grid.columnconfigure(root, 0, weight=1)

            # MainFrame
            tk.Frame.__init__(self, root)
            self.master.title("Tkinter example")
            self.master.protocol("WM_DELETE_WINDOW", self.on_close)
            self.master.bind("<Configure>", self.on_root_configure)
            self.setup_icon()
            self.bind("<Configure>", self.on_configure)
            self.bind("<FocusIn>", self.on_focus_in)
            self.bind("<FocusOut>", self.on_focus_out)

            # NavigationBar
            self.navigation_bar = NavigationBar(self)
            self.navigation_bar.grid(row=0, column=0,
                                     sticky=(tk.N + tk.S + tk.E + tk.W))
            tk.Grid.rowconfigure(self, 0, weight=0)
            tk.Grid.columnconfigure(self, 0, weight=0)

            # BrowserFrame
            self.browser_frame = BrowserFrame(self, self.navigation_bar)
            self.browser_frame.grid(row=1, column=0,
                                    sticky=(tk.N + tk.S + tk.E + tk.W))
            tk.Grid.rowconfigure(self, 1, weight=1)
            tk.Grid.columnconfigure(self, 0, weight=1)

            # Pack MainFrame
            self.pack(fill=tk.BOTH, expand=tk.YES)

        def on_root_configure(self, _):
            logger.debug("MainFrame.on_root_configure")
            if self.browser_frame:
                self.browser_frame.on_root_configure()

        def on_configure(self, event):
            logger.debug("MainFrame.on_configure")
            if self.browser_frame:
                width = event.width
                height = event.height
                if self.navigation_bar:
                    height = height - self.navigation_bar.winfo_height()
                self.browser_frame.on_mainframe_configure(width, height)

        def on_focus_in(self, _):
            logger.debug("MainFrame.on_focus_in")

        def on_focus_out(self, _):
            logger.debug("MainFrame.on_focus_out")

        def on_close(self):
            if self.browser_frame:
                self.browser_frame.on_root_close()
            self.master.destroy()

        def get_browser(self):
            if self.browser_frame:
                return self.browser_frame.browser
            return None

        def get_browser_frame(self):
            if self.browser_frame:
                return self.browser_frame
            return None

        def setup_icon(self):
            resources = os.path.join(os.path.dirname(__file__), "resources")
            icon_path = os.path.join(resources, "tkinter" + IMAGE_EXT)
            if os.path.exists(icon_path):
                self.icon = tk.PhotoImage(file=icon_path)
                # noinspection PyProtectedMember
                self.master.call("wm", "iconphoto", self.master._w, self.icon)

    class BrowserFrame(tk.Frame):

        def __init__(self, master, navigation_bar=None):
            self.navigation_bar = navigation_bar
            self.closing = False
            self.browser = None
            tk.Frame.__init__(self, master)

            global x, y, k, i, j, app, root, a
            b1 = Button(master, text="N", command=f3)
            b1.place(rely=0.7, x=50)
            b2 = Button(master, text="S", command=f4)
            b2.place(rely=0.7, x=50, y=50)
            b3 = Button(master, text="W", command=f2)
            b3.place(rely=0.7, y=25)
            b4 = Button(master, text="E", command=f1)
            b4.place(rely=0.7, x=100, y=25)
            l1 = Button(master, text="OUT", width="10", command=f5)
            l1.place(rely=0.7, x=50, y=90)
            l2 = Button(master, text="IN", width="10", command=f6)
            l2.place(rely=0.7, x=50, y=120)
            l3 = Button(master, text="Save", command=f8)
            l3.place(rely=0.7, x=50, y=-120)
            l4 = Button(master, text="Toggle", command=f7)
            l4.place(rely=0.7, x=50, y=-150)

            self.bind("<FocusIn>", self.on_focus_in)
            self.bind("<FocusOut>", self.on_focus_out)
            self.bind("<Configure>", self.on_configure)
            self.focus_set()

        def embed_browser(self):
            window_info = cef.WindowInfo()
            rect = [0, 0, self.winfo_width(), self.winfo_height()]
            window_info.SetAsChild(self.get_window_handle(), rect)
            self.browser = cef.CreateBrowserSync(window_info,
                                                 url="D:\\pygmap1.html")  # todo
            assert self.browser
            self.browser.SetClientHandler(LoadHandler(self))
            self.browser.SetClientHandler(FocusHandler(self))
            self.message_loop_work()

        def get_window_handle(self):
            if self.winfo_id() > 0:
                return self.winfo_id()
            elif MAC:
                # On Mac window id is an invalid negative value (Issue #308).
                # This is kind of a dirty hack to get window handle using
                # PyObjC package. If you change structure of windows then you
                # need to do modifications here as well.
                # noinspection PyUnresolvedReferences
                from AppKit import NSApp
                # noinspection PyUnresolvedReferences
                import objc
                # Sometimes there is more than one window, when application
                # didn't close cleanly last time Python displays an NSAlert
                # window asking whether to Reopen that window.
                # noinspection PyUnresolvedReferences
                return objc.pyobjc_id(NSApp.windows()[-1].contentView())
            else:
                raise Exception("Couldn't obtain window handle")

        def message_loop_work(self):
            cef.MessageLoopWork()
            self.after(10, self.message_loop_work)

        def on_configure(self, _):
            if not self.browser:
                self.embed_browser()

        def on_root_configure(self):
            # Root <Configure> event will be called when top window is moved
            if self.browser:
                self.browser.NotifyMoveOrResizeStarted()

        def on_mainframe_configure(self, width, height):
            if self.browser:
                if WINDOWS:
                    ctypes.windll.user32.SetWindowPos(
                        self.browser.GetWindowHandle(), 0,
                        0, 0, width, height, 0x0002)
                elif LINUX:
                    self.browser.SetBounds(0, 0, width, height)
                self.browser.NotifyMoveOrResizeStarted()

        def on_focus_in(self, _):
            logger.debug("BrowserFrame.on_focus_in")
            if self.browser:
                self.browser.SetFocus(True)

        def on_focus_out(self, _):
            logger.debug("BrowserFrame.on_focus_out")
            if self.browser:
                self.browser.SetFocus(False)

        def on_root_close(self):
            if self.browser:
                self.browser.CloseBrowser(True)
                self.clear_browser_references()
            self.destroy()

        def clear_browser_references(self):
            # Clear browser references that you keep anywhere in your
            # code. All references must be cleared for CEF to shutdown cleanly.
            self.browser = None

    class LoadHandler(object):

        def __init__(self, browser_frame):
            self.browser_frame = browser_frame

        def OnLoadStart(self, browser, **_):
            if self.browser_frame.master.navigation_bar:
                self.browser_frame.master.navigation_bar.set_url(browser.GetUrl())

    class FocusHandler(object):

        def __init__(self, browser_frame):
            self.browser_frame = browser_frame

        def OnTakeFocus(self, next_component, **_):
            logger.debug("FocusHandler.OnTakeFocus, next={next}"
                         .format(next=next_component))

        def OnSetFocus(self, source, **_):
            logger.debug("FocusHandler.OnSetFocus, source={source}"
                         .format(source=source))
            return False

        def OnGotFocus(self, **_):
            """Fix CEF focus issues (#255). Call browser frame's focus_set
               to get rid of type cursor in url entry widget."""
            logger.debug("FocusHandler.OnGotFocus")
            self.browser_frame.focus_set()

    class NavigationBar(tk.Frame):
        def __init__(self, master):
            self.back_state = tk.NONE
            self.forward_state = tk.NONE
            self.back_image = None
            self.forward_image = None
            self.reload_image = None

            tk.Frame.__init__(self, master)
            resources = os.path.join(os.path.dirname(__file__), "resources")

            # Back button
            back_png = os.path.join(resources, "back" + IMAGE_EXT)
            if os.path.exists(back_png):
                self.back_image = tk.PhotoImage(file=back_png)
            self.back_button = tk.Button(self, image=self.back_image,
                                         command=self.go_back)
            self.back_button.grid(row=0, column=0)

            # Forward button
            forward_png = os.path.join(resources, "forward" + IMAGE_EXT)
            if os.path.exists(forward_png):
                self.forward_image = tk.PhotoImage(file=forward_png)
            self.forward_button = tk.Button(self, image=self.forward_image,
                                            command=self.go_forward)
            self.forward_button.grid(row=0, column=1)

            # Reload button
            reload_png = os.path.join(resources, "reload" + IMAGE_EXT)
            if os.path.exists(reload_png):
                self.reload_image = tk.PhotoImage(file=reload_png)
            self.reload_button = tk.Button(self, image=self.reload_image,
                                           command=self.reload)
            self.reload_button.grid(row=0, column=2)

            # Url entry
            self.url_entry = tk.Entry(self)
            self.url_entry.bind("<FocusIn>", self.on_url_focus_in)
            self.url_entry.bind("<FocusOut>", self.on_url_focus_out)
            self.url_entry.bind("<Return>", self.on_load_url)
            self.url_entry.bind("<Button-1>", self.on_button1)
            self.url_entry.grid(row=0, column=3,
                                sticky=(tk.N + tk.S + tk.E + tk.W))
            tk.Grid.rowconfigure(self, 0, weight=100)
            tk.Grid.columnconfigure(self, 3, weight=100)

            # Update state of buttons
            self.update_state()

        def go_back(self):
            if self.master.get_browser():
                self.master.get_browser().GoBack()

        def go_forward(self):
            if self.master.get_browser():
                self.master.get_browser().GoForward()

        def reload(self):
            if self.master.get_browser():
                self.master.get_browser().Reload()

        def set_url(self, url):
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url)

        def on_url_focus_in(self, _):
            logger.debug("NavigationBar.on_url_focus_in")

        def on_url_focus_out(self, _):
            logger.debug("NavigationBar.on_url_focus_out")

        def on_load_url(self, _):
            if self.master.get_browser():
                self.master.get_browser().StopLoad()
                self.master.get_browser().LoadUrl(self.url_entry.get())

        def on_button1(self, _):
            """Fix CEF focus issues (#255). See also FocusHandler.OnGotFocus."""
            logger.debug("NavigationBar.on_button1")
            self.master.master.focus_force()

        def update_state(self):
            browser = self.master.get_browser()
            if not browser:
                if self.back_state != tk.DISABLED:
                    self.back_button.config(state=tk.DISABLED)
                    self.back_state = tk.DISABLED
                if self.forward_state != tk.DISABLED:
                    self.forward_button.config(state=tk.DISABLED)
                    self.forward_state = tk.DISABLED
                self.after(100, self.update_state)
                return
            if browser.CanGoBack():
                if self.back_state != tk.NORMAL:
                    self.back_button.config(state=tk.NORMAL)
                    self.back_state = tk.NORMAL
            else:
                if self.back_state != tk.DISABLED:
                    self.back_button.config(state=tk.DISABLED)
                    self.back_state = tk.DISABLED
            if browser.CanGoForward():
                if self.forward_state != tk.NORMAL:
                    self.forward_button.config(state=tk.NORMAL)
                    self.forward_state = tk.NORMAL
            else:
                if self.forward_state != tk.DISABLED:
                    self.forward_button.config(state=tk.DISABLED)
                    self.forward_state = tk.DISABLED
            self.after(100, self.update_state)

    global x, y, k, i, j, app, root, a
    a = [[0] * 10] * 10
    app = Tk()
    root = Tk()
    y = 30.8
    x = 77.7
    k = 0.1
    j = 0
    i = 0
    mymap1 = pygmaps.pygmaps(y, x, 15)
    mymap1.draw('pygmap1.html')

    def f1():
        global x, y, k
        x += k

        mymap1 = pygmaps.pygmaps(y, x, 15)
        mymap1.draw('pygmap1.html')
        m()

    def f2():
        global x, y, k
        x -= k

        mymap1 = pygmaps.pygmaps(y, x, 15)
        mymap1.draw('pygmap1.html')
        m()

    def f3():
        global x, y, k
        y += k

        mymap1 = pygmaps.pygmaps(y, x, 15)
        mymap1.draw('pygmap1.html')
        m()

    def f4():
        global x, y, k
        y -= k

        mymap1 = pygmaps.pygmaps(y, x, 15)
        mymap1.draw('pygmap1.html')
        m()

    def f5():
        global x, y, k
        k += k

    def f6():
        global x, y, k
        k = k / 2

    def f7():
        global j, i, a, x, y
        if (j >= i):
            j = j % i
        else:
            mymap1 = pygmaps.pygmaps(a[j][2], a[j][1], 15)
            mymap1.draw('pygmap1.html')
            x = a[j][1]
            y = a[j][2]
            j += 1
            m()

    def f8():
        global i, a, x, y
        a[i][1] = x
        a[i][2] = y
        i = i + 1

    def m():
        global app, root
        if __name__ == '__main__':
            app.destroy()
            root.destroy()
            logger.setLevel(_logging.INFO)
            stream_handler = _logging.StreamHandler()
            formatter = _logging.Formatter("[%(filename)s] %(message)s")
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)
            logger.info("CEF Python {ver}".format(ver=cef.__version__))
            logger.info("Python {ver} {arch}".format(
                ver=platform.python_version(), arch=platform.architecture()[0]))
            logger.info("Tk {ver}".format(ver=tk.Tcl().eval('info patchlevel')))
            assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"
            sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
            root = tk.Tk()
            app = MainFrame(root)
            # Tk must be initialized before CEF otherwise fatal error (Issue #306)
            cef.Initialize()

            app.mainloop()
            cef.Shutdown()

    m()
    homescreen()

def games():
    wall.destroy()
    def snakem():
        game.destroy()

        # !/usr/bin/env python3

        import sys
        import random
        from PIL import Image, ImageTk
        from tkinter import Tk, Frame, Canvas, ALL, NW

        class Cons:

            BOARD_WIDTH = 300
            BOARD_HEIGHT = 300
            DELAY = 100
            DOT_SIZE = 10
            MAX_RAND_POS = 27

        class Board(Canvas):

            def __init__(self):
                super().__init__(width=Cons.BOARD_WIDTH, height=Cons.BOARD_HEIGHT,
                                 background="black", highlightthickness=0)

                self.initGame()
                self.pack()

            def initGame(self):
                '''initializes game'''

                self.inGame = True
                self.dots = 5
                self.score = 0

                # variables used to move snake object
                self.moveX = Cons.DOT_SIZE
                self.moveY = 0

                # starting apple coordinates
                self.appleX = 100
                self.appleY = 190

                self.loadImages()

                self.createObjects()
                self.locateApple()
                self.bind_all("<Key>", self.onKeyPressed)
                self.after(Cons.DELAY, self.onTimer)

            def loadImages(self):
                '''loads images from the disk'''

                try:
                    self.idot = Image.open("dot.png")
                    self.dot = ImageTk.PhotoImage(self.idot)
                    self.ihead = Image.open("head.png")
                    self.head = ImageTk.PhotoImage(self.ihead)
                    self.iapple = Image.open("apple.png")
                    self.apple = ImageTk.PhotoImage(self.iapple)

                except IOError as e:

                    print(e)
                    sys.exit(1)

            def createObjects(self):
                '''creates objects on Canvas'''

                self.create_text(30, 10, text="Score: {0}".format(self.score),
                                 tag="score", fill="white")
                self.create_image(self.appleX, self.appleY, image=self.apple,
                                  anchor=NW, tag="apple")
                self.create_image(50, 50, image=self.head, anchor=NW, tag="head")
                self.create_image(30, 50, image=self.dot, anchor=NW, tag="dot")
                self.create_image(40, 50, image=self.dot, anchor=NW, tag="dot")

            def checkAppleCollision(self):
                '''checks if the head of snake collides with apple'''

                apple = self.find_withtag("apple")
                head = self.find_withtag("head")

                x1, y1, x2, y2 = self.bbox(head)
                overlap = self.find_overlapping(x1, y1, x2, y2)

                for ovr in overlap:

                    if apple[0] == ovr:
                        self.score += 1
                        x, y = self.coords(apple)
                        self.create_image(x, y, image=self.dot, anchor=NW, tag="dot")
                        self.locateApple()

            def moveSnake(self):
                '''moves the Snake object'''

                dots = self.find_withtag("dot")
                head = self.find_withtag("head")

                items = dots + head

                z = 0
                while z < len(items) - 1:
                    c1 = self.coords(items[z])
                    c2 = self.coords(items[z + 1])
                    self.move(items[z], c2[0] - c1[0], c2[1] - c1[1])
                    z += 1

                self.move(head, self.moveX, self.moveY)

            def checkCollisions(self):
                '''checks for collisions'''

                dots = self.find_withtag("dot")
                head = self.find_withtag("head")

                x1, y1, x2, y2 = self.bbox(head)
                overlap = self.find_overlapping(x1, y1, x2, y2)

                for dot in dots:
                    for over in overlap:
                        if over == dot:
                            self.inGame = False

                if x1 < 0:
                    self.inGame = False

                if x1 > Cons.BOARD_WIDTH - Cons.DOT_SIZE:
                    self.inGame = False

                if y1 < 0:
                    self.inGame = False

                if y1 > Cons.BOARD_HEIGHT - Cons.DOT_SIZE:
                    self.inGame = False

            def locateApple(self):
                '''places the apple object on Canvas'''

                apple = self.find_withtag("apple")
                self.delete(apple[0])

                r = random.randint(0, Cons.MAX_RAND_POS)
                self.appleX = r * Cons.DOT_SIZE
                r = random.randint(0, Cons.MAX_RAND_POS)
                self.appleY = r * Cons.DOT_SIZE

                self.create_image(self.appleX, self.appleY, anchor=NW,
                                  image=self.apple, tag="apple")

            def onKeyPressed(self, e):
                '''controls direction variables with cursor keys'''

                key = e.keysym

                LEFT_CURSOR_KEY = "Left"
                if key == LEFT_CURSOR_KEY and self.moveX <= 0:
                    self.moveX = -Cons.DOT_SIZE
                    self.moveY = 0

                RIGHT_CURSOR_KEY = "Right"
                if key == RIGHT_CURSOR_KEY and self.moveX >= 0:
                    self.moveX = Cons.DOT_SIZE
                    self.moveY = 0

                RIGHT_CURSOR_KEY = "Up"
                if key == RIGHT_CURSOR_KEY and self.moveY <= 0:
                    self.moveX = 0
                    self.moveY = -Cons.DOT_SIZE

                DOWN_CURSOR_KEY = "Down"
                if key == DOWN_CURSOR_KEY and self.moveY >= 0:
                    self.moveX = 0
                    self.moveY = Cons.DOT_SIZE

            def onTimer(self):
                '''creates a game cycle each timer event'''

                self.drawScore()
                self.checkCollisions()

                if self.inGame:
                    self.checkAppleCollision()
                    self.moveSnake()
                    self.after(Cons.DELAY, self.onTimer)
                else:
                    self.gameOver()

            def drawScore(self):
                '''draws score'''

                score = self.find_withtag("score")
                self.itemconfigure(score, text="Score: {0}".format(self.score))

            def gameOver(self):
                '''deletes all objects and draws game over message'''

                self.delete(ALL)
                self.create_text(self.winfo_width() / 2, self.winfo_height() / 2,
                                 text="Game Over with score {0}".format(self.score), fill="white")

        class Snake(Frame):

            def __init__(self):
                super().__init__()

                self.master.title('Snake')
                self.board = Board()
                self.pack()

        def main():

            root = Tk()
            nib = Snake()
            root.mainloop()

        if __name__ == '__main__':
            main()

    def tac():
        ########
        import os
        import threading
        import time
        import tkinter.messagebox
        import webbrowser
        from tkinter import Tk, Button
        from tkinter.font import Font
        from copy import deepcopy

        import urllib.request

        from tkinter import ttk
        from tkinter.filedialog import askopenfilename
        import re

        from tkinter import filedialog

        import math
        import sys
        import random
        from PIL import Image, ImageTk
        from tkinter import Tk, Frame, Canvas, ALL, NW

        from tkinter import ttk
        from ttkthemes import themed_tk as tk

        import tkinter.messagebox

        from mutagen.mp3 import MP3
        from pygame import mixer
        # coding=UTF8

        class Board:

            def __init__(self, other=None):
                self.player = 'X'
                self.opponent = 'O'
                self.empty = '.'
                self.size = 3
                self.fields = {}
                for y in range(self.size):
                    for x in range(self.size):
                        self.fields[x, y] = self.empty
                # copy constructor
                if other:
                    self.__dict__ = deepcopy(other.__dict__)

            def move(self, x, y):
                board = Board(self)
                board.fields[x, y] = board.player
                (board.player, board.opponent) = (board.opponent, board.player)
                return board

            def __minimax(self, player):
                if self.won():
                    if player:
                        return (-1, None)
                    else:
                        return (+1, None)
                elif self.tied():
                    return (0, None)
                elif player:
                    best = (-2, None)
                    for x, y in self.fields:
                        if self.fields[x, y] == self.empty:
                            value = self.move(x, y).__minimax(not player)[0]
                            if value > best[0]:
                                best = (value, (x, y))
                    return best
                else:
                    best = (+2, None)
                    for x, y in self.fields:
                        if self.fields[x, y] == self.empty:
                            value = self.move(x, y).__minimax(not player)[0]
                            if value < best[0]:
                                best = (value, (x, y))
                    return best

            def best(self):
                return self.__minimax(True)[1]

            def tied(self):
                for (x, y) in self.fields:
                    if self.fields[x, y] == self.empty:
                        return False
                return True

            def won(self):
                # horizontal
                for y in range(self.size):
                    winning = []
                    for x in range(self.size):
                        if self.fields[x, y] == self.opponent:
                            winning.append((x, y))
                    if len(winning) == self.size:
                        return winning
                # vertical
                for x in range(self.size):
                    winning = []
                    for y in range(self.size):
                        if self.fields[x, y] == self.opponent:
                            winning.append((x, y))
                    if len(winning) == self.size:
                        return winning
                # diagonal
                winning = []
                for y in range(self.size):
                    x = y
                    if self.fields[x, y] == self.opponent:
                        winning.append((x, y))
                if len(winning) == self.size:
                    return winning
                # other diagonal
                winning = []
                for y in range(self.size):
                    x = self.size - 1 - y
                    if self.fields[x, y] == self.opponent:
                        winning.append((x, y))
                if len(winning) == self.size:
                    return winning
                # default
                return None

            def __str__(self):
                string = ''
                for y in range(self.size):
                    for x in range(self.size):
                        string += self.fields[x, y]
                    string += "\n"
                return string

        class GUI:

            def __init__(self):
                self.app = Tk()
                self.app.title('TICTACTOE')
                self.app.resizable(width=False, height=False)
                self.board = Board()
                self.font = Font(family="Helvetica", size=32)
                self.buttons = {}
                for x, y in self.board.fields:
                    handler = lambda x=x, y=y: self.move(x, y)
                    button = Button(self.app, command=handler, font=self.font, width=6, height=3)
                    button.grid(row=y, column=x)
                    self.buttons[x, y] = button
                handler = lambda: self.reset()
                button = Button(self.app, text='RESET', command=handler)
                button.grid(row=self.board.size + 1, column=0, columnspan=self.board.size, sticky="WE")
                self.update()

            def reset(self):
                self.board = Board()
                self.update()

            def move(self, x, y):
                self.app.config(cursor="watch")
                self.app.update()
                self.board = self.board.move(x, y)
                self.update()
                move = self.board.best()
                if move:
                    self.board = self.board.move(*move)
                    self.update()
                self.app.config(cursor="")

            def update(self):
                for (x, y) in self.board.fields:
                    text = self.board.fields[x, y]
                    self.buttons[x, y]['text'] = text
                    self.buttons[x, y]['disabledforeground'] = 'black'
                    if text == self.board.empty:
                        self.buttons[x, y]['state'] = 'normal'
                    else:
                        self.buttons[x, y]['state'] = 'disabled'
                winning = self.board.won()
                if winning:
                    for x, y in winning:
                        self.buttons[x, y]['disabledforeground'] = 'red'
                    for x, y in self.buttons:
                        self.buttons[x, y]['state'] = 'disabled'
                for (x, y) in self.board.fields:
                    self.buttons[x, y].update()

            def mainloop(self):
                self.app.mainloop()

        game.destroy()
        if __name__ == '__main__':
            GUI().mainloop()

    game = Tk()
    game.overrideredirect(True)
    app = FullScreenApp(game)
    img = "self.png"
    C = Canvas(game, bg="blue", height=500, width=600)
    filename = PhotoImage(file=r"gamewall.png")
    background_label = Label(game, image=filename, width=100)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    game.geometry("1550x867+-7+-2")
    snak = PhotoImage(file=r"snake.png")
    snakeb = Button(game, text="SNAKE", width=30, command=snakem, image=snak)
    snakeb.place(x=100, y=+100)
    t = PhotoImage(file=r"tic.png")
    tic = Button(game, text="TICTACTOE", width=30, command=tac, image=t)
    tic.place(x=100, y=+300)
    game.mainloop()
    homescreen()
def calc():
    import os
    import threading
    import time
    import tkinter.messagebox
    import webbrowser
    from tkinter import Tk, Button
    from tkinter.font import Font
    from copy import deepcopy

    import urllib.request

    from tkinter import ttk
    from tkinter.filedialog import askopenfilename
    import re

    from tkinter import filedialog

    import math
    import sys
    import random
    from PIL import Image, ImageTk
    from tkinter import Tk, Frame, Canvas, ALL, NW

    from tkinter import ttk
    from ttkthemes import themed_tk as tk

    import tkinter.messagebox

    from mutagen.mp3 import MP3
    from pygame import mixer


    class Calc():
        def __init__(self):
            self.total = 0
            self.current = ""
            self.new_num = True
            self.op_pending = False
            self.op = ""
            self.eq = False

        def num_press(self, num):
            self.eq = False
            temp = text_box.get()
            temp2 = str(num)
            if self.new_num:
                self.current = temp2
                self.new_num = False
            else:
                if temp2 == '.':
                    if temp2 in temp:
                        return
                self.current = temp + temp2
            self.display(self.current)

        def calc_total(self):
            self.eq = True
            self.current = float(self.current)
            if self.op_pending == True:
                self.do_sum()
            else:
                self.total = float(text_box.get())

        def display(self, value):
            text_box.delete(0, END)
            text_box.insert(0, value)

        def do_sum(self):
            if self.op == "add":
                self.total += self.current
            if self.op == "minus":
                self.total -= self.current
            if self.op == "times":
                self.total *= self.current
            if self.op == "divide":
                self.total /= self.current
            if self.op == "raise":
                self.total = self.total ** self.current
            if self.op == "rootof":
                self.total = self.total ** (1 / self.current)
            if self.op == "fact":
                self.total = int(text_box.get())
                self.total = math.factorial(self.total)
            if self.op == "ln":
                self.total = log(self.total)
            if self.op == "log":
                self.total = log(self.total, 10)
            if self.op == "sine":
                self.total = math.sin(self.total)
            if self.op == "cosine":
                self.total = math.cos(self.total)
            if self.op == "tangent":
                self.total = math.tan(self.total)
            if self.op == "exp":
                self.total = math.exp(self.total)
            if self.op == "inv":
                self.total = 1 / self.total
            self.new_num = True
            self.op_pending = False
            self.display(self.total)

        def operation(self, op):
            self.current = float(self.current)
            if self.op_pending:
                self.do_sum()
            elif not self.eq:
                self.total = self.current
            self.new_num = True
            self.op_pending = True
            self.op = op
            self.eq = False

        def clear(self):
            self.eq = False
            self.current = "0"
            self.display(0)
            self.new_num = True

        def all_clear(self):
            self.clear()
            self.total = 0

        def sign(self):
            self.eq = False
            self.current = -(float(text_box.get()))
            self.display(self.current)

    sum1 = Calc()
    root = Tk()
    calc = Frame(root)
    calc.grid()
    calc.configure(background="black")

    root.title("CALCULATOR")
    text_box = Entry(calc, justify=RIGHT, width=60)
    text_box.grid(row=0, column=0, columnspan=8, padx=30, pady=30)
    text_box.insert(0, "0")
    # text_box.focus()
    numbers = "789456123"
    i = 0
    bttn = []
    for j in range(1, 4):
        for k in range(3):
            bttn.append(Button(calc, height=2, width=4, padx=10, pady=10, text=numbers[i]))
            bttn[i]["bg"] = "red"
            bttn[i]["fg"] = "white"
            bttn[i].grid(row=j, column=k, padx=1, pady=1)
            bttn[i]["command"] = lambda x=numbers[i]: sum1.num_press(x)
            i += 1

    bttn_0 = Button(calc, height=2, width=4, padx=10, pady=10, text="0",bg="black",fg="white")
    bttn_0["command"] = lambda: sum1.num_press(0)
    bttn_0.grid(row=4, column=0, padx=1, pady=1)

    div = Button(calc, height=2, width=4, padx=10, pady=10, text="/",bg="black",fg="white")
    div["command"] = lambda: sum1.operation("divide")
    div.grid(row=1, column=3, padx=1, pady=1)

    mult = Button(calc, height=2, width=4, padx=10, pady=10, text="*",bg="black",fg="white")
    mult["command"] = lambda: sum1.operation("times")
    mult.grid(row=2, column=3, padx=1, pady=1)

    minus = Button(calc, height=2, width=4, padx=10, pady=10, text="-",bg="black",fg="white")
    minus["command"] = lambda: sum1.operation("minus")
    minus.grid(row=3, column=3, padx=1, pady=1)

    add = Button(calc, height=2, width=4, padx=10, pady=10, text="+",bg="black",fg="white")
    add["command"] = lambda: sum1.operation("add")
    add.grid(row=4, column=3, padx=1, pady=1)

    power = Button(calc, height=2, width=4, padx=10, pady=10, text="x^y",bg="black",fg="white")
    power["command"] = lambda: sum1.operation("raise")
    power.grid(row=2, column=4, padx=1, pady=1)

    rootof = Button(calc, height=2, width=4, padx=10, pady=10, text="y-\/x",bg="black",fg="white")
    rootof["command"] = lambda: sum1.operation("rootof")
    rootof.grid(row=2, column=5, padx=1, pady=1)

    fact = Button(calc, height=2, width=4, padx=10, pady=10, text="!",bg="black",fg="white")
    fact["command"] = lambda: sum1.operation("fact")
    fact.grid(row=3, column=4, padx=1, pady=1)

    loge = Button(calc, height=2, width=4, padx=10, pady=10, text="ln",bg="black",fg="white")
    loge["command"] = lambda: sum1.operation("ln")
    loge.grid(row=3, column=5, padx=1, pady=1)

    log10 = Button(calc, height=2, width=4, padx=10, pady=10, text="log",bg="black",fg="white")
    log10["command"] = lambda: sum1.operation("log")
    log10.grid(row=4, column=4, padx=1, pady=1)

    sine = Button(calc, height=2, width=4, padx=10, pady=10, text="sin",bg="black",fg="white")
    sine["command"] = lambda: sum1.operation("sine")
    sine.grid(row=5, column=0, padx=1, pady=1)

    cosine = Button(calc, height=2, width=4, padx=10, pady=10, text="cos",bg="black",fg="white")
    cosine["command"] = lambda: sum1.operation("cosine")
    cosine.grid(row=5, column=1, padx=1, pady=1)

    tangent = Button(calc, height=2, width=4, padx=10, pady=10, text="tan",bg="black",fg="white")
    tangent["command"] = lambda: sum1.operation("tangent")
    tangent.grid(row=5, column=2, padx=1, pady=1)

    exponent = Button(calc, height=2, width=4, padx=10, pady=10, text='e^x',bg="black",fg="white")
    exponent["command"] = lambda: sum1.operation("exp")
    exponent.grid(row=5, column=3, padx=1, pady=1)

    inv = Button(calc, height=2, width=4, padx=10, pady=10, text="1/x",bg="black",fg="white")
    inv["command"] = lambda: sum1.operation("inv")
    inv.grid(row=5, column=4, padx=1, pady=1)

    point = Button(calc, height=2, width=4, padx=10, pady=10, text=".",bg="black",fg="white")
    point["command"] = lambda: sum1.num_press(".")
    point.grid(row=4, column=1, padx=1, pady=1)

    neg = Button(calc, height=2, width=4, padx=10, pady=10, text="+/-",bg="black",fg="white")
    neg["command"] = sum1.sign
    neg.grid(row=4, column=2, padx=1, pady=1)

    clear = Button(calc, height=2, width=4, padx=10, pady=10, text="C",bg="black",fg="white")
    clear["command"] = sum1.clear
    clear.grid(row=1, column=4, padx=1, pady=1)

    all_clear = Button(calc, height=2, width=4, padx=10, pady=10, text="AC",bg="black",fg="white")
    all_clear["command"] = sum1.all_clear
    all_clear.grid(row=1, column=5, padx=1, pady=1)

    equals = Button(calc, height=6, width=4, padx=10, pady=10, text="=",bg="blue",fg="white")
    equals["command"] = sum1.calc_total
    equals.grid(row=4, column=5, columnspan=1, rowspan=2, padx=1, pady=1)

    root.mainloop()
def browser():
    import webbrowser
    from tkinter import Tk, Button
    from tkinter.filedialog import askopenfilename
    from tkinter import Tk, Frame
    from tkinter import ttk
    # Setting structure of the browser window and variable declarations.
    wall.destroy()
    root = Tk()
    root.geometry("1600x900+-10+0")
    root.wm_title("CodeX web Browser ")
    root.iconbitmap('favicon.ico')
    url1 = 'http://www.gmail.com'
    url2 = 'http://www.yahoomail.com'
    url3 = 'http://www.youtube.com'
    url4 = 'http://www.facebook.com'
    url5 = 'http://www.github.com'
    url6 = 'http://www.linkedin.com'
    url7 = 'http://www.firefox.com'
    url8 = 'http://www.bing.com'
    url9 = 'http://www.google.com'

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    frame = Frame(root)
    frame.pack(side=BOTTOM)
    b1 = ttk.Button(frame, command=lambda aurl=url7: OpenUrl(aurl))
    b1.pack(side=LEFT)
    m1 = PhotoImage(file="firefox.png")
    b1.config(image=m1)
    tm1 = m1.subsample(3, 3)
    b1.config(image=tm1)
    b2 = ttk.Button(frame, command=lambda aurl=url8: OpenUrl(aurl))
    b2.pack(side=LEFT)
    m2 = PhotoImage(file="bing.png")
    b2.config(image=m2)
    tm2 = m2.subsample(6, 6)
    b2.config(image=tm2)
    b3 = ttk.Button(frame, command=lambda aurl=url9: OpenUrl(aurl))
    b3.pack(side=LEFT)
    m3 = PhotoImage(file="y.png")
    b3.config(image=m3)
    tm3 = m3.subsample(6, 6)
    b3.config(image=tm3)
    Label(root, text='Quick Links : ', font=("Helvetica", 16)).pack(side=BOTTOM)

    # This is used to open the apps specified in menu bar in our default browser.
    def OpenUrl(url):
        webbrowser.open_new(url)

    # This is used to open the color dialog box under Settings tab.
    def getColor():
        color = askcolor()

    # This  is used to open the downloads folder under downloads tab.
    def callback():
        name = askopenfilename()

        # The following functions are used to clear display area and URL field when back button is clicked.

    def clear_text():
        text.delete(1.0, 'end')

    def clear_entry():
        e1.delete(0, 'end')

    def sequence(*functions):
        def func(*args, **kwargs):
            return_value = None
            for function in functions:
                return_value = function(*args, **kwargs)
            return return_value

        return func

    """As soon as Go button is clicked, the data recieved from the server in form of html code is parsed and displayed
       in the text display area."""

    # go button
    def go():
        lbl.config(image='')
        url = e1.get()
        webbrowser.open_new(url)

    # menubar
    menu = Menu(root)
    root.config(menu=menu)
    subMenu = Menu(menu)
    menu.add_cascade(label="Apps", menu=subMenu)
    subMenu.add_command(label="Gmail", command=lambda aurl=url1: OpenUrl(aurl))
    subMenu.add_command(label="Y! Mail", command=lambda aurl=url2: OpenUrl(aurl))
    subMenu.add_command(label="Youtube", command=lambda aurl=url3: OpenUrl(aurl))
    subMenu.add_command(label="Facebook", command=lambda aurl=url4: OpenUrl(aurl))
    subMenu.add_command(label="Github", command=lambda aurl=url5: OpenUrl(aurl))
    subMenu.add_command(label="LinkedIn", command=lambda aurl=url6: OpenUrl(aurl))
    subMenu.add_separator()
    editMenu = Menu(menu)
    menu.add_cascade(label="Settings", menu=editMenu)
    editMenu.add_command(label="Themes and Colors", command=getColor)
    editMenu.add_command(label="History")
    editMenu.add_command(label="Connect account...")
    editMenu.add_command(label="Exit", command=root.quit)
    editMenu = Menu(menu)
    menu.add_cascade(label="Bookmarks", menu=editMenu)
    editMenu.add_command(label="View")
    editMenu.add_command(label="Add bookmark")
    editMenu = Menu(menu)
    menu.add_cascade(label="Tools", menu=editMenu)
    editMenu.add_command(label="Inspect Element")
    editMenu.add_command(label="Manage Extensions")
    editMenu.add_command(label="Developer Tools")
    editMenu = Menu(menu)
    menu.add_cascade(label="Downloads", menu=editMenu)
    editMenu.add_command(label="Open Downloads Folder", command=callback)
    # Buttons and field
    # declaration
    itiger = PhotoImage(file="cosmo.png")
    tiger = Label(root, image=itiger)
    back = Button(root, relief=SUNKEN, command=sequence(clear_entry, clear_text))
    iback = PhotoImage(file="back.png")
    back.config(image=iback)
    fwd = Button(root, relief=SUNKEN)
    ifwd = PhotoImage(file="fwd.png")
    fwd.config(image=ifwd)
    refresh = Button(root)
    irel = PhotoImage(file="refresh.png")
    refresh.config(image=irel)
    stop = Button(root)
    istop = PhotoImage(file="close.png")
    stop.config(image=istop)
    l1 = Label(root, text="URL:")
    e1 = Entry(root, font=("Helvetica", 12))
    go = Button(root, text="Go", command=go)
    text = Text(root, bd=4, yscrollcommand=scrollbar.set)
    scrollbar.config(command=text.yview)

    # placement of widgets
    tiger.place(x=10, y=10, height=80, width=100)
    back.place(x=120, y=30, height=30, width=40)
    fwd.place(x=170, y=30, height=30, width=40)
    refresh.place(x=220, y=30, height=30, width=30)
    l1.place(x=260, y=30, height=30, width=50)
    e1.place(x=300, y=30, height=30, width=900)
    stop.place(x=1200, y=30, height=30, width=30)
    go.place(x=1250, y=30, height=30, width=40)
    text.place(x=10, y=100, height=510, width=1320)
    im = PhotoImage(file="im.png")
    lbl = Label(text, image=im)
    lbl.pack()

    root.mainloop()
    homescreen()
def photoss():


    wall.destroy()
    if __name__ == "__main__":
        app = App();
        app.mainloop()
    homescreen()
applock()