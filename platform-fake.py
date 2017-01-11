#!/usr/bin/python
import shutil
import signal
import sys
import __main__ as main
import os

FileScriptName = main.__file__ # Featch name of file
from os.path import basename # get basename 
FileScriptsArrayName = os.path.basename(FileScriptName)
inventoryArray = (os.path.splitext(FileScriptsArrayName)[0]) #get only name 
Inventory = inventoryArray.split('-',1)[0] # get only env from before "-" openstack or ec2 

def signal_handler(signal, frame):
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

if not inventoryArray in ["openstack-fake", "ec2-fake"]:
   print "script should not name in this way, please change to \'platform\'-fake.py"
   exit(1);


InventoryBakName = Inventory + "-fake.bak"

#print FileScriptsArrayName

InventoryBak = os.path.abspath(InventoryBakName)

InventoryOrg=os.path.abspath(Inventory+'.py')

#print InventoryBak


if not os.path.exists(InventoryBak): #Check if InventoryBak exist 
    while True:
        user_input = raw_input('there is no backup output create it y/n ? :')
        if user_input in ['y', 'n']:
            break
        else:
            print('That is not a valid option!')

    if user_input in ['y','Y']: 
      if os.path.exists(InventoryOrg):
         print "running " + InventoryOrg + " --list > "+ InventoryBak #Inform user 
         result = os.system(InventoryOrg + " --list > "+ InventoryBak) # create fake inventory
         if result: # if different then 0 false, clean 
            print "failed to run, remove " + InventoryBak 
            os.system("rm " + InventoryBak)
         else: # if answer is 0 then success 
            print "command succesfull"

      else:
         print('File '+ InventoryOrg + ' not exist, you can make backup manualy by')
         print InventoryOrg + " --list > " + InventoryBak
         exit(0)

else: #File InventoryBakexist show output
   with open(InventoryBak, 'r') as fin:
         print fin.read()
