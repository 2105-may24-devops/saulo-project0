# AES 256 encryption/decryption using pycrypto library
import base64
from types import DynamicClassAttribute
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
 
password = input("Enter encryption password: ")

def extend(data , length_of_blocks):
    extended = length_of_blocks - len(data) % length_of_blocks
    extended = extended * chr(length_of_blocks - len(data) % length_of_blocks)
    extended = data + extended
    return extended

def unextend(data):
    unextended =  data[:-ord(data[len(data) - 1:])]
    return unextended
 
 
def encrypt(raw, password):
    length_of_blocks = 16
#    password = input("Enter encryption password: ")
    salt = b"this is a salt."
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    private_key =key

    data = raw
    extended = length_of_blocks - len(data) % length_of_blocks
    extended = extended * chr(length_of_blocks - len(data) % length_of_blocks)
    extended = data + extended

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(extended))
 
 
def decrypt(enc, password):
    length_of_blocks = 16
 #   password = input("Enter encryption password: ")
    salt = b"this is a salt."
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    private_key = key
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    data = cipher.decrypt(enc[16:])
    unextended =  data[:-ord(data[len(data) - 1:])]
    return unextended
 
 
# First let us encrypt secret message
encrypted = encrypt("This is a secret message", password)
print(encrypted)
 
# Let us decrypt using our original password
decrypted = decrypt(encrypted, password)
print(bytes.decode(decrypted))
