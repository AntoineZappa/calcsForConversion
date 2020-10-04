#/usr/bin/env python
import pytest

def main():
    mode = str(input('''\nType a number to select a conversion mode:

    1: Decimal to Binary (with base 2) or any other base
    2: Binary to decimal
    3: Binary to complement 1
    4: Binary to complement 2

Mode: '''))

    if mode == '1':
        try:
            numero = int(input('Input a number to change the base: '))
            base = int(input('Input a base: '))
            
        except ValueError:
            print("")
        print(dec2bin(numero, base))

    elif mode == '2':
        binary = list(input('Input a number in binary: '))
        print(bin2dec(binary))

    elif mode == '3':
        binary = list(input('Input a number in binary: '))
        print(bin2complement1(binary))

    elif mode == '4':
        binary = list(input('Input a number in binary: '))
        print(bin2complement2(binary))

    else:
        print('\n>>>Input not valid. It must be a number in the mode range<<<')
        main()

def dec2bin(decimal, base):

    conversion = ''
    while decimal // base != 0:
        conversion = str(decimal % base) + conversion
        print(conversion)
        decimal = decimal // base
        result = str(decimal) + conversion
    print(type(result))
    return result



def bin2dec(binary):
    
    value = 0
    for i in range(len(binary)):
        n = binary.pop()
        if n == '1':
            value = value + 2**i
    print(type(value))
    return value
    

def bin2complement1(binary):

    result = []
    for i,n in enumerate(binary):
        if n == '1':
            n = '0'
        elif n == '0':
            n = '1'
        result.append(n)
    
    return "".join(result)


def bin2complement2(binary):

    result = []
    for i, n in enumerate(binary):
        if i in range(len(binary)-2):
            if n == '1':
                n = '0'
            elif n == '0':
                n = '1'
        result.append(n)
    
    return "".join(result)

if __name__ == "__main__":
    main()
            
