#!usr/bin/bash python3

import base64
import binascii


def hex_to_b64(hex_val):
    return base64.b64encode(binascii.unhexlify(hex_val))


def validate():
    hex_val = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    b64_val = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    result = hex_to_b64(hex_val)

    print("Test 1 Result: {}".format("SUCCESS!" if b64_val == result else "FAILURE!"))
