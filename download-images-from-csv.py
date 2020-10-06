import sys
import urllib
import urllib.request
from csv import reader
import os.path
import os
import logging

csv_filename = "fp-freestanding-fridge.csv"
LOG_FILENAME = '404-errors.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.ERROR)

with open(csv_filename, 'r') as csv_file:
    n = 1  # starting point
    for line in reader(csv_file):
            tgt_folder = line[0] 
            if not os.path.exists(tgt_folder):
                os.makedirs(tgt_folder)
                n = 1  # restart n for new folder
            if line[1] != '' and line[0] != '': 
                filename = ''.join([line[0], '-', str(n), line[1][-4:]])
                destination = os.path.join(tgt_folder, filename)
            try:            
                urllib.request.urlretrieve(line[1], destination)
            except:
                print("404 error - Not found: {0}".format(line[1])) 
                logging.error("404 error - Not found {0}".format(line[1]))
            else:
                urllib.request.urlretrieve(line[1], destination)
                n += 1
                print("Image saved for {0}".format(line[1]))