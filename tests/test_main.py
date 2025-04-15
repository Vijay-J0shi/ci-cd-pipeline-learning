from src.main import add , subtract

def test_add_func():
    assert add(32,5)==37
    assert add(0,0)==0
    assert add(5,6)==11

def test_sub_fun():
    assert subtract(50,2)==48
    assert subtract(0,0)==0
