#! /usr/bin/python3
import os
import sys

# Get current working directory and save it to variable as string
currentDir = str(os.getcwd())
os.system('clear')

def showHelp():
    """
    Show useful information about how to use the script
    """
    return """
            Sort is a simple program that lets you sort files into specific folders or archives based on their file extension

            Usage:

            Compress files of a specific extension into an archive
            sort -c <extension>

            Compress files at a specific directory into an archive
            sort -c <extension> <directory>
            

            Move files of a specific extension into a folder
            sort -f <extension>

            Move files of a specific extension on a specified directory into a folder
            sort -f <extension> <directory>
           """

def compressFiles(ext, dir):
    """
    Looks for files at the specified directory and then compresses
    the files into an archive.

    If the directory has not been specified then it'll default to
    using the current working directory
    """


def moveTo(ext, fromDir, toDir):
    """
    Looks for files at the specified directory and then moves them
    to a new folder that's named using the extension.
    """
    os.system(f"cd {fromDir}")
    os.system(f"pwd")
    os.system(f"mkdir {toDir}")

    moveMsg(ext)

    # Move files to the directory
    os.system(f"mv {fromDir}/*.{ext} {toDir}")
    

def sortingMsg(ext):
    print(f"Sorting {ext} files...")

def moveMsg(ext):
    print(f"Moving {ext} files...")


def getExt():
    """
    This function gets the extension of the files that you want to 
    work with
    """
    return str(input("Enter file extension: "))
    
def main(arguments):
    options = []
    operation = ""
    if(len(arguments) > 1):

        operation = arguments[1]
        
        for option in arguments:
            
            if not "FileSort" in option and not "-" in option:
                options.append(option)
    

    if (operation == "-f"):
        moveTo(options[0], options[1], options[2])
            
    return ""
    



if __name__ == "__main__":
    main(sys.argv)