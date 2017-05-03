import wardrobe_2 as w

def test_get_name():
    myJeans = w.Clothing("blue jeans")
    assert myJeans.get_name() == "blue jeans"

def test_foo():
    myJeans = w.Clothing("boo", False)
    assert myJeans.is_clean() == False
    assert myJeans.get_name() == "boo"
