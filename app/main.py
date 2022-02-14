import Tkinter as tk
import os,sys
import csv

root = tk.Tk()
root.title('UMP-link by Darwish Zain')

#? comment filename not in use
#? linux -or- windows 10
file = './app/command-linux.csv'#!linux
#file = './app/command-win10.csv'#!windows10
#? number of row in csv
num = 4
#* control number of button visible
#* control width of footer according to number of button

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
frameMain = tk.Frame(root, height=300, width=500)
frameMain.grid(row=0, column=0)

for r in range(num):
    linecsv[r][0] = tk.Button(frameMain, height=5, width=5,text=linecsv[r][2],command=lambda:command(linecsv[r][1]))
    linecsv[r][0].grid(row=linecsv[r][3], column=linecsv[r][4])

#? button to link Darwish Zain's website
devsite = tk.Button(frameMain, text=linecsv[num][2], command=lambda:command(linecsv[num][1]))
devsite.grid(row=linecsv[num][3], column=linecsv[num][4], columnspan=num, sticky='nesw')

#? button to link Darwish Zain's github
github = tk.Button(frameMain, text=linecsv[num+1][2], command=lambda:command(linecsv[num+1][1]))
github.grid(row=linecsv[num+1][3], column=linecsv[num+1][4], columnspan=num, sticky='nesw')

root.mainloop()

#! unused code
#? just for my reference later on
#btnkalam = tk.Button(frameMain, text=d[1][2],command=lambda:command(d[1][1]))
#btnkalam.grid(row=1, column=0)
#d[1][0] = tk.Button(frameMain, height=5, width=5,text=d[1][2],command=lambda:command(d[1][1]))
#d[1][0].grid(row=1, column=1)
#btnOr = tk.Button(root, image='../img/or.ump.png')
#btnOr.grid(row=0, column=0)
