import binascii
from s1c02 import xor


def enscore(s):
    res = 0

    letters = {
        " "     :40000,
        "E" 	:21912,
        "T" 	:16587,
        "A" 	:14810,
        "O" 	:14003,
        "I" 	:13318,
        "N" 	:12666,
        "S" 	:11450,
        "R" 	:10977,  	
        "H" 	:10795,  	
        "D" 	:7874,  	
        "L" 	:7253,  	
        "U" 	:5246,  	
        "C" 	:4943,  	
        "M" 	:4761,  	
        "F" 	:4200,  	
        "Y" 	:3853,  	
        "W" 	:3819,  	
        "G" 	:3693,
        "P" 	:3316,
        "B" 	:2715,
        "V" 	:2019,
        "K" 	:1257,  	
        "X" 	:315,
        "Q" 	:205,  	
        "J" 	:188,  	
        "Z" 	:128
    }	  	 
   
    
    for c in s:
        if chr(c) in letters.keys():
            res += letters[chr(c)]
        elif chr(c).upper() in letters.keys():
            res += letters[chr(c).upper()]
        else:
            res += 0
    return res 


def sbytexor(s):
    bestKey = {
        "xorbyte" : bytes(0),
        "score" : 0,
        "msgResult" : ""
    }
    for byte in range(0,255):
       currentKey = {
           "xorbyte" : bytes(0),
           "score" : 0,
           "msgResult" : ""
       }
       xored= xor(s, len(s) * [byte]) 
       currentKey['xorbyte'] = byte 
       currentKey['msgResult'] = xor(s, len(s) * [currentKey['xorbyte']]) 
       currentKey['score'] = int(enscore(xored))
       if bestKey['score'] < currentKey['score']:
           bestKey = currentKey

    return bestKey

       
if __name__ == "__main__":
    sHexed = binascii.unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    print(sbytexor(sHexed))


