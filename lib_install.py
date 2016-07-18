#!/usr/bin/python
import sys
import os
import subprocess
import glob

typ               = sys.argv[1]
src_name          = sys.argv[2]
install_dirc_name = sys.argv[3]+'/'+typ

cwd_path    = os.getcwd()
script_path = os.path.abspath(os.path.dirname(__file__))

com='python '+ script_path+'/cmake.py ' + typ + "1.0"

subprocess.call('rm -rf build', shell=True)
subprocess.call('mkdir build', shell=True)
os.chdir('build')

src_path_list=glob.glob(cwd_path+'/'+src_name)
for src_path in src_path_list:
    subprocess.call('rm -rf *', shell=True)
    subprocess.call(com +' '+ src_path +' '+install_dirc_name, shell=True )
    subprocess.call('make', shell=True )
    subprocess.call('make install', shell=True )
    print "\n\n"

os.chdir('..')
subprocess.call('rm -rf build', shell=True)
