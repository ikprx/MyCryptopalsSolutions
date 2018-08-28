from s1c02 import xor
import binascii
def repkeyxor(s,k):
    return xor(s,k*len(s))

if __name__ == "__main__":
    text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    res = repkeyxor(text,b'ICE')
    print(binascii.hexlify(res))

