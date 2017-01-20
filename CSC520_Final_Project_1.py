## ======== CSC520_Final_Project.py ==========
##
## Author: Aleksandr Nuzhnyi, Dorahan Arapgirlioglu, Ismayilov Teymur
## Date: 12/14/16
##
##  ==========================================


import tkinter as tk   # python3
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFileDialog
import re
import os # import os for os related functions
from PIL import Image, ImageTk
import tkinter
import tweepy
import facebook

TITLE_FONT = ("Helvetica", 50, "normal")
TITLE_FONT_TWTR = ("Helvetica", 18, "bold")

## This uses multiple sources that helped create it, the main body is based on the ITU Editor project.
## Source for creating multiple frames: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        s1 = Style()
        s1.configure('SelectFrame', background='#059FF5')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # the exit function
        def exit_editor(event=None):
            if tkMessageBox.askokcancel("quit", "Do you want to quit?"):
                tk.Tk.destroy(self)
            tk.Tk.protocol(self,'WM_DeLETE_WINDOW', exit_command)  # override close

        def popup(event):
            cmenu.tk_popup(event.x_root, event.y_root, 0)

        # menubar label and menu items
        menubar = tk.Menu(container)

        # a menu can be torn off, the first position (position 0) in the list of
        # choices is occupied by the tear-off element, and the additional choices
        # are added starting at the position 1. If you get set tearoff = 0,
        # the menu will not have a tear-off feature, and choices will be added
        # starting at position 0

        filemenu = tk.Menu(menubar, tearoff=1)
        filemenu.add_command(label="Exit", accelerator="Alt + F4", command=exit_editor)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=1)
        editmenu.add_command(label="Undo", accelerator="Command + Z")
        editmenu.add_command(label="Redo", accelerator="Command + Y")
        editmenu.add_separator()
        editmenu.add_command(label="Delete", accelerator="Del")
        editmenu.add_command(label="Clear", accelerator="Alt + Command + C")
        editmenu.add_separator()
        editmenu.add_command(label="Select All", accelerator="Command + a")
        editmenu.add_separator()
        menubar.add_cascade(label="Edit", menu=editmenu)
        showinbar = IntVar()

        aboutmenu = tk.Menu(menubar, tearoff=1)
        aboutmenu.add_command(label="Author", command=author_popup)
        menubar.add_cascade(label="About", menu=aboutmenu)

        ## _______________ End Menu Bar Definition _____________________________________________________

        # to use keyboard for executing the commands
        # self.bind("<Command-a>", select_all)
        # self.bind("<Command-A>", select_all)  # just in case caps lock is on

        tk.Tk.config(self, menu=menubar)

        ##END OF KEYS

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()





#Home page
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Pick Your \n Social Media", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Twitter",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Facebook",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()

        photo1 = tk.PhotoImage(file="Final/Assets/select_TWTR@2x.gif")
        lb = tk.Label(self, image=photo1,bg = "white")
        lb.bind('<Button-1>', lambda e: controller.show_frame("PageOne"))
        lb.image = photo1
        lb.pack()

        photo2 = tk.PhotoImage(file="Final/Assets/select_FB@2x.gif")
        lb2 = tk.Label(self, image=photo2, bg="white")
        lb2.bind('<Button-1>', lambda e: controller.show_frame("PageTwo"))
        lb2.image2 = photo2
        lb2.pack()

        lb.place(relx=0.4, rely=0.7, anchor=S)
        lb2.place(relx=0.6, rely=0.7, anchor=S)
        label.place(relx=0.5, rely=0.35, anchor=CENTER)
        button1.place(relx=0.4, rely=0.5, anchor=CENTER)
        button2.place(relx=0.6, rely=0.5, anchor=CENTER)

#Twitter page
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#059FF5')
        label = tk.Label(self, text="Twitter", font=TITLE_FONT_TWTR, fg="White", bg="#059FF5")
        label.pack(side="top", fill="x", pady=20)
        #label.place(relx=0.2, rely=0.03)
        button = tk.Button(self, text="Back", highlightbackground="#059FF5",
                           command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Post", highlightbackground="#059FF5",
                           command=lambda: post())

        button.place(relx=.1, rely=.06, anchor="c")
        button2.place(relx=.9, rely=.06, anchor="c")
        #button.pack()
        #button2.pack()

        # Tweepy API Reference: http://tweepy.readthedocs.io/en/v3.5.0/index.html
        # Check posts at "https://twitter.com/PythonTests"
        # Will keep access open until January
        def post():
            if len(textPad.get("1.0", "end-1c")) == 0:
                print("the widget is empty")
                empty = True
            else:
                print("the widget has text")
                empty = False

            if empty == False:
                post = textPad.get("1.0", END)
                print(post)
                tweet(post)
                Tweet_confirmation()
            elif empty == True:
                No_text()

        def tweet(param):
            ##Twitter data
            ##For account @PythonTests - Python Project
            key = "..."
            secret = "..."
            token = "..."
            token_secret = "..."

            auth = tweepy.OAuthHandler(key, secret)
            auth.set_access_token(token, token_secret)
            client = tweepy.API(auth)
            client.update_status(param)

        # author function
        def Tweet_confirmation():
            if tkMessageBox.showinfo("Posted",
                                     "Tweeted successfully!"):
                pass

         # author function
        def No_text():
            if tkMessageBox.showinfo("No Text",
                                    "Can't tweet nothing, please write something."):
                pass


        ### Trial to bring in designed interface elements as images.
        ### Couldn't figure out how to dynamically update an image following an event.

        #image = Image.open("Final/Assets/Twitter_BACK.png")
        #photo1 = ImageTk.PhotoImage(image)

        #photo1 = tk.PhotoImage(file="Final/Assets/Twitter_BACK.gif")
        #lb = tk.Label(self, text = "Search", bg = "#fecc14", fg = "Black", activebackground = "Red", highlightbackground="Black")
        # lb = tk.Label(self, image=photo1,bg = "#059FF5")
        # lb.bind('<Button-1>', lambda e: event_event)
        # lb.image = photo1
        # lb.pack()

        label1 = tk.Label(self, bg="#059FF5", height=1, width=1200)
        label1.pack(side=TOP, expand=NO, fill=X)

        label2 = tk.Label(self, bg="#059FF5", height=800, width=2)
        label2.pack(side=LEFT, expand=NO, fill=Y)

        label4 = tk.Label(self, bg="#059FF5", height=800, width=2)
        label4.pack(side=RIGHT, expand=NO, fill=Y)

        # the area where we will enter text
        textPad = tk.Text(self, undo=TRUE, bg="#FFFFFF", padx=10, pady=10)
        textPad.pack(expand=YES, fill=BOTH)

        textPad.file_opt = options = {}

        label3 = tk.Label(self, bg="#059FF5", height=1, width=800)
        label3.pack(side=BOTTOM, expand=NO, fill=X)


        # Select all the text in textbox
        def select_all(event):
            textPad.tag_add(SEL, "1.0", END)
            textPad.mark_set(INSERT, "1.0")
            textPad.see(INSERT)
            return 'break'

        textPad.bind("<Command-a>", select_all)
        textPad.bind("<Command-A>", select_all)  # just in case caps lock is on




#Facebook page
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#39579A')
        label = tk.Label(self, text="Facebook", font=TITLE_FONT_TWTR, fg="White", bg="#39579A")
        label.pack(side="top", fill="x", pady=20)
        button = tk.Button(self, text="Back", highlightbackground="#39579A",
                           command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Post", highlightbackground="#39579A",
                            command=lambda: post())
        #button.pack()
        #button2.pack()
        button.place(relx=.1, rely=.06, anchor="c")
        button2.place(relx=.9, rely=.06, anchor="c")

        def test(param):
            print(param)

        label1 = tk.Label(self, bg="#39579A", height=1, width=1200)
        label1.pack(side=TOP, expand=NO, fill=X)

        label2 = tk.Label(self, bg="#39579A", height=800, width=2)
        label2.pack(side=LEFT, expand=NO, fill=Y)

        label4 = tk.Label(self, bg="#39579A", height=800, width=2)
        label4.pack(side=RIGHT, expand=NO, fill=Y)

        # the area where we will enter text
        textPad = tk.Text(self, undo=TRUE, bg="#FFFFFF", padx=10, pady=10)
        textPad.pack(expand=YES, fill=BOTH)

        textPad.file_opt = options = {}

        label3 = tk.Label(self, bg="#39579A", height=1, width=800)
        label3.pack(side=BOTTOM, expand=NO, fill=X)

        # Select all the text in textbox
        # Repetition of PageOne select_all function, because couldn't figure out how to access it from another class.
        def select_all(event):
            textPad.tag_add(SEL, "1.0", END)
            textPad.mark_set(INSERT, "1.0")
            textPad.see(INSERT)
            return 'break'

        textPad.bind("<Command-a>", select_all)
        textPad.bind("<Command-A>", select_all)  # just in case caps lock is on

        def post():

            # The values are not filled in because Facebook blocked the test account
            # created for this project, requiring a government issued photo ID.
            cfg = {
                "page_id": "###",  # Step 1
                "access_token": "###"  # Step 3
            }

            # Tutorial to post on Facebook: http://nodotcom.org/python-facebook-tutorial.html
            # Facebook API Reference: http://facebook-sdk.readthedocs.io/en/latest/api.html
            # How to receive the access tokens: https://developers.facebook.com/docs/facebook-login/access-tokens
            def get_api(cfg):
                graph = facebook.GraphAPI(cfg['access_token'])
                # Get page token to post as the page. You can skip
                # the following if you want to post as yourself.
                # resp = graph.get_object('me/accounts')
                # page_access_token = None
                # for page in resp['data']:
                #    if page['id'] == cfg['page_id']:
                #        page_access_token = page['access_token']
                # graph = facebook.GraphAPI(page_access_token)
                return graph
                # You can also skip the above if you get a page token:
                # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
                # and make that long-lived token as in Step 3

            # if __name__ == "__main__":
            #     main()

            if len(textPad.get("1.0", "end-1c")) == 0:
                print("the widget is empty")
                empty = True
            else:
                print("the widget has text")
                empty = False

            if empty == False:
                # If there is text in textpad, post it to Facebook wall.
                msg = textPad.get("1.0", END)
                api = get_api(cfg)
                status = api.put_wall_post(msg)
                print(msg)

            elif empty == True:
                No_text()

        # author function
        def No_text():
            if tkMessageBox.showinfo("No Text",
                                     "Can't post nothing, please write something."):
                pass



# author function
def author_popup():
    if tkMessageBox.showinfo("Information", "Authors for this project: \n \n Aleksandr Nuzhnyi, Dorahan Arapgirlioglu, Ismayilov Teymur"):
        pass


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("600x600")
    app.title("Social Media Controller")
    app.mainloop()