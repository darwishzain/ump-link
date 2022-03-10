import tkinter as tk
#! linux : Tkinter
#! win10 : tkinter
import os,sys
import csv
import time

label = 'UMP-link on '+ sys.platform
developer = 'Developed by Darwish Zain'
version = 'Version 0.1.6 - dev'

print(label)
time.sleep(1)
print(developer)
time.sleep(1)
print(version)
time.sleep(1)

root = tk.Tk()
root.title(label+" "+version)

file = './data/command.csv'

#? csv format: id, command, displayname, row, column
line = []#* array variable for data from csv file
with open(file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        line.append(row)
    # array : line

#print(line)#* checking if data from csv file came through
#? runFrame cli command
def command(cmd):
    os.system(cmd)

def openlink(link):
    if os.name == 'posix':
        link='xdg-open '+link
    elif os.name == 'nt':
        link = 'explorer'+link
    os.system(link)

#? frame where the button is in
mainFrame = tk.Frame(root, bg='#F0F0F0', height=300, width=500)
mainFrame.grid(row=0, column=0)
titleFrame = tk.Frame(mainFrame, bg='#FFF')
titleFrame.grid(row=0, column=4, columnspan=5)
clockFrame = tk.Frame(mainFrame, bg="#FFF")
clockFrame.grid(row=1, column=0)
webFrame = tk.Frame(mainFrame)
webFrame.grid(row=2, column=0, columnspan=5)
runFrame = tk.Frame(mainFrame)
runFrame.grid(row=3, column=0)
devFrame = tk.Frame(mainFrame, bg='#FFF')
devFrame.grid(row=4, column=0, columnspan=5)
#root.attributes('-zoomed', True)
#root.state('zoomed')
def titleBar():
    closeBtn = tk.Button(titleFrame, text='X', bg='#DF0024', fg='#FFF', command=root.destroy ,relief='flat')
    closeBtn.grid(row=0, column=5, sticky='nesw')
    maxBtn = tk.Button(titleFrame, text="[]", bg="#F3C300", fg="#FFF", relief="flat")
    maxBtn.grid(row=0, column=4, sticky='nesw')#TODO maximize windows
    miniBtn = tk.Button(titleFrame, text='_', bg='#2E6DB4', fg='#FFF', relief='flat')
    miniBtn.grid(row=0, column=3, sticky='nesw')#TODO minimize windows

def startTime():
    global timeDisplay, dateDisplay
    timeDisplay = tk.Label(clockFrame, text="HH:MM::SS")
    timeDisplay.grid(row=0, column=0, columnspan=2)
    dateDisplay = tk.Label(clockFrame, text="DD/MM/YYYY")
    dateDisplay.grid(row=0, column=3, columnspan=2)
    updateTime()

def updateTime():
    global timeH24, timeH12, timeM, timeS
    global dateD, dateM, dateY
    timeH24 = time.strftime("%H")
    timeH12 = time.strftime("%I")
    timeM = time.strftime("%M")
    timeS = time.strftime("%S")
    dateD  = time.strftime("%d")
    dateM  = time.strftime("%m")
    dateY  = time.strftime("%Y")

    clock = timeH24+":"+timeM+":"+timeS
    timeDisplay.config(text=clock)
    date = dateD+"/"+dateM+"/"+dateY
    dateDisplay.config(text=date)
    root.after(1000,updateTime)

def webBtn():
    kalamBtn = tk.Button(webFrame, bg='#F0F0F0', height=5, width=10, text=line[0][2],command=lambda:openlink(line[0][1]), relief='flat')
    kalamBtn.grid(row=line[0][3], column=line[0][4])
    ecommBtn = tk.Button(webFrame, height=5, width=10, text=line[1][2],command=lambda:openlink(line[1][1]), relief='flat')
    ecommBtn.grid(row=line[1][3], column=line[1][4])
    orBtn = tk.Button(webFrame, height=5, width=10, text=line[2][2],command=lambda:openlink(line[2][1]), relief='flat')
    orBtn.grid(row=line[2][3], column=line[2][4])
    udasBtn = tk.Button(webFrame, height=5, width=10, text=line[3][2],command=lambda:openlink(line[3][1]), relief='flat')
    udasBtn.grid(row=line[3][3], column=line[3][4])
    efindBtn = tk.Button(webFrame, height=5, width=10, text=line[4][2],command=lambda:openlink(line[4][1]), relief='flat')
    efindBtn.grid(row=line[4][3], column=line[4][4])

def runBtn():
    codeBtn = tk.Button(runFrame, bg='#F0F0F0', height=5, width=10, text=line[5][2], command=lambda:command(line[5][1]), relief='flat')
    codeBtn.grid(row=0, column=0)
    githubBtn = tk.Button(runFrame, bg='#F0F0F0', height=5, width=10, text=line[6][2], command=lambda:command(line[6][1]), relief='flat')
    githubBtn.grid(row=0, column=1)

def devBtn():
    #? button to link Darwish Zain's webFrame
    devsite = tk.Button(devFrame, text=line[7][2], command=lambda:openlink(line[7][1]), relief='flat')
    devsite.grid(row=line[7][3], column=line[7][4], columnspan=3, sticky='nesw')

    #? button to link Darwish Zain's github
    github = tk.Button(devFrame, text=line[8][2], command=lambda:openlink(line[8][1]), relief='flat')
    github.grid(row=line[8][3], column=line[8][4], columnspan=1, sticky='nesw')

    donate = tk.Button(devFrame, bg='#00AC9F', fg='#FFFFFF', text=line[9][2], command=lambda:openlink(line[9][1]), relief='flat')
    donate.grid(row=line[9][3], column=line[9][4], columnspan=1, sticky='nesw')

    affiliate = tk.Button(devFrame, bg='#2E6DB4', fg='#FFFFFF', text=line[10][2], command=lambda:openlink(line[10][1]), relief='flat')
    affiliate.grid(row=line[10][3], column=line[10][4], columnspan=1, sticky='nesw')

titleBar()
startTime()
webBtn()
runBtn()
devBtn()

root.iconbitmap('./image/UMP-link.ico')
root.eval('tk::PlaceWindow . center')#? Application positioned at center of screen
root.mainloop()

#! unused code
#? just for my reference later on
#btnkalam = tk.Button(mainFrame, text=d[1][2],command=lambda:command(d[1][1]))
#btnkalam.grid(row=1, column=0)
#d[1][0] = tk.Button(mainFrame, height=5, width=10,text=d[1][2],command=lambda:command(d[1][1]))
#d[1][0].grid(row=1, column=1)
#btnOr = tk.Button(root, image='../img/or.ump.png')
#btnOr.grid(row=0, column=0)
#if os.name=='posix':
#    file = './data/command-linux.csv'#!linux
#elif os.name=='nt':
#    file = './data/command-win10.csv'#!windows10
