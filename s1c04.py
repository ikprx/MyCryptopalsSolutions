from s1c03 import sbytexor
import binascii

def singleCharXor(lines):
    bestKey = {
        "xorbyte" : bytes(0),
        "score" : 0,
        "msgResult" : ""
    }
    for line in lines:
        nline = binascii.unhexlify(line.replace('\n',''))
        currentKey= sbytexor(nline)
        if bestKey['score'] < currentKey['score']:
            bestKey = currentKey
    return bestKey


if __name__ == "__main__":
    print(singleCharXor(open("4.txt","r").readlines()))
