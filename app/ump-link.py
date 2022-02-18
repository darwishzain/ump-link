import Tkinter as tk
import os,sys
import csv

root = tk.Tk()
root.title('UMP-link on '+os.name)
if os.name=='posix':
    file = './data/command-linux.csv'#!linux
elif os.name=='nt':
    file = './data/command-win10.csv'#!windows10

print('Running ump-link on '+os.name)

#? csv format,id, command, name, row, column
linecsv = []#* array variable for data from csv file
with open(file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        linecsv.append(row)
    # array : linecsv

#print(linecsv)#* checking if data from csv file came through
#? run cli command
def command(cmd):
    os.system(cmd)

#? frame where the button is in
fmain = tk.Frame(root, bg='#F0F0F0', height=300, width=500)
fmain.grid(row=0, column=0)

def umplink():
    kalamBtn = tk.Button(fmain, bg='#F0F0F0', height=5, width=5,text=linecsv[0][2],command=lambda:command(linecsv[0][1]), relief='flat')
    kalamBtn.grid(row=linecsv[0][3], column=linecsv[0][4])
    ecommBtn = tk.Button(fmain, height=5, width=5,text=linecsv[1][2],command=lambda:command(linecsv[1][1]), relief='flat')
    ecommBtn.grid(row=linecsv[1][3], column=linecsv[1][4])
    orBtn = tk.Button(fmain, height=5, width=5,text=linecsv[2][2],command=lambda:command(linecsv[2][1]), relief='flat')
    orBtn.grid(row=linecsv[2][3], column=linecsv[2][4])
    udasBtn = tk.Button(fmain, height=5, width=5,text=linecsv[3][2],command=lambda:command(linecsv[3][1]), relief='flat')
    udasBtn.grid(row=linecsv[3][3], column=linecsv[3][4])
    efindBtn = tk.Button(fmain, height=5, width=5,text=linecsv[4][2],command=lambda:command(linecsv[4][1]), relief='flat')
    efindBtn.grid(row=linecsv[4][3], column=linecsv[4][4])

umplink()
#? button to link Darwish Zain's website
devsite = tk.Button(fmain, text=linecsv[5][2], command=lambda:command(linecsv[5][1]), relief='flat')
devsite.grid(row=linecsv[5][3], column=linecsv[5][4], columnspan=3, sticky='nesw')

#? button to link Darwish Zain's github
github = tk.Button(fmain, text=linecsv[6][2], command=lambda:command(linecsv[6][1]), relief='flat')
github.grid(row=linecsv[6][3], column=linecsv[6][4], columnspan=1, sticky='nesw')

donate = tk.Button(fmain, bg='#00AC9F', text=linecsv[7][2], command=lambda:command(linecsv[7][1]), relief='flat')
donate.grid(row=linecsv[7][3], column=linecsv[7][4], columnspan=1, sticky='nesw')

root.mainloop()

#! unused code
#? just for my reference later on
#btnkalam = tk.Button(fmain, text=d[1][2],command=lambda:command(d[1][1]))
#btnkalam.grid(row=1, column=0)
#d[1][0] = tk.Button(fmain, height=5, width=5,text=d[1][2],command=lambda:command(d[1][1]))
#d[1][0].grid(row=1, column=1)
#btnOr = tk.Button(root, image='../img/or.ump.png')
#btnOr.grid(row=0, column=0)
