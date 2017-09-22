#!usr/bin/bash python3

val = 'YELLOW SUBMARINE'
test = 'YELLOW SUBMARINE\x04\x04\x04\x04'


def pkcs_7(input_, size):
    diff = size - len(input_)
    if diff <= 0 or diff > 255:
        return input_

    return input_ + chr(diff) * diff


def validate():
    result = pkcs_7(val, 20)
    print("Test 9 Result: {}".format("SUCCESS!" if test == result else "FAILURE!"))
