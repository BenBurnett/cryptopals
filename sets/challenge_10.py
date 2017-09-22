#!usr/bin/bash python3

import base64

from Crypto.Cipher import AES
from Crypto.Util import strxor
from sets.challenge_9 import pkcs_7


class AES_CBC(object):
    def __init__(self, key, iv):
        self._cipher = AES.new(key, AES.MODE_ECB)
        self._iv = iv

    @staticmethod
    def _chunk_gen(data):
        return (pkcs_7(data[i:i + 16], 16) for i in range(0, len(data), 16))

    def decrypt(self, data):
        iv = self._iv
        result = b''
        for chunk in AES_CBC._chunk_gen(data):
            result += strxor.strxor(self._cipher.decrypt(chunk), iv)
            iv = chunk
        return result

    def encrypt(self, data):
        iv = self._iv
        result = b''
        for chunk in AES_CBC._chunk_gen(data):
            iv = self._cipher.encrypt(strxor.strxor(chunk, iv))
            result += iv
        return result


def validate():
    with open('../files/10.txt', 'rb') as f:
        data_ = base64.decodebytes(f.read())

    key_ = b'YELLOW SUBMARINE'
    iv_ = b'\x00' * 16
    cipher = AES_CBC(key_, iv_)

    result_ = cipher.decrypt(data_)
    result_2 = cipher.encrypt(result_)

    print(result_.decode())
    print("Test 10 Result: {}".format("SUCCESS!" if data_ == result_2 else "FAILURE!"))
