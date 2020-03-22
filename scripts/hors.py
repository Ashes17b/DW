import random
import sys

nvals = 256
max = 256

message = "hello"

if (len(sys.argv) > 1):
	message = int(sys.argv[1])


def get_private():
    priv = []
    for x in range(nvals):
        priv.append(random.randint(0, max))
    return priv


def int_to_bytes(value):
    result = bytearray()

    for i in range(0, len(value)/2):
	str = value[2*i:2*i+2]
        result.append(int(str, 16))
    result.reverse()

    return result


def hashthem(priv):
    pub = []

    for x in priv:
       m = hashlib.md5()
       m.update(str(x))
       pub.append(m.hexdigest()[:4])
    return pub


def getsig(val, priv, pub):
    sig = []
    for x in val:
      sig.append(pub[priv[x]])
    return sig


import hashlib

m = hashlib.md5()

m.update(message)

msg = int_to_bytes(m.hexdigest())

print "Byte values:",

for i in range(len(msg)):
	print msg[i],

print
print
priv = get_private()

print "Private key"
print priv

print
public = hashthem(priv)

print "Public key"
print public

print

print "Signature"

sig = getsig(msg, priv, public)

print sig
