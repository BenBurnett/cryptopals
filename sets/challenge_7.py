#!usr/bin/bash python3

import base64

from Crypto.Cipher import AES


def validate():
    with open("../files/7.txt", "rb") as f:
        data = base64.decodebytes(f.read())

    cipher = AES.new("YELLOW SUBMARINE", AES.MODE_ECB)

    result = cipher.decrypt(data)

    print(result.decode('utf-8'))
