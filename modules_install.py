#!/usr/bin/python
import sys
import subprocess

install_dirc_name = sys.argv[1]
print "\033[1m"'Dowload custom cmake modules, move to '+install_dirc_name+'/Modules' "\033[0m"
subprocess.call('git clone https://github.com/hshi/Modules', shell=True)
subprocess.call('rm -rf '+install_dirc_name+'/Modules', shell=True)
subprocess.call('mkdir '+install_dirc_name+'/Modules', shell=True)
subprocess.call('cp -r Modules '+install_dirc_name, shell=True)
