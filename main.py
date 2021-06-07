import sys
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pathlib import *

#checks to make sure the correct number of parameters have been used when running this program.
#program expects at least 3 parameters, except when the -h flag is used. In that case it expects 2.
def check_params(numb_args):
    if numb_args == 3:
        return True
    elif numb_args < 2 :
        print("Incorrect arguments. Correct ussage: py main.py <-flag> <file name or path to file>")
        return False
    elif numb_args == 2 and  sys.argv[1]== "-h":
        print("<REPLACE ME> with a print out of the instructions on how to use this program and all the flag options.")
        return False
    else:
        print("Incorrect arguments. Correct ussage: py main.py <-flag> <file name or path to file>")
        return False

def password_rules():
    password = input("Enter password: \n")

    while len(password) < 8:
        print("Passwords must be atleast 8 characters long. Please try again.")
        password = input("Enter password: \n")

    confirmPass = input("Enter password again to confirm: \n") 

    while password != confirmPass:
        print("Passwords did not match. Please try again.")
        password = input("Enter password: \n")

        while len(password) < 8:
            print("Passwords must be atleast 8 characters long. Please try again.")
            password = input("Enter password: \n")

        confirmPass = input("Enter password again to confirm: \n") 

    return password


def aes_encrypt(file_path):
    pass

def fernet_encrypt(file_path):
    password = password_rules()
    password = str.encode(password)
    baseSalt = b'\xbf\xe2\xd1\xaf\xbc\xb1\xdd\x82\xe2\xaf\xbc\xdd\x27\xd9\x82\xbf\x61\x62'
    userSalt = input("Enter salt value: \n")
    userSalt = str.encode(userSalt)
    finalSalt = userSalt + baseSalt
    over_write_or_new = input("Enter the word: <new> to create an encripted copy of the file or enter the word: <overwrite> to overwrite the original file with the encripted one. \n")

    while ((over_write_or_new != "new") and (over_write_or_new != "<new>") and (over_write_or_new != "overwrite") and (over_write_or_new != "<overwrite>")):
        print("Incorrect user input.")
        over_write_or_new = input("Enter the word: <new>  to create an encripted copy of the file or enter the word: <overwrite> to overwrite the original file with the encripted one. \n")

    if(over_write_or_new == "new") or (over_write_or_new == "<new>"):
        new_encrypted_file_name = input("Enter the name of newly encripted file that will be created: \n" )

    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=finalSalt,
            iterations=200000,
            backend=None
            )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    encrypt_fernet = Fernet(key)

    p_file_path = Path(file_path)

    with p_file_path.open('rb') as file:
        unencrypted_file = file.read()

    encrypted_file = encrypt_fernet.encrypt(unencrypted_file)

    if(over_write_or_new == "new") or (over_write_or_new == "<new>"):
        p_new = Path(new_encrypted_file_name)
        with p_new.open('wb') as new_file:
            new_file.write(encrypted_file)
    elif(over_write_or_new == "overwrite") or (over_write_or_new == "<overwrite>"):
        with p_file_path.open('wb') as new_file:
            new_file.write(encrypted_file)
    else:
        exit(1)

    print("File successfuly encrypted.")



def nsa_encrypt(file_path):
    pass

def encrypt(file_path):
    encryptionType = input("How would you like your file to be encrypted? (options are: aes256, fernet, nsa): \n")

    while ((encryptionType != "aes256") and (encryptionType != "fernet") and (encryptionType != "nsa") ):
        print("Incorrect user input.")
        encryptionType = input("How would you like your file to be encrypted? (options are: aes256, fernet, nsa): \n")

    if(encryptionType == "aes256"):
        aes_encrypt(file_path)

    if(encryptionType == "fernet"):
        fernet_encrypt(file_path)

    if(encryptionType == "fernet"):
        nsa_encrypt(file_path)

def aes_decrypt(file_path):
    pass

def fernet_decrypt(file_path):
    password = password_rules()
    password = str.encode(password)
    baseSalt = b'\xbf\xe2\xd1\xaf\xbc\xb1\xdd\x82\xe2\xaf\xbc\xdd\x27\xd9\x82\xbf\x61\x62'
    userSalt = input("Enter salt value: \n")
    userSalt = str.encode(userSalt)
    finalSalt = userSalt + baseSalt

    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=finalSalt,
            iterations=200000,
            backend=None
            )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    decrypt_fernet = Fernet(key)

    p_file_path = Path(file_path)

    with p_file_path.open('rb') as file:
        encrypted_file = file.read()

    decrypted_file = decrypt_fernet.decrypt(encrypted_file)

    with p_file_path.open('wb') as new_file:
        new_file.write(decrypted_file)

    print("File successfuly decrypted.")




def nsa_decrypt(file_path):
    pass


def decrypt(file_path):
    decryptionType = input("What was the file encrypted with? (options are: aes256, fernet, nsa): \n")

    while ((decryptionType != "aes256") and (decryptionType != "fernet") and (decryptionType != "nsa") ):
        print("Incorrect user input.")
        decryptionType = input("What was the file encrypted with? (options are: aes256, fernet, nsa): \n")

    if(decryptionType == "aes256"):
        aes_decrypt(file_path)

    if(decryptionType == "fernet"):
        fernet_decrypt(file_path)

    if(decryptionType == "fernet"):
        nsa_decrypt(file_path)


def send_file(file_path):
    pass


def change_pass(file_path):
    pass


def help_info():
    pass


def recieve_file(file_path):
    pass


def destroy_file(file_path):
    pass


def move_file(file_path):
    pass


def check_if_file_exists(flag, file_path):
    print(file_path)
    if( flag != "-h"):
        my_file = Path(file_path)
        if my_file.is_file():
            pass
        else:
            print("ERROR: Could not find file.")
            exit(1)


def arguments(flag, file_path):
    if( flag == "-e"):
        encrypt(file_path)
    if( flag == "-d"):
        decrypt(file_path)
    if( flag == "-s"):
        send_file(file_path)
    if( flag == "-c"):
        change_pass(file_path)
    if( flag == "-h"):
        help_info()
    if( flag == "-destroy"):
        destroy_file(file_path)
    if( flag == "-r"):
        recieve_file(file_path)
    if( flag == "-m"):
        move_file(file_path)

def main():
    if check_params(len(sys.argv)):
        check_if_file_exists(sys.argv[1], sys.argv[2])
        arguments(sys.argv[1], sys.argv[2])
    else:
        exit(1)


if __name__ == "__main__":
    main()