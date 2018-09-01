from os import urandom
from s2c09 import pkcs7pad
from s1c07 import aes_encrypt_ecb
from s2c11 import isecb
import base64
from s1c06 import breaktoblocks

key = urandom(16)
strenc = base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK") 

def encryption_oracle(i, append):
    return aes_encrypt_ecb(pkcs7pad(append+i,16),key)

def getbs(s):
    fenc = encryption_oracle(s,bytearray())

    a = bytearray()
    a.append(ord("A"))

    enc = encryption_oracle(s,a)

    while len(fenc) == len(enc):
        a.append(ord("A"))
        enc = encryption_oracle(s,a)

    return len(enc) - len(fenc)
def decryptbbb(s,bs):
    found = ""

    while len(found) <= bs:
        padding = bytearray(str("A"*(bs-len(found)-1)).encode('ascii'))
        encrypted = breaktoblocks(encryption_oracle(s,padding),16)[0]
        for ch in range(0, 255):
            padding1 = bytearray(str("A"*(bs-len(found)-1)+found).encode('ascii'))
            padding1.append(ch)
            encrypted1 = breaktoblocks(encryption_oracle(s,padding1),16)[0]
            if encrypted == encrypted1:
                found += chr(ch)
                break
    print(found)



def main():
    bs = getbs(strenc)
    ecb = isecb(encryption_oracle(strenc,bytearray(43)))
    if ecb:
        decryptbbb(strenc,bs)
        

if __name__ == "__main__":
    main()