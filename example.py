#! /bin/python3
import sys
import os
from lib.Argument import Argument 
import json

a= Argument(sys.argv)



if(a.hasOptions(['-h','--help'])):
    a.printHelp("help")


"""
WORKS LIKE --proxy=true
"""

if(a.hasOptions(['--proxy','-p'])): 
    if a.getOptionValue('--proxy') or a.getOptionValue('-p'):
        print("implemented")
    else:
        print("not worked")