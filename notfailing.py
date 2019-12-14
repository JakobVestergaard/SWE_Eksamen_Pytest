
from rle import rle

def test_rle():
    assert rle('kkk') == '3k'

def test_rle2():
    assert rle('kkkkkkoooo') == '6k4o'

def test_empty():
    assert rle('') == ''

def test_nordic():
    assert rle('æøå') == '1æ1ø1å'

def test_weird():
    assert  rle('§~*') == '1§1~1*'

def test_numbers():
    assert rle('123') == '111213'

def test_alot():
    assert rle(' ') == '1 '

def test_fun():
    assert rle('äâã') == '1ä1â1ã'

def test_spaces():
    assert rle('kkk eee  lll') == '3k1 3e2 3l'

def test_floats():
    assert rle('3.14') == '131.1114'

def test_floats1():
    assert rle('3,14') == '131,1114'

def test_Randers():
    assert rle('Rr') == '1R1r'

def test_escape():
    assert rle('\\\\') == '2\\' 
