import mock
import pytest
import os, sys
from converter.converter import dec2bin
from converter.converter import bin2dec
from converter.converter import bin2complement1
from converter.converter import bin2complement2


def test_dec2bin():
    assert dec2bin(4, 2) == "100"
    assert dec2bin(6, 2) == "110"
    assert dec2bin(3, 3) == "10"
    assert dec2bin(
        3, 0) == "integer division or modulo by zero: Base has to be different than Zero"
    

def test_bin2dec():
    assert bin2dec('100') == '4'
    assert bin2dec('101') == '5'
    assert bin2dec('10a') == 'Oops!! binaries have only 1s and 0s'


def test_bin2complement1():
    assert bin2complement1('11111') == "0"
    assert bin2complement1('1010') == "101"


def test_bin2complement2():
    assert bin2complement2('10101') == "1011"
    assert bin2complement2('11111') == '1'


def test_init():
    from converter import converter
    with mock.patch.object(converter, "main", return_value=45):
        with mock.patch.object(converter, "__name__", "__main__"):
            with mock.patch.object(converter.sys, 'exit') as mock_exit:
                converter.init()
                assert mock_exit.call_args[0][0] == 45
