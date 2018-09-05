from os import urandom
from s2c09 import pkcs7pad
from s1c07 import aes_encrypt_ecb
from s2c11 import isecb
import base64
from s1c06 import breaktoblocks

key =  urandom(16)
strenc = base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK") 

def encryption_oracle(append):
    return aes_encrypt_ecb(pkcs7pad(append+strenc,16),key)

def getbs():
    fenc = encryption_oracle(bytearray())

    a = bytearray()
    a.append(ord("A"))

    enc = encryption_oracle(a)

    while len(fenc) == len(enc):
        a.append(ord("A"))
        enc = encryption_oracle(a)

    return len(enc) - len(fenc)

def getTextLen():
    cnpad = len(encryption_oracle(bytearray()))
    ncnpad = cnpad
    i = 1
    while cnpad == ncnpad:
        ncnpad = len(encryption_oracle(bytearray(str("A"*i).encode('ascii'))))
        if ncnpad != cnpad:
            return ncnpad - 16 - i
        i+=1

def decryptbbb(bs):
    cipherlen = len(encryption_oracle(bytearray()))
    found = bytearray()
    textlen = getTextLen()
        
    while len(found) != textlen:
        padding = bytearray(str("A"*(cipherlen-len(found)-1)).encode('ascii'))
        enc = encryption_oracle(padding)[:cipherlen]
        for c in range(0,255):
            padding1 = bytearray(str("A"*(cipherlen-len(found)-1)).encode('ascii'))
            padding1 += found
            padding1.append(c)
            enc1 = encryption_oracle(padding1)[:cipherlen]
            if enc1 == enc:
                found.append(c)
    return found




def main():
    bs = getbs()
    ecb = isecb(encryption_oracle(bytearray(43)))
    if ecb:
        print(decryptbbb(bs).decode('ascii'))
        

if __name__ == "__main__":
    main()
