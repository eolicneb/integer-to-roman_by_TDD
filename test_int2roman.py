import pytest
from int2roman import (Int2Roman,
                       _get_unit_decade,
                       _get_larger_decade)


def test_zero():
    assert Int2Roman(0) == ""

def test_large_exception():
    with pytest.raises(ValueError):
        Int2Roman(4000)

def test_non_int():
    with pytest.raises(TypeError):
        Int2Roman("non integer")

@pytest.mark.parametrize("big_int, big_dec", [(7, 7), (54, 50), (376, 300), (2456, 2000)])
def test_big_decade(big_int, big_dec):
    assert _get_larger_decade(big_int) == big_dec

def test_directs():
    assert Int2Roman(1) == "I"
    assert Int2Roman(5) == "V"
    assert Int2Roman(10) == "X"
    assert Int2Roman(50) == "L"
    assert Int2Roman(100) == "C"
    assert Int2Roman(500) == "D"
    assert Int2Roman(1000) == "M"

@pytest.mark.parametrize("dec, prev", [(0, 0), (2,1), (43, 10), (823, 100)])
def test_previous_decade(dec, prev):
    assert _get_unit_decade(dec) == prev

def test_one_before_pentade():
    assert Int2Roman(4) == "IV"
    assert Int2Roman(9) == "IX"
    assert Int2Roman(40) == "XL"
    assert Int2Roman(90) == "XC"
    assert Int2Roman(400) == "CD"
    assert Int2Roman(900) == "CM"

def test_many_after_pentade():
    assert Int2Roman(2) == "II"
    assert Int2Roman(60) == "LX"
    assert Int2Roman(300) == "CCC"
    assert Int2Roman(700) == "DCC"

@pytest.mark.parametrize("the_int, roman", [(23, "XXIII"), (2938, "MMCMXXXVIII")])
def test_complete_parsing(the_int, roman):
    assert Int2Roman(the_int) == roman