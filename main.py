import sys
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import kdf
from cryptography.hazmat.primitives.kdf import KeyDerivationFunction
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pathlib import *

#checks to make sure the correct number of parameters have been used when running this program.
#program expects at least 3 parameters, except when the -h flag is used. In that case it expects 2.
def check_params(numbArgs,firstArg):
    if numbArgs == 3:
        return True
    elif numbArgs == 2 and  firstArg == "-h":
        print("<REPLACE ME> with a print out of the instructions on how to use this program and all the flag options.")
        return False
    else:
        print("Incorrect arguments. Correct ussage: py main.py <-flag> <file name or path to file>")
        return False

def password_rules():
    password = input("Enter password: ")

    while len(password) < 8:
        print("Passwords must be atleast 8 characters long. Please try again.")
        password = input("Enter password: ")

    confirmPass = input("Enter password again to confirm: ") 

    while password != confirmPass:
        print("Passwords did not match. Please try again.")
        password = input("Enter password: ")

        while len(password) < 8:
            print("Passwords must be atleast 8 characters long. Please try again.")
            password = input("Enter password: ")

        confirmPass = input("Enter password again to confirm: ") 

    return password


def aes_encrypt(filePath):
    pass

def fernet_encrypt(filePath):
    password = password_rules()
    baseSalt = b'\xbf\xe2\xd1\xaf\xbc\xb1\xdd\x82\xe2\xaf\xbc\xdd\x27\xd9\x82\xbf\x61\x62'
    userSalt = input("Enter salt value:")
    userSalt = str.encode(userSalt)
    finalSalt = userSalt + baseSalt
    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=finalSalt,
            iterations=200000,
            )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    token = f.encrypt(b"Secret message!")

def nsa_encrypt(filePath):
    pass

def encrypt(filePath):
    encryptionType = input("How would you like your file to be encrypted? (options are: aes256, fernet, nsa)")

    if(encryptionType == "aes256"):
        aes_encrypt(filePath)

    if(encryptionType == "fernet"):
        fernet_encrypt(filePath)

    if(encryptionType == "fernet"):
        nsa_encrypt(filePath)


def decrypt(filePath):
    pass


def send_file(filePath):
    pass


def change_pass(filePath):
    pass


def help_info():
    pass

def recieve_file(filePath):
    pass

def destroy_file(filePath):
    pass

def arguments(flag, filePath):
    if( flag == "-e"):
        encrypt(filePath)
    if( flag == "-d"):
        decrypt(filePath)
    if( flag == "-s"):
        send_file(filePath)
    if( flag == "-c"):
        change_pass(filePath)
    if( flag == "-h"):
        help_info()
    if( flag == "-destroy"):
        destroy_file(filePath)
    if( flag == "-r"):
        recieve_file(filePath)

def main():
    if check_params(len(sys.argv), sys.argv[1]):
        print ("correct inputs")
        arguments(sys.argv[1], sys.argv[2])
    else:
        pass


if __name__ == "__main__":
    main()