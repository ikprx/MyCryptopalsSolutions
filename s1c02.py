import binascii

def xor(s1,s2):
    return bytes([  l1^l2 for l1,l2 in zip(s1,s2)])

if __name__ == "__main__":
    s1 = binascii.unhexlify("1c0111001f010100061a024b53535009181c") 
    s2 = binascii.unhexlify("686974207468652062756c6c277320657965") 
    print(binascii.hexlify(xor(s1,s2)))
