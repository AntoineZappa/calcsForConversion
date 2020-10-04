import pytest
from converter import dec2bin
from converter import bin2dec
from converter import bin2complement1
from converter import bin2complement2


def test_dec2bin():
    assert dec2bin(4, 2) == "100"
    assert dec2bin(6, 2) == "110"


def test_bin2dec():
    assert bin2dec(['1','0','0']) == 4


def test_bin2complement1():
    assert bin2complement1(['1','1','1','1','1']) == "00000"


def test_bin2complement2():
    assert bin2complement2('10101') == "01001"
    assert bin2complement2('10111') == '01011'
