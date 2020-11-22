import sys
import os

File_Name = input("  Enter File Name or Extension to Look Up for Extension Type   : ")
File_Path = os.path.join(os.path.dirname(__file__), "Extensions.txt")

def Filter(Data):
    """
      Data is taken from Wikipedia, which consists of Quotation also, which Hardens identification of an Extension.
      So, that part is removed in this function, by considering the string before '['

      It expects String as its Argument

      It returns the String before '[' character and if this character is not present, then it returns entire String.
    """
    i=0
    for Char in Data:
        if(Char == '['):
            return Data[:i]
        i += 1
    return Data

def Extension_Extract(Data):
    """
      This Function is used to Select, Extension part of a file, so it considers/returns the String
       after '.' character. If '.' character is not present, then the function assumes that 
       entire string itself is extension, so it returns that String.

      It expects a String as Argument and also returns a String as mentioned earlier. 
    """
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

        if Extension_Extract(File_Name).casefold() == Extension[0].casefold():
            print("   Description  : " + Extension[1])
            sys.exit()

    print(" Sorry, Extension not Available in Database :(")
