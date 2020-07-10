import sys
import os
import csv
import logging
import tkinter as tk
from tkinter import filedialog

def createDictFromCsv(csvReaderFile, uniqueHeaderKey):
    dict = {}
    firstRow = []
    nameIndex = 0
    for i, row in enumerate(csvReaderFile):
        if i == 0:
            firstRow = row
            nameIndex = firstRow.index(uniqueHeaderKey)
        if i != 0:
            name = row[nameIndex]
            valueDict = {}
            for y,value in enumerate(row):
                if y != nameIndex:
                    keyValuePair = {firstRow[y] : value}
                    valueDict.update(keyValuePair)
            dict[name] = valueDict
    return dict


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
with open(oldList, mode='r', encoding = 'utf-8-sig') as old_file, open(newList, 'r', encoding = 'utf-8-sig') as new_file, open('Result.csv', 'w', encoding = 'utf8') as result_file:

    # Create dictionaries from the csv file
    csv_old_dict = createDictFromCsv(csv.reader(old_file, delimiter = ','), 'Name')
    logging.info("Old dict: %s" % csv_old_dict)
    csv_new_dict = createDictFromCsv(csv.reader(new_file, delimiter = ','), 'Name')
    logging.info("New dict: %s "% csv_new_dict)

    # Get headers for the value columns 
    valueKeys = csv_old_dict[list(csv_old_dict.keys())[0]].keys()
    # Create name header (unique identifier)
    result_file.write( f'Name')
    # Create other headers
    for key in valueKeys:
        result_file.write( f',{key}')

    # Define which items belong to which category (both lists, old list, new list)
    itemsInBothLists = (item for item in csv_old_dict.keys() if item in csv_new_dict.keys())
    itemsOnlyInOldList = (item for item in csv_old_dict.keys() if item not in csv_new_dict.keys())
    itemsOnlyInNewList = (item for item in csv_new_dict.keys() if item not in csv_old_dict.keys())
    
    # Print items for each of the respective categories
    for itemName in itemsInBothLists:
        priceColumn = 'Price'
        oldPrice = int(csv_old_dict.get(itemName, {}).get(priceColumn))
        newPrice = int(csv_new_dict.get(itemName, {}).get(priceColumn))
        if oldPrice != newPrice:
            result_file.write( f'\n{itemName},{oldPrice-newPrice}')
    for itemName in itemsOnlyInOldList:
        result_file.write( f'\n{itemName},Removed')
    for itemName in itemsOnlyInNewList:
        result_file.write( f'\n{itemName},Added')   

# Close files
old_file.close()
new_file.close()
result_file.close()

# Present result file
if (TestMode != True)*(remoteUser != True):
    os.startfile ('Result.csv')
print("Saved in Result.csv")   

logging.info('done')  
