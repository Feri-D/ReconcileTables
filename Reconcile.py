import sys
import os
import csv
import logging
import tkinter as tk
from tkinter import filedialog

# SELECT TEST MODE HERE
TestMode = False

# Set logging format, level and location
if TestMode == True:
    logging.basicConfig(
        format='%(asctime)s:%(levelname)s:Line %(lineno)d: %(message)s',
        level=logging.DEBUG,
        filename = 'reconcile.log',
        filemode = 'w')
else:
    logging.basicConfig(
        format='%(asctime)s: Line %(lineno)d: %(message)s',
        level=logging.INFO,
        filename = 'reconcile.log',
        filemode = 'w')
logging.info('start')  
logging.debug("TEST MODE")

remoteUser = False
oldList = None
newList = None

# Files used in test mode
if TestMode == True:
    oldList = 'Old_prices.csv'
    newList = 'New_prices.csv'
    logging.debug("TEST INPUTS USED")

# Handle input file names as arguments
if (len(sys.argv)>1 ):
    oldList = sys.argv[1]
    logging.debug("FIRST argument received")
    print ("Usage details: Reconcile.py <OldListPath> <NewListPath>")
if (len(sys.argv)>2 ):
    newList = sys.argv[2]
    logging.debug("SECOND argument received")    
    remoteUser = True
if (len(sys.argv)>3 ):
    print ("Usage details: Reconcile.py <OldListPath> <NewListPath>")
    logging.debug("TOO MANY arguments received")

# Ask for missing input files
root = tk.Tk()
root.withdraw()

if oldList == None:
    oldList = filedialog.askopenfilename(title='Select the OLD list')
if newList == None:
    newList = filedialog.askopenfilename(title='Select the NEW list')

# Open up files
with open(oldList, mode='r') as old_file, open(newList, 'r') as new_file, open('Result.csv', 'w') as result_file:
    csv_old = csv.DictReader(old_file)
    csv_new = csv.DictReader(new_file)
    firstLine = False

# Evaluate price differences
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
                           
# Evaluate removals
        if found != True: 
            result_file.write( f'\n{row_old[oldLabels[0]]},Removed')
            print("no entry found:",row_old[oldLabels[0]])   
            logging.info(f'no entry found for: {row_old[oldLabels[0]]}')

# Find additions
    new_file.seek(0,0)
    for row_new in csv_new:
        found = False
        old_file.seek(0,0)
        for row_old in csv_old:
            if row_old[oldLabels[0]] == row_new[newLabels[0]]:
                found = True
# Log additions
        if found != True: 
            result_file.write( f'\n{row_new[newLabels[0]]},Added')
            print("found as extra:",row_new[newLabels[0]]) 
            logging.info(f'new entry found for: {row_new[newLabels[0]]}')  

# Close files
old_file.close()
new_file.close()
result_file.close()

# Present result file
if (TestMode != True)*(remoteUser != True):
    os.startfile ('Result.csv')
print("Saved in Result.csv")   

logging.info('done')  