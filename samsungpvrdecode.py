#!/usr/bin/env python

from Crypto.Cipher import AES
import io

def getKey(mdbfile):

    fp = open(mdbfile, 'rb')
    #fpw = open(keyfile, 'wb')
    fp.seek(8)
    key = []
    dump = []
    for i in range(0,16):
        dump.append(fp.read(1))
        if ((i + 1) % 4 == 0):
            key.append(''.join(dump[::-1]))
	    dump = []

    s = ''.join(key)
    return s
    #fpw.write(s)


    fp.close()
    #fpw.close()


mdbfile = "/mnt/stuff/stuff/20130915233306.mdb"
#keyfile = "/mnt/stuff/stuff/20130915233306.key"

print getKey(mdbfile)
