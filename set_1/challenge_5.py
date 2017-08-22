import binascii

from Crypto.Cipher import XOR


def xor_encrypt(key, s):
    return XOR.new(key).encrypt(s)


def xor_decrypt(key, s):
    return XOR.new(key).decrypt(s)


def validate():
    val = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
    test = b'''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''

    result = binascii.hexlify(xor_encrypt('ICE', val))

    print("Test 5 Result: {}".format("SUCCESS!" if test == result else "FAILURE!"))
