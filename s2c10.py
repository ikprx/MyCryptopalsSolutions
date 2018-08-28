import base64
from s1c07 import aes_decrypt_ecb, aes_encrypt_ecb
from s1c06 import breaktoblocks
from s1c02 import xor
from s2c09 import pkcs7pad 

def aes_decrypt_cbc(txt,key,iv):
    plaintext = bytearray() 

    blocks = breaktoblocks(txt,16)
    prev_block = iv
    for block in blocks:
        currentplaintext = xor( aes_decrypt_ecb(block,key), prev_block)
        prev_block = block
        plaintext += currentplaintext
    return bytes(plaintext)

def aes_encrypt_cbc(txt,key,iv):
    ciphers = bytearray()
    
    blocks = breaktoblocks(pkcs7pad(txt,16),16)
    prev_block = iv

    for block in blocks:
        currentcipher = aes_encrypt_ecb(xor(block,prev_block),key) 
        prev_block = currentcipher
        ciphers += currentcipher

    return bytes(ciphers)

def main():
    key = bytes("YELLOW SUBMARINE".encode('ascii'))
    iv = bytes(16)
    
    f = base64.b64decode("".join((open("10.txt","r").readlines())))

    i =(aes_decrypt_cbc(f,key,iv))
    o = (aes_encrypt_cbc(i,key,iv))
    i2  = (aes_decrypt_cbc(o,key,iv))
    print(i2)
    

if __name__ == "__main__":
    main()
