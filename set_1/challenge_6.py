import base64
import itertools

from challenge_3 import break_single_byte_xor, english_score
from challenge_5 import xor_decrypt


def hamming_distance(a, b):
    return sum([bin(x ^ y).count('1') for x, y in zip(a, b)])


def hamming_distance_normalized(s, key_len, count=4):
    combos = list(itertools.combinations([s[i:i + key_len] for i in range(0, count * key_len, key_len)], 2))
    return sum([hamming_distance(combo[0], combo[1]) for combo in combos]) / (key_len * len(combos))


def break_repeating_xor(s, key_len):
    blocks = [s[i: i + key_len] for i in range(0, len(s), key_len)]
    trans = itertools.zip_longest(*blocks, fillvalue=0)
    return bytes([break_single_byte_xor(bytes(x), english_score) for x in trans])


def validate():
    with open("6.txt", "rb") as f:
        data = base64.decodebytes(f.read())

    key_len_ = min(range(2, 41), key=lambda x: hamming_distance_normalized(data, x))
    key = break_repeating_xor(data, key_len_)
    result = xor_decrypt(key, data)

    print(result.decode('ascii'))
