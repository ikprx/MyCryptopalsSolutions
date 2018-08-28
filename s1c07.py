import base64
from Crypto.Cipher import AES

def aes_encrypt_ecb(t,key):
    cipher = AES.new(key,AES.MODE_ECB)
    return cipher.encrypt(t)

def aes_decrypt_ecb(t,key):
    cipher = AES.new(key,AES.MODE_ECB)
    return cipher.decrypt(t)

if __name__ == "__main__":
    key = "YELLOW SUBMARINE"
    text =base64.b64decode("".join([ line.replace('\n','') for line in open("7.txt","r").readlines()])) 
    print(aes_decrypt_ecb(text,key))
