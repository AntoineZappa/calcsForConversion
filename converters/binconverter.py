#/usr/bin/env python

import sys
import os

def init():
    if __name__ == "__main__":
        sys.exit(main())

def main():

    mode = str(input('''\n
+------------------------------------------------------------+
|    Type a number to select a conversion mode:              |
+------------------------------------------------------------+
|    1: Decimal to Binary (with base 2) or any other base    |
|    2: Binary to decimal                                    |   
|    3: Binary to complement 1                               |
|    4: Binary to complement 2                               |        
+------------------------------------------------------------+                          

Mode: '''))

    if mode == '1':
        number = int(input('Type a number to change the base: '))
        base = int(input('Type its base: '))
        print(dec2bin(number, base))

    elif mode == '2':
        binary = str(input('Input a number in binary: '))
        print(bin2dec(binary))

    elif mode == '3':
        binary = str(input('Input a number in binary: '))
        print(bin2complement1(binary))

    elif mode == '4':
        binary = str(input('Input a number in binary: '))
        print(bin2complement2(binary))

    else:
        print('\n>>>Input not valid. It must be a number in the mode range<<<')
        main()


def dec2bin(decimal, base):
    """Convert from decimal to a number with a new base

    Args:
        decimal (int): number to change base
        base (int): base

    Returns:
        str: str with the converted number
    """
    conversion = ''

    try:
        if base == 1:
            raise Exception() 
            result = "Base has to be different than 1"
        while decimal // base != 0:

            conversion = str(decimal % base) + conversion
            decimal = decimal // base
            result = str(decimal) + conversion
            
    except ZeroDivisionError as error:
        result = f"{error}: Base has to be different than Zero"
    
    except TypeError as error:
        
        result = "Letters of other signs are not allowed"

    return result


def bin2dec(binary):
    """ Convert binary to decimal

    Args:
        binary (str): list of elements from binay  str

    Returns:
        str: str with the final decimal 
    """

    result = 0
    binary = list(binary)
    
    try:
        for i in range(len(binary)):
            n = binary.pop()
            if n not in ['1','0']:
                raise Exception()
                result = 'Oops!! binaries have only 1s and 0s'
            if n == '1':
                result = result + pow(2, i)
    except Exception:
        result = 'Oops!! binaries have only 1s and 0s'
    return str(result)
    

def bin2complement1(binary):
    """Convert a binary in bincary one's compliment

    Args:
        binary (str): [description]

    Returns:
        str: str with the new binary
    """
    try: 
        binmap = map(lambda i: '1' if i == '0' else '0', 
                    list(binary))
        binstr = "".join(list(binmap))
        binfinal = bin(int(binstr, 2))
        result = str(binfinal).replace('0b', '')
    except Exception:
        result = 'Oops!! binaries have only 1s and 0s'
    return result


def bin2complement2(binary):
    """Convert decimal into binary two's compliment

    Args:
        binary (str): [description]

    Returns:
        str: [description]
    """
    binmap = map(lambda i: '1' if i == '0' else '0',
                 list(binary))
    binstr = "".join(list(binmap))

    intFromBin = int(binstr, 2)
    intToSumUp = int('00000001',2)

    binfinal = bin(intFromBin + intToSumUp)
    
    return str(binfinal).replace('0b','')


init()
