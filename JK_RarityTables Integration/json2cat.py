# Use python 3.7.4 or later
import json
import os.path

# Constants
MECH_PATH = "mech_all"

# Global vars
lMechList = []


# get file list from bash
if os.path.exists(MECH_PATH):
    os.chdir(MECH_PATH)

    lMechList = os.listdir(".")        
else:
    print ("No such path")
    exit

# run on list
for mech in lMechList:
   pass 


# function to create new file / append to existing
def fCatFiles(strTag, strMech):
    pass

# function that parses the tags to get the target file name
def fJsonStuff(strMech):
    pass
