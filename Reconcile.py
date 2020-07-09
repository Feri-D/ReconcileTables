import csv
import os
import tkinter as tk
from tkinter import filedialog

# Ask for input files
root = tk.Tk()
root.withdraw()

oldList = filedialog.askopenfilename(title='Select the OLD list')
newList = filedialog.askopenfilename(title='Select the NEW list')
"""
# Testing input file names
oldList = 'Old_prices.csv'
newList = 'New_prices.csv'
"""
# Open up files
with open(oldList, mode='r') as old_file, open(newList, 'r') as new_file, open('Result.csv', 'w') as result_file:
    csv_old = csv.DictReader(old_file)
    csv_new = csv.DictReader(new_file)
    firstLine = False

    # Evaulationg price differences
    for row_old in csv_old:  
        found = False
        if firstLine != True:
            oldLabels = csv_old.fieldnames
            newLabels = csv_new.fieldnames
            result_file.write( f'{newLabels[0]},{newLabels[1]}')
            firstLine = True
        new_file.seek(0,0)
        for row_new in csv_new:
            if row_old[oldLabels[0]] == row_new[newLabels[0]]:
                found = True
                if row_old[oldLabels[1]] != row_new[newLabels[1]]:
                    result_file.write( f'\n{row_old[oldLabels[0]]},{int(row_new[newLabels[1]])-int(row_old[oldLabels[1]])}')
                    print("difference saved",row_old[oldLabels[0]])
                else:                 
                    print("no diff found",row_old[oldLabels[0]])  
                           
        # Evaulationg removals
        if found != True: 
            result_file.write( f'\n{row_old[oldLabels[0]]},Removed')
            print("not found",row_old[oldLabels[0]])   

    # Finding additions
    new_file.seek(0,0)
    for row_new in csv_new:
        found = False
        old_file.seek(0,0)
        for row_old in csv_old:
            if row_old[oldLabels[0]] == row_new[newLabels[0]]:
                found = True
    # log additions
        if found != True: 
            result_file.write( f'\n{row_new[newLabels[0]]},Added')
            print("found as extra",row_new[newLabels[0]])   

# Closing files
old_file.close()
new_file.close()
result_file.close()

# Present result file
os.startfile ('Result.csv')