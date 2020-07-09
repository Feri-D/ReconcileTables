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
    line_count = 0
    for row in csv_old:
        if line_count == 0:
            labels = csv_old.fieldnames
            outFile.write( f'{labels[0]},{labels[1]}')
            line_count += 1
        print(f'\t{row[labels[0]]} costs {row[labels[1]]}.')
        outFile.write( f'\n{row[labels[0]]},{row[labels[1]]}')
        line_count += 1
    print(f'Processed {line_count} lines.')

# Open result file
# os.startfile ('Result.csv')