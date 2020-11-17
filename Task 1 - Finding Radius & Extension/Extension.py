import sys
import os

File_Name = input("  Enter File Name or Extension to Look Up for Extension Type   : ")
File_Path = os.path.join(os.path.dirname(__file__), "Extensions.txt")

def Filter(Data):
    i=0
    for Char in Data:
        if(Char == '['):
            return Data[:i]
        i += 1
    return Data

def Extension_Extract(Data):
    i=0
    for Char in Data:
        if(Char == '.'):
            return Data[i+1:]
        i += 1
    return Data


with open(File_Path, "r") as Ext_File:
    Extensions = Ext_File.readlines()

    for Extension in Extensions:
        Extension = Extension.split("\t")
        Extension[0] = Filter(Extension[0])

        if Extension_Extract(File_Name).lower() == Extension[0].lower():
            print("   Description  : " + Extension[1])
            sys.exit()

    print(" Sorry, Extension not Available in Database :(")