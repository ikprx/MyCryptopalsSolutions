
def pkcs7pad(s,bs):
    out = bytearray(s)
    bfill = bs - (len(s) % bs)
    if bfill == 0:
        for x in range(0,bs):
            out.append(bs)
    else:
        for x in range(0,bfill):
            out.append(bfill)
    
    return bytes(out)


if __name__ == "__main__":
    print(pkcs7pad(b'YELLOW SUBMARINE',20))
