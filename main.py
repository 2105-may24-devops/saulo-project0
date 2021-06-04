import sys
import pathlib

#current_path = os.path.abspath('.')
#parent_path = os.path.dirname(current_path)
#sys.path.append(parent_path)

def check_params():
    if len(sys.argv) == 3:
        return True
    else:
        print("Incorrect parameters. Correct ussage: main.py <-flag> <file name or path to file>")
        return False

def encrypt():
    pass


def decrypt():
    pass


def send_file():
    pass


def change_pass():
    pass


def help_info():
    pass

def recieve_file():
    pass

def first_argument(flag):
    if( flag == "-e"):
        encrypt()
    if( flag == "-d"):
        decrypt()
    if( flag == "-s"):
        send_file()
    if( flag == "-c"):
        change_pass()
    if( flag == "-h"):
        help_info()
    if( flag == "-r"):
        recieve_file()


#from functions.py import check_params

def main():
    if check_params():
        print ("correct inputs")
        first_argument(sys.argv[1])
    else:
        print ("incorrect inputs")


if __name__ == "__main__":
    main()