#!usr/bin/bash python3

import binascii

from Crypto.Util import strxor


def validate():
    hex_val = b"1c0111001f010100061a024b53535009181c"
    hex_key = b"686974207468652062756c6c277320657965"
    hex_res = b"746865206b696420646f6e277420706c6179"

    x = binascii.unhexlify(hex_val)
    y = binascii.unhexlify(hex_key)

    result = binascii.hexlify(strxor.strxor(x, y))

    print("Test 2 Result: {}".format("SUCCESS!" if hex_res == result else "FAILURE!"))
