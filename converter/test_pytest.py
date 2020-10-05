import pytest
from converter import dec2bin
from converter import bin2dec
from converter import bin2complement1
from converter import bin2complement2


def test_dec2bin():
    assert dec2bin(4, 2) == "100"
    assert dec2bin(6, 2) == "110"
    assert dec2bin(3, 3) == "110"


def test_bin2dec():
    assert bin2dec('100') == '4'
    assert bin2dec('101') == '5'


def test_bin2complement1():
    assert bin2complement1('11111') == "0"
    assert bin2complement1('1010') == "101"

def test_bin2complement2():
    assert bin2complement2('10101') == "1011"
    assert bin2complement2('11111') == '1'
