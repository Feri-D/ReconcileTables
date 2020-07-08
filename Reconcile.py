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

with open(oldList, 'r') as t1, open(newList, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()
print(fileone)
print(filetwo)

with open('Result.csv', 'w') as outFile:
    for line in filetwo:
        if line in fileone:
            outFile.write(line)
            outFile.write("test \n")
"""
with open(oldList) as f:
    for i, line in enumerate(f):             
        print ("line {0} = {1}".format(i, line.split()))
with open(newList) as f:
    for i, line in enumerate(f):             
        print("line {0} = {1}".format(i, line.split()))
"""
with open(oldList, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["ï»¿Name"]} costs {row["Price"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

with open(newList, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["ï»¿Name"]} costs {row["Price"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')


# Open result file
# os.startfile ('Result.csv')