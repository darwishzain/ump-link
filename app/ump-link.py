import tkinter as tk
#! linux : Tkinter
#! win10 : tkinter
import os,sys
import csv
import time

developer = 'Darwish Zain'
version = '0.1.6 - dev'

root = tk.Tk()
root.title('UMP-link on '+ sys.platform + ' v' +version)

if os.name=='posix':
    file = './data/command-linux.csv'#!linux
elif os.name=='nt':
    file = './data/command-win10.csv'#!windows10

print('Running ump-link on '+ sys.platform)
time.sleep(1)
print('Developed by '+ developer)
time.sleep(1)
print('Version '+ version)
time.sleep(1)
#? csv format,id, command, name, row, column
line = []#* array variable for data from csv file
with open(file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        line.append(row)
    # array : line

#print(line)#* checking if data from csv file came through
#? run cli command
def command(cmd):
    os.system(cmd)

#? frame where the button is in
fmain = tk.Frame(root, bg='#F0F0F0', height=300, width=500)
fmain.grid(row=0, column=0)
titlebar = tk.Frame(fmain, bg='#FFF')
titlebar.grid(row=0, column=0, columnspan=5)
website = tk.Frame(fmain)
website.grid(row=1, column=0, columnspan=5)
openapp = tk.Frame(fmain)
openapp.grid(row=2, column=0)
devbar = tk.Frame(fmain, bg='#FFF')
devbar.grid(row=3, column=0, columnspan=5)

def bartitle():
    closebtn = tk.Button(titlebar, text='X', bg='#DF0024', fg='#FFF', relief='flat')
    closebtn.grid(row=0, column=5, sticky='nesw')
    minibtn = tk.Button(titlebar, text='_', bg='#2E6DB4', fg='#FFF', relief='flat')
    minibtn.grid(row=0, column=4, sticky='nesw')

def umplink():
    kalamBtn = tk.Button(website, bg='#F0F0F0', height=5, width=10, text=line[0][2],command=lambda:command(line[0][1]), relief='flat')
    kalamBtn.grid(row=line[0][3], column=line[0][4])
    ecommBtn = tk.Button(website, height=5, width=10, text=line[1][2],command=lambda:command(line[1][1]), relief='flat')
    ecommBtn.grid(row=line[1][3], column=line[1][4])
    orBtn = tk.Button(website, height=5, width=10, text=line[2][2],command=lambda:command(line[2][1]), relief='flat')
    orBtn.grid(row=line[2][3], column=line[2][4])
    udasBtn = tk.Button(website, height=5, width=10, text=line[3][2],command=lambda:command(line[3][1]), relief='flat')
    udasBtn.grid(row=line[3][3], column=line[3][4])
    efindBtn = tk.Button(website, height=5, width=10, text=line[4][2],command=lambda:command(line[4][1]), relief='flat')
    efindBtn.grid(row=line[4][3], column=line[4][4])

def appopen():
    codeBtn = tk.Button(openapp, bg='#F0F0F0', height=5, width=10, text='VSCode',command=lambda:command('code'), relief='flat')
    codeBtn.grid(row=0, column=0)
def devlink():
    #? button to link Darwish Zain's website
    devsite = tk.Button(devbar, text=line[5][2], command=lambda:command(line[5][1]), relief='flat')
    devsite.grid(row=line[5][3], column=line[5][4], columnspan=3, sticky='nesw')

    #? button to link Darwish Zain's github
    github = tk.Button(devbar, text=line[6][2], command=lambda:command(line[6][1]), relief='flat')
    github.grid(row=line[6][3], column=line[6][4], columnspan=1, sticky='nesw')

    donate = tk.Button(devbar, bg='#00AC9F', fg='#FFFFFF', text=line[7][2], command=lambda:command(line[7][1]), relief='flat')
    donate.grid(row=line[7][3], column=line[7][4], columnspan=1, sticky='nesw')

#bartitle()
umplink()
appopen()
devlink()

root.iconbitmap('./icon.ico')
root.eval('tk::PlaceWindow . center')#? Application apppear at center of screen
root.mainloop()

#! unused code
#? just for my reference later on
#btnkalam = tk.Button(fmain, text=d[1][2],command=lambda:command(d[1][1]))
#btnkalam.grid(row=1, column=0)
#d[1][0] = tk.Button(fmain, height=5, width=10,text=d[1][2],command=lambda:command(d[1][1]))
#d[1][0].grid(row=1, column=1)
#btnOr = tk.Button(root, image='../img/or.ump.png')
#btnOr.grid(row=0, column=0)
