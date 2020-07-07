#import csv
import os
import tkinter as tk
from tkinter import filedialog
"""
# Ask for input files
root = tk.Tk()
root.withdraw()

oldList = filedialog.askopenfilename(title='Select the OLD list')
newList = filedialog.askopenfilename(title='Select the NEW list')
"""
# Testing input file names
oldList = 'Old_prices.csv'
newList = 'New_prices.csv'

with open(oldList, 'r') as t1, open(newList, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()
print(fileone)
print(filetwo)
with open('Result.csv', 'w') as outFile:
    for line in filetwo:
        if line in fileone:
            outFile.write(line)

#os.startfile ('Result.csv')