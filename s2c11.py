from s1c06 import breaktoblocks
from os import urandom
from s1c07 import aes_encrypt_ecb
from s2c10 import aes_encrypt_cbc
from random import randint
from s2c09 import pkcs7pad 


def encryption_oracle(x):
    key = urandom(16)
    iv = urandom(16)
    if(randint(0,1)):
        print("->ECB")
        return aes_encrypt_ecb(pkcs7pad(x,16),key)
    else:
        print("->CBC")
        return aes_encrypt_cbc(x,key,iv)

def isecb(x):
    blocks = breaktoblocks(x,16)

    for block in blocks:
        if x.count(block) > 1:
            return True
    return False


def main():
    toenc = bytes(("X"*43).encode('ascii'))

    found = False
    while not found :
        encrypted = encryption_oracle(toenc)
        if(isecb(encrypted)):
            found = True
            print("ECB detected")
        print("#"*10)
if __name__ == "__main__":
    main()