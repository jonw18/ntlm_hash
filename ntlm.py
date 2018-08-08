#!/usr/bin/python

import binascii
import hashlib
import sys

if len(sys.argv) != 2:
    print "\nUsage: python ntlm.py [PASSWORD]\n"
    sys.exit(0)

password = sys.argv[1]
ntlm_hash = hashlib.new('md4', password.encode('utf-16le')).digest().encode('hex')
print "\nPassword:  " + password
print "ntlm hash: " + ntlm_hash + "\n"
