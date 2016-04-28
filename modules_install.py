#!/usr/bin/python
import sys
import os
import subprocess
import glob

install_dirc_name = sys.argv[1]

print "\033[1m" "Download custom cmake modules, move to "+install_dirc_name+"/Modules." "\033[0m"
str = raw_input("To comfirm, input 'Y':")

if str=='Y':
   subprocess.call('git clone https://github.com/hshi/Modules', shell=True)
   subprocess.call('rm -rf '+install_dirc_name+'/Modules', shell=True)
   subprocess.call('cp -r Modules '+install_dirc_name, shell=True)
else:
   print "Do not installed."
