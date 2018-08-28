from s1c05 import repkeyxor
from s1c03 import enscore,sbytexor
from s1c02 import xor
import base64

def hd(s1, s2):
    return "".join([ bin(l) for l in xor(s1,s2)]).count("1")

def getKeysize(s):
    keysizes = []
    for keysize in range(2,40):
        currentkeysize = {
                "hd": float(0),
                "keysize": 0 
        }
        
        b1 = s[:keysize]
        b2 = s[keysize:2*keysize]
        b3 = s[2*keysize:3*keysize]
        b4 = s[3*keysize:4*keysize]

        currentkeysize['hd'] = float(hd(b1,b2) + hd(b2,b3) + hd(b3,b4)) / float(3*keysize)
        currentkeysize['keysize'] = keysize
        keysizes.append(currentkeysize)
    return sorted(keysizes,key=lambda elem:elem['hd'],reverse=False)[:3]

def breaktoblocks(s,bs):
    blocks = []
    for x in range(0,len(s),bs):    
        blocks.append(s[x:x+bs])
    return blocks

def transpose(blocks):
    transposed = []
    for byteID in range(0,len(blocks[0])):
        currentblock = []
        for rowID in range(0,len(blocks)):
            if len(blocks[rowID]) > byteID:
                currentblock.append(blocks[rowID][byteID])
        transposed.append(currentblock)
    return transposed

def getkey(s):
    keys = []
    keysizes = getKeysize(s)
    for keysize in keysizes:
        key = bytearray()
        blocks = transpose(breaktoblocks(s,keysize['keysize']))
        for block in blocks:
            key.append(sbytexor(block)['xorbyte'])
        keys.append(bytes(key))
    return keys 

def brepkeyxor(s):
    keys = getkey(s)
    results = []
    for key in keys:
        currentres = {
            "msg" : bytes(),
            "key" : bytes(),
            "score" : 0
        }
        xored = repkeyxor(s,key)
        currentres['msg'] = xored
        currentres['score'] = enscore(xored)
        currentres['key'] = key
        results.append(currentres)

    return sorted(results,key=lambda elem:elem['score'],reverse=True)[0] 


if __name__ == "__main__":
    res = brepkeyxor(base64.b64decode("".join([ line.replace("/n","") for line in open("6.txt","r")])))
    print(("Key:\n%s\n\n\n")%(res['key']))
    print(("Text:\n%s")%(res['msg']))
