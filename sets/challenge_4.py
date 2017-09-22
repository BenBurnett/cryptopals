#!usr/bin/bash python3

import binascii

from Crypto.Util import strxor
from sets.challenge_3 import english_score, break_single_byte_xor


def validate():
    test = b"Now that the party is jumping\n"

    with open("../files/4.txt", "r") as f:
        lines = [binascii.unhexlify(line.strip('\n')) for line in f]

    idx, key = sorted([(i, break_single_byte_xor(lines[i], english_score)) for i in range(len(lines))], reverse=True,
                      key=lambda x: english_score(lines[x[0]]))[0]

    result = strxor.strxor_c(lines[idx], key)

    print("Test 4 Result: {}".format("SUCCESS!" if test == result else "FAILURE!"))
