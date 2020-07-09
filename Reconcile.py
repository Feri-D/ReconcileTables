import csv
import os
import logging
import tkinter as tk
from tkinter import filedialog

#set logging format, level and location
logging.basicConfig(
    format='%(asctime)s: Line %(lineno)d: %(message)s',
    level=logging.INFO,
    filename = 'reconcile.log',
    filemode = 'w')
logging.info('start')  
"""
# Testing input file names
oldList = 'Old_prices.csv'
newList = 'New_prices.csv'
"""
# Ask for input files
root = tk.Tk()
root.withdraw()

oldList = filedialog.askopenfilename(title='Select the OLD list')
newList = filedialog.askopenfilename(title='Select the NEW list')

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
                    print("difference saved:",row_old[oldLabels[0]])
                    logging.info(f'difference saved for: {row_old[oldLabels[0]]}')
                else:                 
                    print("no difference found:",row_old[oldLabels[0]])
                    logging.info(f'no diffrerence found for: {row_old[oldLabels[0]]}')
                           
        # Evaulationg removals
        if found != True: 
            result_file.write( f'\n{row_old[oldLabels[0]]},Removed')
            print("no entry found:",row_old[oldLabels[0]])   
            logging.info(f'no entry found for: {row_old[oldLabels[0]]}')

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
            print("found as extra:",row_new[newLabels[0]]) 
            logging.info(f'new entry found for: {row_new[newLabels[0]]}')  

# Closing files
old_file.close()
new_file.close()
result_file.close()

# Present result file
os.startfile ('Result.csv')

logging.info('done')  