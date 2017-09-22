#!usr/bin/bash python3

import binascii

from Crypto.Util import strxor

english_data = {
    ' ': 18.31,
    'E': 10.21,
    'T': 7.51,
    'A': 6.55,
    'O': 6.20,
    'N': 5.70,
    'I': 5.73,
    'S': 5.33,
    'R': 4.97,
    'H': 4.86,
    'L': 3.36,
    'D': 3.35,
    'U': 2.30,
    'C': 2.27,
    'M': 2.02,
    'F': 1.97,
    'W': 1.69,
    'G': 1.64,
    'P': 1.50,
    'Y': 1.47,
    'B': 1.27,
    'V': 0.79,
    'K': 0.57,
    'X': 0.15,
    'J': 0.11,
    'Q': 0.09,
    'Z': 0.06
}


def english_score(s):
    return sum(english_data.get(chr(c).upper(), -2) for c in s)


def break_single_byte_xor(s, score):
    return sorted([c for c in range(256)], reverse=True, key=lambda x: score(strxor.strxor_c(s, x)))[0]


def validate():
    val = b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    test = b"Cooking MC's like a pound of bacon"
    bin_val = binascii.unhexlify(val)

    key = break_single_byte_xor(bin_val, english_score)

    result = strxor.strxor_c(bin_val, key)

    print("Test 2 Result: {}".format("SUCCESS!" if test == result else "FAILURE!"))
