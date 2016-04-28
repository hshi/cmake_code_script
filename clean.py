#!/usr/bin/python
import sys
import os
import subprocess
import glob

#Remove directories
subprocess.call('rm -rf `ls -1 -d */`', shell=True)  
