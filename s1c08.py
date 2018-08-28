from s1c06 import breaktoblocks
def detectecb(text):
    
    res = {
        "ecb" : False,
        "text" : text,
        "repeated" : []
    }
    blocks = breaktoblocks(text,16)
    for block in blocks:
        if text.count(block) > 1 and block not in res['repeated']:
            res['repeated'].append(block) 
            res["ecb"]= True
    return res


if __name__ == "__main__":
    for block in open("8.txt","r").readlines():
        res = (detectecb(block.replace('\n','')))
        if res['ecb'] == True:
            print(res['text'])
            print(res['repeated'])

        
