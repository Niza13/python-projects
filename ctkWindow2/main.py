# window 2 trial

from tkinter import *
import tkinter as tk
import customtkinter as ctk
from PIL import Image       #library pillow for images 
# import rsa                  #for encryption
from cryptography.fernet import Fernet  #for encryption
import tkinter.filedialog as fd     #to browse location of files
import os   #for system (browse path and creating folders and files)
import subprocess       #for output of command
import zipfile   #to zip the result folder/file

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("dark-blue")


# main window
root = ctk.CTk()

w=root.winfo_width()
h=root.winfo_height()



w=900 
h=600
# w=1100 
# h=800
# w=1200 
# h=900
resol = f"{w}x{h}"

root.title("ctk Tool Layout")
root.geometry(f"{w}x{h}")
root.minsize(900,600)       #w=1208, h=720
root.resizable(True,True)


# root layout settings
root.grid_columnconfigure((1,3), weight=1, uniform='group')
# root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=3)
root.grid_rowconfigure(1, weight=1)

# ............................................................

# scaleFunc
def scaleFunc(num):
    # removing% and converting to int
    scaleFactor = int(num.replace("%",""))/100
    ctk.set_widget_scaling(scaleFactor)
    # print(num)


# def windowControl(event):
#     h=root.winfo_height()       #gets height dynamically
#     w=root.winfo_width()        #gets width dynamically
#     print("width: ",w, "height: ",h)

    


# binding configure event to window and specifying callback func
# root.bind("<Configure>", windowControl)     #when configure event occurs windowcontrol func is called


# resize scaling
if(resol=="500x200"):
    scaleFunc("50%")
elif(resol=="700x400"):
    scaleFunc("50%")
elif(resol=="900x600"):
    scaleFunc("70%")
elif(resol=="1100x800"):
    scaleFunc("90%")
elif(resol=="1200x900"):
    scaleFunc("100%")
    


# navbar........................................................
navbar = ctk.CTkFrame(root,
                      fg_color="grey10",
                      height=130)
navbar.grid(row=0, column=0, columnspan=4, padx=0, pady=0, sticky="ew")

# nav config
navbar.grid_columnconfigure((1,2,3), weight=1, uniform="uniform")
# navbar.grid_columnconfigure(2, weight=1)
# navbar.grid_columnconfigure(4, weight=1)

logo = ctk.CTkLabel(navbar,
                      text="CTK Tool Layout",
                      font=ctk.CTkFont(family="Oswald",weight="normal", size=25),
                      text_color="white")
logo.grid(row=0, column=0, columnspan=2, padx=(20,50), pady=10, sticky="w")



# searhbar.................................................................
searchbar = ctk.CTkEntry(navbar,
                         placeholder_text="Search functions...",
                         placeholder_text_color="azure3",
                         text_color="azure3",
                         fg_color="grey20",
                         width=300,
                         height=40,
                         font=ctk.CTkFont(weight="normal", size=12),
                         corner_radius=0,
                         border_width=0)
searchbar.grid(row=0, column=2, padx=(10,10), pady=10, sticky="ew")



# iconBtnFunc
def iconBtnFunc():
    print("icons pressed")


# search icon
searchIcon = PhotoImage(file=r"ctkWindow2Icons\\search.png")


# searchBtn
searchBtn=ctk.CTkButton(navbar,
                        fg_color="grey20",
                        image = searchIcon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=10,
                        command=iconBtnFunc)
searchBtn.grid(row=0, column=2, padx=(0,0), pady=(10,10), sticky="sne")


# ..............................................
# scalling
# scaleFunc
def scaleFunc(num):
    # removing% and converting to int
    scaleFactor = int(num.replace("%",""))/100
    ctk.set_widget_scaling(scaleFactor)
    print(num)

# Resize label
resize = ctk.CTkLabel(navbar,
                         text="Resize:",
                         font=ctk.CTkFont(size=14),
                         text_color="white").grid(row=0, column=3, padx=(10,260), pady=(15,10), sticky="ne")

# scalingmenu
scalingOption = ctk.CTkOptionMenu(navbar,
                                  height=30,
                                  width=70,
                                  text_color="azure3",
                                  fg_color='grey20',
                                  button_color='grey20',
                                  button_hover_color='grey20',
                                  dropdown_hover_color="grey25",
                                  dropdown_fg_color="grey20",
                                  dropdown_text_color="azure3",
                               anchor="w",
                               values=["70%","80%","90%","100%","110%","120%"],
                               command=scaleFunc)
scalingOption
scalingOption.grid(row=0,column=3, padx=(10,180), pady=(15,10), sticky="ne")

# default scalling
scalingOption.set("70%")
# .......................................


# edit icon............................................................
editIcon = PhotoImage(file=r"ctkWindow2Icons\\edit.png")
# editBtn
editBtn=ctk.CTkButton(navbar,
                        fg_color="grey10",
                        image = editIcon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=40,
                        command=iconBtnFunc)
editBtn.grid(row=0, column=3, padx=(10,130), pady=(15,10), sticky="ne")

# bell icon........................................................
bellicon = PhotoImage(file=r"ctkWindow2Icons\\bell.png")
# bellBtn
bellBtn=ctk.CTkButton(navbar,
                        fg_color="grey10",
                        image = bellicon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=40,
                        command=iconBtnFunc)
bellBtn.grid(row=0, column=3, padx=(40,80), pady=(15,10), sticky="ne")


# user icon..........................................................
userIcon = PhotoImage(file=r"ctkWindow2Icons\user.png")
# userBtn
userBtn=ctk.CTkButton(navbar,
                        fg_color="grey10",
                        image = userIcon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=40,
                        command=iconBtnFunc)
userBtn.grid(row=0, column=3, padx=(70,30), pady=(15,10), sticky="ne")


# ............................................................................
# sidebar
# ...........................................................................

# list icon
listicon = PhotoImage(file=r"ctkWindow2Icons\\list.png")
# listBtn
listBtn=ctk.CTkButton(root,
                        fg_color="transparent",
                        image = listicon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=50,
                        height=50,
                        command=iconBtnFunc)
listBtn.grid(row=1, rowspan=8, column=0, padx=(10,0), pady=(30,40), sticky="new")


# home icon
homeIcon = PhotoImage(file=r"ctkWindow2Icons\\home.png")
# homeBtn
homeBtn=ctk.CTkButton(root,
                        fg_color="transparent",
                        image = homeIcon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=50,
                        height=50,
                        command=iconBtnFunc)
homeBtn.grid(row=1, column=0, padx=(10,0), pady=(80,30), sticky="new")


# cloud icon
cloudIcon = PhotoImage(file=r"ctkWindow2Icons\\cloud.png")
# cloudBtn
cloudBtn=ctk.CTkButton(root,
                        fg_color="transparent",
                        image = cloudIcon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=50,
                        height=50,
                        command=iconBtnFunc)
cloudBtn.grid(row=1, column=0, padx=(10,0), pady=(130,30), sticky="new")


# db icon
dbIcon = PhotoImage(file=r"ctkWindow2Icons\\database.png")
# cloudBtn
dbBtn=ctk.CTkButton(root,
                        fg_color="transparent",
                        image = dbIcon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=50,
                        height=50,
                        command=iconBtnFunc)
dbBtn.grid(row=1, column=0, padx=(10,0), pady=(180,30), sticky="new")


# bracesIcon
bracesIcon = PhotoImage(file=r"ctkWindow2Icons\\code.png")
# cloudBtn
bracesBtn=ctk.CTkButton(root,
                        fg_color="transparent",
                        image = bracesIcon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=50,
                        height=50,
                        command=iconBtnFunc)
bracesBtn.grid(row=1, column=0, padx=(10,0), pady=(230,30), sticky="new")


# usersIcon
usersIcon = PhotoImage(file=r"ctkWindow2Icons\\group.png")
# usersBtn
usersBtn=ctk.CTkButton(root,
                        fg_color="transparent",
                        image = usersIcon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=50,
                        height=50,
                        command=iconBtnFunc)
usersBtn.grid(row=1, column=0, padx=(10,0), pady=(280,30), sticky="new")


# refreshIcon
refreshIcon = PhotoImage(file=r"ctkWindow2Icons\\refresh.png")
# refreshBtn
refreshBtn=ctk.CTkButton(root,
                        fg_color="transparent",
                        image = refreshIcon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=50,
                        height=50,
                        command=iconBtnFunc)
refreshBtn.grid(row=1, column=0, padx=(10,0), pady=(330,30), sticky="new")


# plusIcon
plusIcon = PhotoImage(file=r"ctkWindow2Icons\\plus.png")
# plusBtn
plusBtn=ctk.CTkButton(root,
                        fg_color="transparent",
                        image = plusIcon,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=50,
                        height=50,
                        command=iconBtnFunc)
plusBtn.grid(row=1, column=0, padx=(10,0), pady=(380,30), sticky="new")


# ..........................................................................
# column 1
# ..........................................................................

# column frame

colFrame1 = ctk.CTkScrollableFrame(root,
                          fg_color="grey92",
                          scrollbar_button_color="grey92",
                          scrollbar_fg_color="transparent",
                          scrollbar_button_hover_color="grey94")
colFrame1.grid(row=1, column=1, padx=10, pady=(20,20), sticky="snew")



# frame label
colLabel1 = ctk.CTkLabel(colFrame1,
                         text="Destination",
                         font=ctk.CTkFont(size=28),
                         text_color="black").grid(row=0, column=0, padx=20, pady=10, sticky="snw")

col1_text1 = ctk.CTkLabel(colFrame1,
                         text="Lorem ipsum dolor sit amet, consecteur adipicsing.",
                         justify="left",
                         font=ctk.CTkFont(size=12),
                         text_color="grey20").grid(row=0, column=0, padx=(20,20), pady=(80,10), sticky="new")


# radio btn func...............................................................

# by default source and destination
source = None
destination = None

# function to browse location, takes place:source/destination and root window
def browse(place):

    currdir = os.getcwd()
    tempdir = fd.askdirectory(parent=root, initialdir=currdir,title=f'Select {place}')

    if len(tempdir) > 0:
        print (tempdir)

    if(place=='source'):
        pathEntry1.insert(0,tempdir)
        source = tempdir
    else:
        pathEntry2.insert(0,tempdir)
        destination = tempdir
        
    # print('source',source, 'destination',destination)


# getting confirmed loc
def confirm():

    source = pathEntry1.get()
    destination = pathEntry2.get()

    if(source=="" and  destination==""):
        print("enter location")
        
    print(source,destination)

# to clear loc feilds
def clear():
    pathEntry1.delete("0","end")
    pathEntry2.delete("0","end")

pathEntry1 = ctk.CTkEntry(colFrame1,
                                 text_color="grey40",
                                 placeholder_text="enter source path",
                                 font=ctk.CTkFont(size=12),
                                #  width=300,
                                 corner_radius=0,
                                 height=25)

pathEntry2 = ctk.CTkEntry(colFrame1,
                                 text_color="grey40",
                                 placeholder_text="enter destination path:",
                                 font=ctk.CTkFont(size=12),
                                #  width=300,
                                 corner_radius=0,
                                 height=25)

def rbFunc():
    ans = rbVar.get()

    if ans==1:
        
        # placing entry1
        pathEntry1.grid(row=1, column=0, padx=50, pady=(30,8), sticky="ew")

        # placing btn1
        sourceBtn1 = ctk.CTkButton(colFrame1,
                                   text="Browse",
                                   command=browse('source'),
                                   width=50,
                                   fg_color="green",
                                   hover_color='green')
        # sourceBtn1.grid(row=1, column=0, padx=(50,10), pady=(30,8), sticky="e")
            
        # placing entry2
        pathEntry2.grid(row=1, column=0, padx=50, pady=(100,8), sticky="ew")

        # placing btn1
        sourceBtn2 = ctk.CTkButton(colFrame1,
                                   text="Browse",
                                   command=browse('destination'),
                                   width=50,
                                   fg_color="green",
                                   hover_color='green')
        # sourceBtn2.grid(row=1, column=0, padx=(50,10), pady=(100,8), sticky="e")

        confirmBtn = ctk.CTkButton(colFrame1,
                                   text="Confirm",
                                   command=confirm,
                                   width=50,
                                   fg_color="green4",
                                   hover_color='green')
        confirmBtn.grid(row=1, column=0, padx=(50,0), pady=(170,8), sticky="w")
        
        clearBtn = ctk.CTkButton(colFrame1,
                                   text="Clear",
                                   command=clear,
                                   width=50,
                                   fg_color="green4",
                                   hover_color='green')
        clearBtn.grid(row=1, column=0, padx=(140,0), pady=(170,8), sticky="w")
        
        # print(rbVar.get())
    else:
        print(rbVar.get())


# radio btn variable
rbVar = ctk.IntVar()

# radio btns
locFile = ctk.CTkRadioButton(colFrame1,
                               value=1,
                               variable=rbVar,
                               command=rbFunc,
                               font=ctk.CTkFont(size=13),
                               text="Local Files",
                               hover_color="green4",
                               fg_color="green4",
                               text_color='grey10',
                               height=10,
                               border_width_checked=3)
locFile.grid(row=1, rowspan=2, column=0, padx=20, pady=(10,80), sticky="ew")


s3Bucket = ctk.CTkRadioButton(colFrame1,
                               value=2,
                               variable=rbVar,
                               command=rbFunc,
                               text="S3 Bucket",
                               hover_color="green",
                               fg_color="green",
                               font=ctk.CTkFont(size=13),
                               text_color='grey10',
                               height=10,
                               border_width_checked=3)
s3Bucket.grid(row=2, column=0, padx=20, pady=(5,5), sticky="ew")


remoteServer = ctk.CTkRadioButton(colFrame1,
                               value=3,
                               variable=rbVar,
                               command=rbFunc,
                               hover_color="green",
                               fg_color="green",
                               font=ctk.CTkFont(size=13),
                               text="On Remote Server",
                               text_color='grey10',
                               height=40,
                               border_width_checked=3)
remoteServer.grid(row=3, column=0, padx=20, pady=(5,5), sticky="ew")


# sublabel 1 (Encryption).................................................................
col1_SubLabel1 = ctk.CTkLabel(colFrame1,
                         text="Encryption",
                         font=ctk.CTkFont(size=24),
                         text_color="grey30").grid(row=4, column=0, columnspan=1, padx=20, pady=(30,5), sticky="snw")


# swicth func
def switchFunc():
    # print(switchVar.get())
    val = switchVar.get()


    # save and cancel btn's...........................................
    # cancel btn func
    def cancelbtn():
        # clears feilds
        passwd.delete(0,"end")
        repeatPasswd.delete(0,"end")
        
    def savebtn():
        print("button pressed")
        
        val1 = passwd.get()
        val2 = repeatPasswd.get()
        if(val1==val2):
            # print("matched")

            # encrypting password and storing in passwd.txt file

            # extracting public key and encrypting message
            with open("publicK.pem","rb") as f:
                public_K = rsa.PublicKey.load_pkcs1(f.read())
                # print(public_K)

            encryptmsg = rsa.encrypt(val1.encode(),public_K)

            # storing encrypted text in file
            with open("passwd.txt","wb") as f2:
                f2.write(encryptmsg)
            

        else:
            print("passwords did not match!")

        


    if(val==1):

        # entry..............................................................
        passwd = ctk.CTkEntry(colFrame1,
                              show="*",
                              text_color="grey40",
                              placeholder_text="Password",
                              font=ctk.CTkFont(size=11),
                              height=50,
                            #   width=300,
                              border_color="grey80",
                              corner_radius=10,
                              border_width=1)
        passwd.grid(row=5, column=0, padx=(20,10), pady=(10,0), sticky="ew")


        repeatPasswd = ctk.CTkEntry(colFrame1,
                                    
                              show="*",
                              text_color="grey40",
                              placeholder_text="Repeat Password",
                              height=50,
                            #   width=300,
                              border_color="grey80",
                              corner_radius=10,
                              font=ctk.CTkFont(size=13),
                              border_width=1)
        repeatPasswd.grid(row=6, column=0, padx=(20,10), pady=(10,0), sticky="ew")

        saveBtn = ctk.CTkButton(colFrame1,
                                text="Save",
                                fg_color="blue2",
                                corner_radius=0,
                                font=ctk.CTkFont(weight="bold", family="Raleway"),
                                hover_color="blue3",
                                height=40,
                                width=130,
                                command=savebtn)
        saveBtn.grid(row=8, rowspan=2, column=0, padx=(20,160), pady=(20,10), sticky="nw")


        cancelBtn = ctk.CTkButton(colFrame1,
                                text="Cancel",
                                fg_color="transparent",
                                text_color="blue2",
                                hover_color="grey94",
                                corner_radius=0,
                                border_width=1,
                                border_color="blue2",
                                font=ctk.CTkFont(family="Raleway"),
                                width=130,
                                height=40,
                                command=cancelbtn)
        cancelBtn.grid(row=8, column=0, padx=(20,10), pady=(20,10), sticky="ne")

    


# variable for switch
switchVar = ctk.IntVar()

switchEncrypt = ctk.CTkSwitch(colFrame1,
                              text=None,
                              command=switchFunc,
                              variable=switchVar,
                              onvalue=1,
                              offvalue=0,
                              button_color="white",
                              fg_color="grey50",
                              button_hover_color="blue3",
                            #   progress_color="green",
                              height=10)

switchEncrypt.grid(row=4, column=0, padx=(10,60), pady=(35,5), sticky="nse")





# sublabel 2 (Danger Zone)............................................................
col1_SubLabel1 = ctk.CTkLabel(colFrame1,
                         text="Danger Zone",
                         font=ctk.CTkFont(size=24),
                         text_color="grey30").grid(row=9, column=0, padx=(18,10), pady=30, sticky="snw")



def btnFunc1():
        print("button pressed")
        
# close btn
closeBtn = ctk.CTkButton(colFrame1,
                        text="Close",
                        fg_color="firebrick3",
                        hover_color="red3",
                        corner_radius=0,
                        font=ctk.CTkFont(weight="bold"),
                        height=40,
                        width=140,
                        command=btnFunc1)
closeBtn.grid(row=9, column=0, padx=(170,10), pady=30, sticky="sne")



# ..........................................................................
# column 2
# ..........................................................................

# column frame 2

colFrame2 = ctk.CTkScrollableFrame(root,
                          fg_color="grey92",
                          scrollbar_button_color="grey92",
                          scrollbar_fg_color="transparent",
                          scrollbar_button_hover_color='4')
colFrame2.grid(row=1, column=2, padx=10, pady=(20,20), sticky="snew")

# configuration for checkboxes roe
colFrame2.rowconfigure(2, weight=1)


# frame label......................................................
colLabel2 = ctk.CTkLabel(colFrame2,
                         text="Collection Type",
                         font=ctk.CTkFont(size=28),
                         text_color="black").grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="snw")


col1_text1 = ctk.CTkLabel(colFrame2,
                         text="Lorem ipsum dolor sit amet, consecteur adipicsing.",
                         justify="left",
                         font=ctk.CTkFont(size=12),
                         text_color="grey20").grid(row=0, column=0, padx=(20,10), pady=(80,10), sticky="nw")


# sublabels
col2_SubLabel1 = ctk.CTkLabel(colFrame2,
                         text="User",
                         font=ctk.CTkFont(size=24),
                         text_color="grey30").grid(row=1, column=0, padx=(20,0), pady=30, sticky="snw")


col2_SubLabel2 = ctk.CTkLabel(colFrame2,
                         text="Malware",
                         font=ctk.CTkFont(size=24),
                         text_color="grey30").grid(row=1, column=0, padx=(30,200), pady=30, sticky="sne")


# column2 checkbox func.................................
def checkboxFunc():
    
    vals = checkVar.get()

    if(vals!='zero' and vals not in checkValArr):
        checkValArr.append(vals)
        print(checkValArr)



# variable to store and get checked items
checkVar = ctk.StringVar()


# array to add checked items
checkValArr = []

# checkboxes
logins = ctk.CTkLabel(colFrame2,
                         text="Logins",
                         font=ctk.CTkFont(size=15),
                         
                         text_color="grey20").grid(row=2, rowspan=5, column=0, columnspan=2, padx=(20,10), pady=10, sticky="nw")

cb1 = ctk.CTkCheckBox(colFrame2,
                           text=None,
                           border_width=2,
                           corner_radius=2,
                           checkbox_height=20,
                           checkbox_width=20,
                           command=checkboxFunc,
                           variable=checkVar,
                           hover_color="green4",
                           fg_color="green4",
                           onvalue="logins",
                           offvalue='zero')
cb1.grid(row=2, column=0, padx=(200,10), pady=10, sticky="nw")

# .....................................................................

startupItems = ctk.CTkLabel(colFrame2,
                         text="startupItems",
                         font=ctk.CTkFont(size=15),
                         
                         text_color="grey20").grid(row=2, column=0, padx=(250,10), pady=10, sticky="nw")

cb2 = ctk.CTkCheckBox(colFrame2,
                           text=None,
                           border_width=2,
                           corner_radius=2,
                           checkbox_height=20,
                           checkbox_width=20,
                           command=checkboxFunc,
                           variable=checkVar,
                           hover_color="green4",
                           fg_color="green4",
                           onvalue="startup_items",
                           offvalue='zero')
cb2.grid(row=2, column=0, padx=(420,10), pady=10, sticky="nw")

# .....................................................................

networkShares = ctk.CTkLabel(colFrame2,
                         text="Network Shares",
                         font=ctk.CTkFont(size=15),
                         
                         text_color="grey20").grid(row=2, column=0, padx=(20,10), pady=(45,10), sticky="nw")

cb3 = ctk.CTkCheckBox(colFrame2,
                           text=None,
                           border_width=2,
                           corner_radius=2,
                           checkbox_height=20,
                           checkbox_width=20,
                           command=checkboxFunc,
                           variable=checkVar,
                           hover_color="green4",
                           fg_color="green4",
                           onvalue="network_shares",
                           offvalue='zero')
cb3.grid(row=2, column=0, padx=(200,10), pady=(45,10), sticky="nw")

# .....................................................................

processes = ctk.CTkLabel(colFrame2,
                         text="Processes",
                         font=ctk.CTkFont(size=15),
                         
                         text_color="grey20").grid(row=2, column=0, padx=(250,10), pady=(45,10), sticky="nw")

cb4 = ctk.CTkCheckBox(colFrame2,
                           text=None,
                           border_width=2,
                           corner_radius=2,
                           checkbox_height=20,
                           checkbox_width=20,
                           command=checkboxFunc,
                           variable=checkVar,
                           hover_color="green4",
                           fg_color="green4",
                           onvalue="processes_running",
                           offvalue='zero')
cb4.grid(row=2, column=0, padx=(420,10), pady=(45,10), sticky="nw")



# .....................................................................

programsRun = ctk.CTkLabel(colFrame2,
                         text="Programs Run",
                         font=ctk.CTkFont(size=15),
                         
                         text_color="grey20").grid(row=2, column=0, padx=(20,10), pady=(80,10), sticky="nw")

cb5 = ctk.CTkCheckBox(colFrame2,
                           text=None,
                           border_width=2,
                           corner_radius=2,
                           checkbox_height=20,
                           checkbox_width=20,
                           command=checkboxFunc,
                           variable=checkVar,
                           hover_color="green4",
                           fg_color="green4",
                           onvalue="programs_run",
                           offvalue='zero')
cb5.grid(row=2, column=0, padx=(200,10), pady=(80,10), sticky="nw")

# .....................................................................

network = ctk.CTkLabel(colFrame2,
                         text="Network",
                         font=ctk.CTkFont(size=15),
                         
                         text_color="grey20").grid(row=2, column=0, padx=(250,10), pady=(80,10), sticky="nw")

cb6 = ctk.CTkCheckBox(colFrame2,
                           text=None,
                           border_width=2,
                           corner_radius=2,
                           checkbox_height=20,
                           checkbox_width=20,
                           command=checkboxFunc,
                           variable=checkVar,
                           hover_color="green4",
                           fg_color="green4",
                           onvalue="network",
                           offvalue='zero')
cb6.grid(row=2, column=0, padx=(420,10), pady=(80,10), sticky="nw")


# .....................................................................

webArtifacts1 = ctk.CTkLabel(colFrame2,
                         text="Web Artifacts Run",
                         font=ctk.CTkFont(size=15),
                         
                         text_color="grey20").grid(row=2, column=0, padx=(20,10), pady=(115,10), sticky="nw")

cb7 = ctk.CTkCheckBox(colFrame2,
                           text=None,
                           border_width=2,
                           corner_radius=2,
                           checkbox_height=20,
                           checkbox_width=20,
                           command=checkboxFunc,
                           variable=checkVar,
                           hover_color="green4",
                           fg_color="green4",
                           onvalue="webArtifacts1_run",
                           offvalue='zero')
cb7.grid(row=2, column=0, padx=(200,10), pady=(115,10), sticky="nw")

# .....................................................................

webArtifacts2 = ctk.CTkLabel(colFrame2,
                         text="Web Artifacts",
                         font=ctk.CTkFont(size=15),
                         
                         text_color="grey20").grid(row=2, column=0, padx=(250,10), pady=(115,10), sticky="nw")

cb8 = ctk.CTkCheckBox(colFrame2,
                           text=None,
                           border_width=2,
                           corner_radius=2,
                           checkbox_height=20,
                           checkbox_width=20,
                           command=checkboxFunc,
                           variable=checkVar,
                           hover_color="green4",
                           fg_color="green4",
                           onvalue="webArtifacts2",
                           offvalue='zero')
cb8.grid(row=2, column=0, padx=(420,10), pady=(115,10), sticky="nw")


# .....................................................................

dataAccessed = ctk.CTkLabel(colFrame2,
                         text="Data Accessed",
                         font=ctk.CTkFont(size=15),
                         
                         text_color="grey20").grid(row=2, column=0, padx=(20,10), pady=(150,10), sticky="nw")

cb9 = ctk.CTkCheckBox(colFrame2,
                           text=None,
                           border_width=2,
                           corner_radius=2,
                           checkbox_height=20,
                           checkbox_width=20,
                           command=checkboxFunc,
                           variable=checkVar,
                           hover_color="green4",
                           fg_color="green4",
                           onvalue="data_accessed",
                           offvalue='zero')
cb9.grid(row=2, column=0, padx=(200,10), pady=(150,10), sticky="nw")


# ..........................................................................
# function to create directories and files
def createFile(command,checkboxName,fname):

    destination = pathEntry2.get()

    try:
        # txt = os.system('cmd /c "wmic startup list full"')
        ansCode = subprocess.check_output(command,shell=True)
        ans=ansCode.decode('utf-8')

    except:
        print(f'error while running {checkboxName}')

    # creating a file to store encrypted output
    with open ((fr'{destination}\results\{checkboxName}\{fname}'),'w') as f:
        f.write(ans)

    return ans


# ..........................................................................
# function to encrypt data from command prompt
def runEncrypt(data,filename):

    key = Fernet.generate_key()
    f = Fernet(key)

    data = bytes(data, encoding='utf-8')

    ans = f.encrypt(data)

    ans
    b'...'

    # storing encrypted text in file
    with open(filename,"wb") as f1:
        f1.write(ans)
        print(ans)

    print(f'{filename} data is encrypted successfully')


# ..........................................................................

# zipping file
def zipping(folder_to_zip_path, output_zip_file_path):
    print(folder_to_zip_path,'\n',output_zip_file_path)


    try:
        # creating main zip folder
        with zipfile.ZipFile('results.zip', 'w') as zip_object:


            try:
                
                print('entering subfolders')
                # creating zip subfolders
                with zipfile.ZipFile(output_zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for root, _, files in os.walk(folder_to_zip_path):

                        try:

                            print('entering files')

                            # adding files to it
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, folder_to_zip_path)
                                zipf.write(file_path, arcname=arcname)

                        except:
                            print('files transfer failed')
            except:
                print('subfolders failed')
    except:
        print('zipping failed')



# ..................................................
# save all and deselect all btn's
def selectAll():
    
    # getting values of checked boxes
    for i in checkValArr:
        print(i)

    # creating directory at destination
    try:
        destination = pathEntry2.get()
        os.makedirs(os.path.join(destination,'results'))
    except:
        print('directory already exixts')

    # creating folders for each checkbox in result folder
    for i in checkValArr:
        try:
            
            path = destination+'/results/'

            # making directories of selected checkboxes
            os.makedirs(os.path.join(path,i))
        except:
            print('directory already exixts')

    # run commands and creating files respectively
    for i in checkValArr:
        if(i=='startup_items'):

            # creating file with passing command, folder name and filename to get output
            data = createFile("wmic startup list full",'startup_items','startup_items_list.txt')

            # runEncrypt(data,'startup_items_list.txt')

        if(i=='processes_running'):
            # creating file with passing command, folder name and filename to get output
            data = createFile("wmic process list",'processes_running','wmic_process_list.txt')

            # runEncrypt(data,'wmic_process_list.txt')

        if(i=='network'):
            # creating file with passing command, folder name and filename to get output
            cmd = {'ipconfig /all':'ipconfig_all.txt',
                   'ipconfig /displaydns': 'ipconfig _displaydns.txt',
                   'route print':'route_print.txt',
                   'net view':'net_view.txt',
                   'netstat -nao':'netstat_nao.txt',
                   'netstat -vb':'netstat_vb.txt',
                   'netstat -ns':'netstat_ns.txt',
                   'net accounts':'net_accounts.txt',
                   'net accounts/domain': 'net_accounts_domain.txt',
                   'net session':'net_session.txt',
                   'net share':'net_share.txt',
                   'net group':'net_group.txt',
                   'net user':'net_user.txt',
                   'net localgroup':'net_localgroup.txt',
                   'net localgroup administrators':'net_localgroup_administrators.txt',
                   'net group administrators':'net_group_administrators.txt',
                   'net view/domain':'net_view_domain.txt',
                   'net firewall show config':'net_firewall_show_config.txt',
                   'net wlan show network':'net_wlan_show_network.txt'}
            
            # for i in cmd:
            #     print(i,cmd[i])
            for i in cmd:

                try:

                    # creating file and storing data for each elem in cmd
                    data = createFile(i,'network',cmd[i])
                    print(f'{i} completed successfully')

                except:
                    print(f'{i} unsuccessful')


    # print(path,'and',destination)
    # Call the function to zip the folder and its files
    # print('results destination...'+destination+'/results')
    zipping(os.path.join(destination,'/results'), os.path.join(destination,'/results.zip'))




# btn to deselect all checkboxes
def deselectAll():
    cb1.deselect()
    cb2.deselect()
    cb3.deselect()
    cb4.deselect()
    cb5.deselect()
    cb6.deselect()
    cb7.deselect()
    cb8.deselect()
    cb9.deselect()
    checkValArr.clear()

selectAllBtn = ctk.CTkButton(colFrame2,
                        fg_color="transparent",
                        text="Select All",
                        text_color="blue2",
                        border_color="blue2",
                        hover_color="grey94",
                        corner_radius=0,
                        border_width=1,
                        height=50,
                        width=180,
                        font=ctk.CTkFont(size=16),
                        command=selectAll)
selectAllBtn.grid(row=3, column=0, padx=(20,20), pady=(10,10), sticky="nw")


deselectBtn = ctk.CTkButton(colFrame2,
                        text="Deselect All",
                        fg_color="transparent",
                        text_color="blue2",
                        hover_color="grey94",
                        corner_radius=0,
                        border_width=1,
                        border_color="blue2",
                        height=50,
                        width=180,
                        font=ctk.CTkFont(size=16),
                        command=deselectAll)
deselectBtn.grid(row=3, column=0, padx=(30,120), pady=(10,10), sticky="ne")
# ..........................................


# sublabel......................................
col2_SubLabel3 = ctk.CTkLabel(colFrame2,
                         text="System Config",
                         font=ctk.CTkFont(size=24),
                         text_color="grey30").grid(row=4, column=0, padx=(20,20), pady=(20,10), sticky="snw")


# text all and selected.................................
col2_text_all = ctk.CTkLabel(colFrame2,
                         text="All",
                         font=ctk.CTkFont(size=12),
                         text_color="grey20").grid(row=5, columnspan=2, column=0, padx=(20,20), pady=(10,10), sticky="snw")


# sliderFunc.............................................
def sliderFunc(value):
    print(value)

systemSlider = ctk.CTkSlider(colFrame2,
                             height=15,
                            #  width=300,
                             from_=0,
                             to=100,
                             button_color="black",
                             progress_color="black",
                             orientation="horizontal",
                             button_hover_color="black",
                             command=sliderFunc,
                             width=10)
systemSlider.grid(row=5, column=0, padx=(40,140), pady=(10,10), sticky="ew")


# text  selected
col2_text_selected = ctk.CTkLabel(colFrame2,
                         text="Selected",
                         font=ctk.CTkFont(size=12),
                         text_color="grey20").grid(row=5, column=0,  padx=(10,95), pady=(10,10), sticky="sne")


# ..............................................................................

# sublabel
col2_SubLabel4 = ctk.CTkLabel(colFrame2,
                         text="General",
                         font=ctk.CTkFont(size=24),
                         text_color="grey30").grid(row=6, column=0, padx=(20,10), pady=(30,0), sticky="snw")


# column 2 radio 
# 
def radioBtnFunc2():
    print(radioVar2.get())

radioVar2 = ctk.StringVar()
# 
# btn's.........................
fileSysScan= ctk.CTkLabel(colFrame2,
                         text="File System Scan",
                         font=ctk.CTkFont(size=15),
                         text_color="grey20").grid(row=7, column=0, padx=(20,10), pady=(5,5), sticky="snw")



col2_rb1 = ctk.CTkRadioButton(colFrame2,
                              text=None,
                              height=2,
                              width=2,
                              command=radioBtnFunc2,
                              fg_color="black",
                              hover_color="black",
                              variable= radioVar2,
                              value="File System Scan",
                              border_width_checked=2)
col2_rb1.grid(row=7, column=0, padx=(30,80), pady=(5,5), sticky="sne")


# ................................................................

collectHash= ctk.CTkLabel(colFrame2,
                         text="Collect Hash",
                         font=ctk.CTkFont(size=15),
                         text_color="grey20").grid(row=7, column=0, padx=(20,10), pady=(80,10), sticky="nw")


col2_rb2 = ctk.CTkRadioButton(colFrame2,
                              text=None,
                              command=radioBtnFunc2,
                              fg_color="black",
                              hover_color="black",
                              variable= radioVar2,
                              value="collectHash",
                              border_width_checked=2)
col2_rb2.grid(row=7, column=0, padx=(30,10), pady=(80,10), sticky="ne")


# .............................................................

fileCount= ctk.CTkLabel(colFrame2,
                         text="file Count",
                         font=ctk.CTkFont(size=16),
                         text_color="grey20").grid(row=8, column=0, columnspan=2, padx=(20,20), pady=(5,10), sticky="nw")

redSquare = PhotoImage(file=r"ctkWindow2Icons\\redSquare.png")

redSquareBtn=ctk.CTkButton(colFrame2,
                        image = redSquare,
                        text=None,
                        fg_color="transparent",
                        # hover_color="grey",
                        hover=False,
                        width=30,
                        height=30,
                        state="disabled")
redSquareBtn.grid(row=8, column=0, padx=(200,10), pady=(0,10), stick="nw")

# .............................................................

fileCount2= ctk.CTkLabel(colFrame2,
                         text="file Count2",
                         font=ctk.CTkFont(size=16),
                         text_color="grey20").grid(row=8, column=0, padx=(250,10), pady=(6,10), sticky="nw")


tickSquare = PhotoImage(file=r"ctkWindow2Icons\\ticksquare.png")

tickSquareBtn=ctk.CTkButton(colFrame2,
                        image = tickSquare,
                        text=None,
                        fg_color="transparent",
                        # hover_color="grey",
                        hover=False,
                        width=30,
                        height=30,
                        state="disabled")
tickSquareBtn.grid(row=8, column=0, padx=(410,10), pady=(0,10), stick="nw")

# ..........................................................................
# column 3
# ..........................................................................

# column frame 3

colFrame3 = ctk.CTkScrollableFrame(root,
                          fg_color="grey92",
                          scrollbar_button_color="grey92",
                          scrollbar_fg_color="transparent",
                          scrollbar_button_hover_color="grey94")
colFrame3.grid(row=1, column=3, padx=(10,30), pady=(20,20), sticky="snew")

# frame label...............................
colLabel3 = ctk.CTkLabel(colFrame3,
                         text="Status",
                         font=ctk.CTkFont(size=28),
                         text_color="black").grid(row=0, column=0, padx=20, pady=10, sticky="snw")


# text .............................................
col3_text1 = ctk.CTkLabel(colFrame3,
                         text="Lorem ipsum dolor sit amet, consecteur adipicsing.",
                         font=ctk.CTkFont(size=12),
                         text_color="grey20").grid(row=0, column=0,padx=(20,20), pady=(80,10), sticky="new")

# .................................
# subFrame
subFrame = ctk.CTkFrame(colFrame3,
                        fg_color="white",
                        width=800)
subFrame.grid(row=1, column=0, padx=(20,20), pady=10, sticky="sn")


# sublabels...............................
subFrameLabel = ctk.CTkLabel(subFrame,
                         text="Resource Summary",
                         font=ctk.CTkFont(size=24),
                         text_color="grey30").grid(row=0, column=0, padx=(20,80), pady=(20,10), sticky="snw")

# 574
subFrameLabel1 = ctk.CTkLabel(subFrame,
                         text="574",
                         font=ctk.CTkFont(family="Roboto",size=30),
                         text_color="grey30").grid(row=1, column=0, padx=(20,10), pady=(0,40), sticky="snw")


subFrameLabel2 = ctk.CTkLabel(subFrame,
                         text="Resources",
                         font=ctk.CTkFont(size=13),
                         text_color="grey30").grid(row=1, column=0, padx=(20,10), pady=(30,10), sticky="snw")


# ..............................................................
#  column 3 subframe labels
col3_label1= ctk.CTkLabel(subFrame,
                         text="Lorem ipsum",
                         font=ctk.CTkFont(size=15),
                         text_color="grey20").grid(row=2, column=0, padx=20, pady=(10,0), sticky="nw")


# ..................................
numLabel1 = ctk.CTkLabel(subFrame,
                         text="2",
                         width=10,
                         font=ctk.CTkFont(size=12, weight='bold'),
                         text_color="grey20").grid(row=2, column=0, padx=(210,20), pady=(10,0), sticky="nw")

green1 = PhotoImage(file=r"ctkWindow2Icons\tickcircle.png")
# userBtn
green1_Btn1=ctk.CTkButton(subFrame,
                        fg_color="transparent",
                        image = green1,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=40,
                        state="disabled")
green1_Btn1.grid(row=2, column=0, padx=(220,20), pady=(10,0), sticky="nw")

# .............................................

col3_label2= ctk.CTkLabel(subFrame,
                         text="Lorem ipsum",
                         font=ctk.CTkFont(size=15),
                         text_color="grey20").grid(row=2, rowspan=6, column=0, padx=20, pady=(40,10), sticky="nw")

# ..................................
numLabel2 = ctk.CTkLabel(subFrame,
                         text="5",
                         width=10,
                         font=ctk.CTkFont(size=12, weight='bold'),
                         text_color="grey20").grid(row=2, column=0, padx=(210,20), pady=(40,10), sticky="nw")

green2 = PhotoImage(file=r"ctkWindow2Icons\tickcircle.png")
# userBtn
green2_Btn2=ctk.CTkButton(subFrame,
                        fg_color="transparent",
                        image = green1,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=40,
                        state="disabled")
green2_Btn2.grid(row=2, column=0, padx=(220,20), pady=(40,10), sticky="nw")

# ..................................
numLabel3 = ctk.CTkLabel(subFrame,
                         text="1",
                         width=10,
                         font=ctk.CTkFont(size=12, weight='bold'),
                         text_color="grey20").grid(row=2, column=0, padx=(170,20), pady=(40,10), sticky="nw")

red2 = PhotoImage(file=r"ctkWindow2Icons\redCircle.png")
# userBtn
red2_Btn2=ctk.CTkButton(subFrame,
                        fg_color="transparent",
                        image = red2,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=10,
                        height=10,
                        state="disabled")
red2_Btn2.grid(row=2, column=0, padx=(180,20), pady=(43,10), sticky="nw")

# ..............................................

col3_label3= ctk.CTkLabel(subFrame,
                         text="Lorem ipsum",
                         font=ctk.CTkFont(size=15),
                         text_color="grey20").grid(row=2, column=0, padx=20, pady=(70,10), sticky="nw")


# ..................................
numLabel4 = ctk.CTkLabel(subFrame,
                         text="2",
                         width=10,
                         font=ctk.CTkFont(size=12, weight='bold'),
                         text_color="grey20").grid(row=2, column=0, padx=(210,20), pady=(70,10), sticky="nw")

green3 = PhotoImage(file=r"ctkWindow2Icons\tickcircle.png")
# userBtn
green3_Btn3=ctk.CTkButton(subFrame,
                        fg_color="transparent",
                        image = green3,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=10,
                        height=10,
                        state="disabled")
green3_Btn3.grid(row=2, column=0, padx=(226,20), pady=(70,10), sticky="nw")

# ..............................................


col3_label4= ctk.CTkLabel(subFrame,
                         text="Lorem ipsum",
                         font=ctk.CTkFont(size=15),
                         text_color="grey20").grid(row=2, column=0, padx=20, pady=(100,10), sticky="nw")

# ..................................
numLabel5 = ctk.CTkLabel(subFrame,
                         text="3",
                         width=10,
                         font=ctk.CTkFont(size=12, weight='bold'),
                         text_color="grey20").grid(row=2, column=0, padx=(210,20), pady=(100,10), sticky="nw")

red5 = PhotoImage(file=r"ctkWindow2Icons\redCircle.png")
# userBtn
red5_Btn5=ctk.CTkButton(subFrame,
                        fg_color="transparent",
                        image = red5,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=10,
                        height=10,
                        state="disabled")
red5_Btn5.grid(row=2, column=0, padx=(225,20), pady=(99,10), sticky="nw")

# ...............................................

col3_label5= ctk.CTkLabel(subFrame,
                         text="Lorem ipsum",
                         font=ctk.CTkFont(size=15),
                         text_color="grey20").grid(row=2, column=0, padx=20, pady=(130,10), sticky="nw")

# ..................................
numLabel6 = ctk.CTkLabel(subFrame,
                         text="2",
                         width=10,
                         font=ctk.CTkFont(size=12, weight='bold'),
                         text_color="grey20").grid(row=2, column=0, padx=(210,20), pady=(130,10), sticky="nw")

green5 = PhotoImage(file=r"ctkWindow2Icons\tickcircle.png")
# userBtn
green5_Btn5=ctk.CTkButton(subFrame,
                        fg_color="transparent",
                        image = green5,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=10,
                        height=10,
                        state="disabled")
green5_Btn5.grid(row=2, column=0, padx=(225,20), pady=(130,10), sticky="nw")
# ........................................
numLabel7 = ctk.CTkLabel(subFrame,
                         text="1",
                         width=10,
                         font=ctk.CTkFont(size=12, weight='bold'),
                         text_color="grey20").grid(row=2, column=0, padx=(170,20), pady=(130,10), sticky="nw")

yellow5 = PhotoImage(file=r"ctkWindow2Icons\exclaim.png")
# userBtn
yellow5_Btn5=ctk.CTkButton(subFrame,
                        fg_color="transparent",
                        image = yellow5,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=10,
                        height=10,
                        state="disabled")
yellow5_Btn5.grid(row=2, column=0, padx=(180,20), pady=(132,10), sticky="nw")

# ........................................

col3_label6= ctk.CTkLabel(subFrame,
                         text="Lorem ipsum",
                         font=ctk.CTkFont(size=15),
                         text_color="grey20").grid(row=2, column=0, padx=20, pady=(160,10), sticky="nw")


numLabel8 = ctk.CTkLabel(subFrame,
                         text="10",
                         width=10,
                         font=ctk.CTkFont(size=11, weight='bold'),
                         text_color="grey20").grid(row=2, column=0, padx=(207,20), pady=(160,10), sticky="nw")

green6 = PhotoImage(file=r"ctkWindow2Icons\tickcircle.png")
# userBtn
green6_Btn6=ctk.CTkButton(subFrame,
                        fg_color="transparent",
                        image = green6,
                        text=None,
                        # hover_color="grey",
                        hover=False,
                        width=10,
                        height=10,
                        state="disabled")
green6_Btn6.grid(row=2, column=0, padx=(225,20), pady=(160,10), sticky="nw")


# column 3 subframe btn.......................................
def btnFunc3():
    print("button pressed 3")

viewAll = ctk.CTkButton(subFrame,
                        fg_color="transparent",
                        text="View All",
                        text_color="blue2",
                        border_color="blue2",
                        hover_color="grey98",
                        corner_radius=0,
                        border_width=1,
                        height=50,
                        font=ctk.CTkFont(size=16),
                        command=btnFunc3)
viewAll.grid(row=3, column=0, padx=(20,50), pady=(10,10), sticky="sne")



# ........................................................
# column 3 btn's


# start and delete account btn's
def btnFunc4():
    print("button pressed 4")

startBtn = ctk.CTkButton(colFrame3,
                        text="Start",
                        fg_color="green4",
                        hover_color="green",
                        corner_radius=0,
                        font=ctk.CTkFont(weight="bold"),
                        height=40,
                        width=130,
                        command=btnFunc4)
startBtn.grid(row=2, column=0, padx=(20,10), pady=(60,10), sticky="snw")


delBtn = ctk.CTkButton(colFrame3,
                        text="Delete Account",
                        fg_color="red3",
                        hover_color="red3",
                        corner_radius=0,
                        font=ctk.CTkFont(weight="bold"),
                        height=40,
                        width=130,
                        command=btnFunc4)
delBtn.grid(row=2, column=0, padx=(0,50), pady=(60,10), sticky="sne")


root.mainloop()