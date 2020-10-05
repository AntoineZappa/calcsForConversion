#/usr/bin/env python


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
        try:
            number = int(input('Input a number to change the base: '))
            base = int(input('Input a base: '))
            
        except ValueError:
            print("")
        print(dec2bin(number, base))

    elif mode == '2':
        binary = str(input('Input a number in binary: '))
        print(bin2dec(binary))

    elif mode == '3':
        binary = str(input('Input a number in binary: '))
        print(bin2complement1(binary))

    elif mode == '4':
        binary = list(input('Input a number in binary: '))
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

    while decimal // base != 0:

        conversion = str(decimal % base) + conversion
        decimal = decimal // base
        result = str(decimal) + conversion
    
    return result


def bin2dec(binary):
    """ Convert binary to decimal

    Args:
        binary (str): list of elements from binay  str

    Returns:
        str: str with the final decimal 
    """
    value = 0
    binary = list(binary)
    for i in range(len(binary)):
        n = binary.pop()
        if n == '1':
            value = value + pow(2,i)

    return str(value)
    

def bin2complement1(binary):
    """Convert a binary in bincary two's compliment

    Args:
        binary (str): [description]

    Returns:
        str: str with the new binary
    """
    result = []
    for i,n in enumerate(binary):
        if n == '1':
            n = '0'
        elif n == '0':
            n = '1'
        result.append(n)
    integer = int("".join(result),2)
    binfinal = bin(integer)

    return str(binfinal).replace('0b', '')

def bin2complement2(binary):

    result = []
    for i, n in enumerate(binary):
        if i in range(len(binary)):
            if n == '1':
                n = '0'
            elif n == '0':
                n = '1'
        result.append(n)

    numstr = "".join(result)
    bin1 = int(numstr, 2)
    bin2 = int('00000001',2)
    
    binfinal = bin (bin1 + bin2)
    
    return str(binfinal).replace('0b','')

if __name__ == "__main__":
    main()
