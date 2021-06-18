import sys
import os
import base64
from pathlib import *

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
except ModuleNotFoundError:
    print("ERROR: cyptography module not found.")
    exit(1)

try:
    from stegano import lsbset
    from stegano import lsb
except ModuleNotFoundError:
    print("ERROR: stegano module not found.")
    exit(1)




#checks to make sure the correct number of parameters have been used when running this program.
#program expects at least 3 parameters, except when the -h flag is used. In that case it expects 2.
def check_params(numb_args):
    if numb_args == 3:
        return True
    elif numb_args < 2 :
        print("Incorrect arguments. Correct ussage: py main.py <-flag> <file name or path to file>")
        return False
    elif numb_args >= 6 :
        return True
    elif numb_args == 2 and  sys.argv[1]== "-h":
        print("<REPLACE ME> with a print out of the instructions on how to use this program and all the flag options.")
        return False
    elif numb_args == 5 and  sys.argv[1]== "-se":
        return True
    elif numb_args == 4 and  sys.argv[1]== "-sd":
        return True
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
        p_new = Path(new_encrypted_file_name)
        path_without_file_name = p_new.parent
        while(path_without_file_name.is_dir() == False):
            make_new_file_path = input("File path was not found. Enter <new> to create that path or enter <try> to enter an existing path. \n")
            if(make_new_file_path == "new" or make_new_file_path == "<new>"):
                path_without_file_name.mkdir(parents=True, exist_ok=True)
            elif(make_new_file_path == "try" or make_new_file_path == "<try>"):
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
        path_without_file_name = p_new.parent
        if path_without_file_name.is_dir():
            try:
                with p_new.open('wb') as new_file:
                    new_file.write(encrypted_file)
            except:
                print("ERROR: writing the file: " + str(p_new))
        else:
            pwd = Path(os.getcwd())
            absolute_path = pwd / path_without_file_name
            print("The file path: "+ str(absolute_path) +" has not been found.")
            exit(1)
    elif(over_write_or_new == "overwrite") or (over_write_or_new == "<overwrite>"):
        try:
            with p_file_path.open('wb') as new_file:
                new_file.write(encrypted_file)
        except:
            print("ERROR: writing the file: " + str(p_file_path))
            exit(1)
    else:
        exit(1)

    print("File successfuly encrypted.")

def fernet_encrypt_noninterractive(file_path):
    password = sys.argv[4]
    password = str.encode(password)
    baseSalt = b'\xbf\xe2\xd1\xaf\xbc\xb1\xdd\x82\xe2\xaf\xbc\xdd\x27\xd9\x82\xbf\x61\x62'
    userSalt = sys.argv[5]
    userSalt = str.encode(userSalt)
    finalSalt = userSalt + baseSalt
    over_write_or_new = "overwrite"

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

    try:
        with p_file_path.open('rb') as file:
            unencrypted_file = file.read()
    except:
        print("ERROR: reading the file: " + str(p_file_path))
        exit(1)

    encrypted_file = encrypt_fernet.encrypt(unencrypted_file)
    try:
        with p_file_path.open('wb') as new_file:
                new_file.write(encrypted_file)
    except:
        print("ERROR: writing the file: " + str(p_file_path))
        exit(1)

    print("File successfuly encrypted.")

def nsa_encrypt(file_path):
    fernet_encrypt(file_path)

def aes_encrypt(file_path):
    fernet_encrypt(file_path)

def aes_encrypt_noninterractive(file_path):
    fernet_encrypt_noninterractive(file_path)

def nsa_encrypt_noninterractive(file_path):
    fernet_encrypt_noninterractive(file_path)

def encrypt(file_path):
    if(len(sys.argv) >= 6 and sys.argv[3] == "fernet" ):
            fernet_encrypt_noninterractive(file_path)
    elif(len(sys.argv) >= 6 and sys.argv[3] == "aes256" ):
            aes_encrypt_noninterractive(file_path)
    elif(len(sys.argv) >= 6 and sys.argv[3] == "nsa" ):
            nsa_encrypt_noninterractive(file_path)
    else:
        encryptionType = input("How would you like your file to be encrypted? (options are: aes256, fernet, nsa): \n")

        while ((encryptionType != "aes256") and (encryptionType != "fernet") and (encryptionType != "nsa") ):
            print("Incorrect user input.")
            encryptionType = input("How would you like your file to be encrypted? (options are: aes256, fernet, nsa): \n")

        if(encryptionType == "aes256"):
            aes_encrypt(file_path)

        if(encryptionType == "fernet"):
            if(len(sys.argv) > 6):
                fernet_encrypt_noninterractive(file_path)
            else:
                fernet_encrypt(file_path)

        if(encryptionType == "nsa"):
            nsa_encrypt(file_path)


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

    try:
        with p_file_path.open('rb') as file:
            encrypted_file = file.read()
    except:
        print("ERROR: reading the file: " + str(p_file_path))
        exit(1)

    decrypted_file = decrypt_fernet.decrypt(encrypted_file)

    try:
        with p_file_path.open('wb') as new_file:
            new_file.write(decrypted_file)
    except:
        print("ERROR: writing the file: " + str(p_file_path))
        exit(1)

    print("File successfuly decrypted.")

def fernet_decrypt_noninterractive(file_path):
    password = sys.argv[4]
    password = str.encode(password)
    baseSalt = b'\xbf\xe2\xd1\xaf\xbc\xb1\xdd\x82\xe2\xaf\xbc\xdd\x27\xd9\x82\xbf\x61\x62'
    userSalt = sys.argv[5]
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

    try:
        with p_file_path.open('rb') as file:
            encrypted_file = file.read()
    except:
        print("ERROR: reading the file: " + str(p_file_path))
        exit(1)

    decrypted_file = decrypt_fernet.decrypt(encrypted_file)

    try:
        with p_file_path.open('wb') as new_file:
            new_file.write(decrypted_file)
    except:
        print("ERROR: writing the file: " + str(p_file_path))
        exit(1)

    print("File successfuly decrypted.")


def nsa_decrypt(file_path):
    fernet_decrypt(file_path)

def aes_decrypt(file_path):
    fernet_decrypt(file_path)

def aes_decrypt_noninterractive(file_path):
    fernet_decrypt_noninterractive(file_path)

def nsa_decrypt_noninterractive(file_path):
    fernet_decrypt_noninterractive(file_path)


def decrypt(file_path):
    if(len(sys.argv) >= 6 and sys.argv[3] == "fernet"):
        fernet_decrypt_noninterractive(file_path)
    elif(len(sys.argv) >= 6 and sys.argv[3] == "aes256"):
        aes_decrypt_noninterractive(file_path)
    elif(len(sys.argv) >= 6 and sys.argv[3] == "nsa"):
        nsa_decrypt_noninterractive(file_path)
    else:
        decryptionType = input("What was the file encrypted with? (options are: aes256, fernet, nsa): \n")

        while ((decryptionType != "aes256") and (decryptionType != "fernet") and (decryptionType != "nsa") ):
            print("Incorrect user input.")
            decryptionType = input("What was the file encrypted with? (options are: aes256, fernet, nsa): \n")

        if(decryptionType == "aes256"):
            aes_decrypt(file_path)

        if(decryptionType == "fernet"):
            if(len(sys.argv) >= 6):
                fernet_decrypt_noninterractive(file_path)
            else:
                fernet_decrypt(file_path)

        if(decryptionType == "nsa"):
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


def stenography_encrypt(file_path):
    pwd = Path(os.getcwd())
    p_new = Path(file_path)
    image =  Path(sys.argv[3])
    destination =  Path(sys.argv[4])
    parent_destination  = destination.parent
    abs_destination = pwd / destination
    parent_image = image.parent
    abs_image = pwd / image
    parent_path = p_new.parent
    abs_path = pwd / p_new
    if (p_new.is_file() and image.is_file()):
        try:
            with p_new.open('rb') as new_file:
                file_to_hide = new_file.read()
        except:
            print("ERROR: reading the file: " + str(p_new))
            exit(1)
        secret = lsb.hide(str(image), str(file_to_hide))
        if(parent_destination.is_dir()):
            secret.save(str(destination))
        else:
             print("ERROR: could not find directory: " + str(parent_destination))
    else:
        print("ERROR: reading the file: " + str(image))
        exit(1)
        

def stenography_decrypt(file_path):
    pwd = Path(os.getcwd())
    image =  Path(file_path)
    image_path = image.parent
    abs_image = pwd / image
    destination =  Path(sys.argv[3])
    parent_destination  = destination.parent
    abs_destination = pwd / destination
    if(parent_destination.is_dir()):
        clear_message = lsb.reveal(str(image))
   #    clear_message = str.encode(clear_message)
        try:
            with destination.open('wb') as new_file:
                new_file.write(clear_message)
        except:
            print("ERROR: writing the file: " + str(destination))
            exit(1)
    else:
             print("ERROR: could not find directory: " + str(parent_destination))
             exit(1)


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
    if( flag == "-se"):
        stenography_encrypt(file_path)
    if( flag == "-sd"):
        stenography_decrypt(file_path)
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
