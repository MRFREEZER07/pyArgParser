#! /bin/python3
import sys
from Argparser import Argparser


a= Argparser(sys.argv)


if(a.hasOptions(['-h','--help'])):
    a.printHelp("help")


"""
WORKS LIKE --proxy=true
"""

if(a.hasOptions(['--proxy','-p'])): 
    answerr =a.getOptionValue('-p') or a.getOptionValue("--proxy")
    print(answerr)
else:
    print("not worked")

if(a.hasOptions(['-f','--file'])):
    fileName = a.getOptionValue('-f') or a.getOptionValue('--file')
    print(fileName)