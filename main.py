import sys
import pathlib

#current_path = os.path.abspath('.')
#parent_path = os.path.dirname(current_path)
#sys.path.append(parent_path)

def checkParams():
    if len(sys.argv) == 3:
        return True
    else:
        print("Incorrect parameters. Correct ussage: main.py <-flag> <file name or path to file>")
        return False

def encrypt():
    pass


def decrypt():
    pass


def sendFile():
    pass


def changePass():
    pass


def helpInfo():
    pass

def recieveFile():
    pass

def firstArgument(flag):
    if( flag == "-e"):
        encrypt()
    if( flag == "-d"):
        decrypt()
    if( flag == "-s"):
        sendFile()
    if( flag == "-c"):
        changePass()
    if( flag == "-h"):
        helpInfo()
    if( flag == "-r"):
        recieveFile()


#from functions.py import checkParams

def main():
    if checkParams():
        print ("correct inputs")
        firstArgument(sys.argv[1])
    else:
        print ("incorrect inputs")


if __name__ == "__main__":
    main()