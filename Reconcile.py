import csv
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

with open(oldList, mode='r') as old_file, open(newList, 'r') as new_file, open('Result.csv', 'w') as outFile:
    csv_old = csv.DictReader(old_file)
    csv_new = csv.DictReader(new_file)
    oldLineCount = 0
    newLineCount = 0

    for row_old in csv_old:  
        if oldLineCount == 0:
            oldLabels = csv_old.fieldnames
            newLabels = csv_new.fieldnames
            outFile.write( f'{oldLabels[0]},{oldLabels[1]}')
            oldLineCount += 1
        oldLineCount += 1
        newLineCount = 1
        new_file.seek(0,0)
        for row_new in csv_new:
            if row_old[oldLabels[0]] == row_new[newLabels[0]]:
                if row_old[oldLabels[1]] != row_new[newLabels[1]]:
                    outFile.write( f'\n{row_old[oldLabels[0]]},{int(row_new[newLabels[1]])-int(row_old[oldLabels[1]])}')
                    newLineCount += 1
                newLineCount += 1
            newLineCount += 1   
    oldLineCount += 1

# Open result file
#os.startfile ('Result.csv')