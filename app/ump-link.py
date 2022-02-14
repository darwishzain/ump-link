import tkinter as tk
import os,sys
import csv
#? UMP CYAN #00ADA5

root = tk.Tk()
root.title('UMP-link')
#? remove title bar
#root.attributes('-type','dock')
#root.attributes('-alpha',0.9)#? reduce opacity


#? comment filename not in use
#? linux -or- windows 10
#file = './app/command-linux.csv'#!linux
file = './command-win10.csv'#!windows10

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
framemain = tk.Frame(root)
framemain.grid(row=1, column=0)
#? all ump-link button
kalam = tk.Button(framemain, height=5, width=10, text=linecsv[0][2],command=lambda:command(linecsv[0][1]))
kalam.grid(row=linecsv[0][3], column=linecsv[0][4])

kalam = tk.Button(framemain, height=5, width=10, text=linecsv[1][2],command=lambda:command(linecsv[1][1]))
kalam.grid(row=linecsv[1][3], column=linecsv[1][4])

kalam = tk.Button(framemain, height=5, width=10, text=linecsv[2][2],command=lambda:command(linecsv[2][1]))
kalam.grid(row=linecsv[2][3], column=linecsv[2][4])

kalam = tk.Button(framemain, height=5, width=10, text=linecsv[3][2],command=lambda:command(linecsv[3][1]))
kalam.grid(row=linecsv[3][3], column=linecsv[3][4])
#? button to link Darwish Zain's website
devsite = tk.Button(framemain, text=linecsv[4][2], bg='#FFFFFF', fg='#00AC9F', command=lambda:command(linecsv[4][1]), relief='flat')
devsite.grid(row=linecsv[4][3], column=linecsv[4][4], columnspan=2, sticky='nesw')

#? button to link Darwish Zain's github
github = tk.Button(framemain, text=linecsv[5][2], bg='#6E5494', fg='#FFFFFF', command=lambda:command(linecsv[5][1]), relief='flat')
github.grid(row=linecsv[5][3], column=linecsv[5][4], columnspan=2, sticky='nesw')

side = tk.Frame(framemain)
side.grid(row=0, column=3)
mini = tk.Button(side, text='_',  bg='#87CEEB',command=lambda:root.iconify(), relief='flat')
mini.grid(row=1, column=1)
close = tk.Button(side, text='X', bg='#DC143C', command=lambda:root.destroy(), relief='flat')
close.grid(row=1, column=2)
#? position window to centerof screen
root.eval('tk::PlaceWindow . center')
root.mainloop()

#! unused code
#? just for my reference later on
#for r in range(4):    linecsv[r][0] = tk.Button(framemain, height=5, width=5,text=linecsv[r][2],command=lambda:command(linecsv[r][1]))    linecsv[r][0].grid(row=linecsv[r][3], column=linecsv[r][4])

#btnkalam = tk.Button(framemain, text=d[1][2],command=lambda:command(d[1][1]))
#btnkalam.grid(row=1, column=0)
#d[1][0] = tk.Button(framemain, height=5, width=5,text=d[1][2],command=lambda:command(d[1][1]))
#d[1][0].grid(row=1, column=1)
#btnOr = tk.Button(root, image='../img/or.ump.png')
#btnOr.grid(row=0, column=0)
