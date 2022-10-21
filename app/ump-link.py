import tkinter as tk
#! linux : Tkinter
#! win10 : tkinter
import os,sys
import csv
import time

appName = 'UMP-link on '+ sys.platform
developer = 'Developed by Darwish Zain'
version = 'Version 1.0.0 - akhr'

print(appName)
time.sleep(1)
print(developer)
time.sleep(1)
print(version)
time.sleep(1)

root = tk.Tk()
root.title(appName+" "+version)

runLine = [
    ["code","code", "VSCode", 0, 0],
    ["github", "github", "Github", 0, 1],
    ["browser", "https://google.com", "Browser", 0, 2]
    ]

webLine = [
    ["kalam-ump", "https://kalam.ump.edu.my", "KALAM", 0, 0],
    ["ecomm-ump", "https://community.ump.edu.my", "ECOMM", 0, 1],
    ["or-ump", "https://or.ump.edu.my", "OR UMP", 0, 2],
    ["udas-ump", "https://udas.ump.edu.my", "UDAS", 0, 3],
    ["efind-ump", "https://efind.ump.edu.my", "EFind", 0, 4]
    ]

devLine =[
    ["github", "https://github.com/darwishzain", "More Code", 0, 1],
    ["github", "https://darwishzain.com", "Website", 0, 2]
    ]
file = './data/command.csv'


#? runFrame cli command
def command(cmd):
    os.system(str(cmd))

def openlink(link):
    if os.name == 'posix':
        link='xdg-open '+link
    elif os.name == 'nt':
        link = 'explorer '+link
    os.system(str(link))

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
    kalamBtn = tk.Button(webFrame, bg='#F0F0F0', height=5, width=10, text=webLine[0][2],command=lambda:openlink(webLine[0][1]), relief='flat')
    kalamBtn.grid(row=webLine[0][3], column=webLine[0][4])
    ecommBtn = tk.Button(webFrame, height=5, width=10, text=webLine[1][2],command=lambda:openlink(webLine[1][1]), relief='flat')
    ecommBtn.grid(row=webLine[1][3], column=webLine[1][4])
    orBtn = tk.Button(webFrame, height=5, width=10, text=webLine[2][2],command=lambda:openlink(webLine[2][1]), relief='flat')
    orBtn.grid(row=webLine[2][3], column=webLine[2][4])
    udasBtn = tk.Button(webFrame, height=5, width=10, text=webLine[3][2],command=lambda:openlink(webLine[3][1]), relief='flat')
    udasBtn.grid(row=webLine[3][3], column=webLine[3][4])
    efindBtn = tk.Button(webFrame, height=5, width=10, text=webLine[4][2],command=lambda:openlink(webLine[4][1]), relief='flat')
    efindBtn.grid(row=webLine[4][3], column=webLine[4][4])

def runBtn():
    codeBtn = tk.Button(runFrame, bg='#F0F0F0', height=5, width=10, text=runLine[0][2], command=lambda:command(runLine[0][1]), relief='flat')
    codeBtn.grid(row=runLine[0][3], column=runLine[0][4])
    githubBtn = tk.Button(runFrame, bg='#F0F0F0', height=5, width=10, text=runLine[1][2], command=lambda:command(runLine[1][1]), relief='flat')
    githubBtn.grid(row=runLine[1][3], column=runLine[1][4])
    browserBtn = tk.Button(runFrame, bg="#F0F0F0", height=5, width=10, text=runLine[2][2], command=lambda:openlink(runLine[2][1]), relief="flat")
    browserBtn.grid(row=runLine[2][3], column=runLine[2][4])

def devBtn():
    #? button to link Darwish Zain's github
    github = tk.Button(devFrame, text=devLine[0][2], command=lambda:openlink(devLine[0][1]), relief='flat')
    github.grid(row=devLine[0][3], column=devLine[0][4], columnspan=1, sticky='nesw')
    #? button to link Darwish Zain's Website
    website = tk.Button(devFrame, text=devLine[1][2], command=lambda:openlink(devLine[1][1]), relief='flat')
    website.grid(row=devLine[1][3], column=devLine[1][4], columnspan=1, sticky='nesw')

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
