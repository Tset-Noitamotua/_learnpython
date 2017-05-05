import wardrobe_app.wardrobe_2 as w
import pytest
import sys

# Python Version as tuple
python_version = (sys.version_info[0], sys.version_info[1], sys.version_info[2])
# Python Version as string
python_version_str = str(python_version).replace(', ', '.').strip('()')
print("Python Version --> {}".format(python_version_str))

@pytest.mark.fast
@pytest.mark.skipif(python_version < (3,5), \
reason="Too old Python version! Need at least Python 3.5 - \
You have Python {}".format(python_version_str))
def test_get_name():
    myJeans = w.Clothing("blue jeans")
    assert myJeans.get_name() == "blue jeans"

@pytest.mark.fast
def test_clothing_class():
    myJeans = w.Clothing("boo", False)
    assert myJeans.is_clean() == False
    assert myJeans.get_name() == "boo"

@pytest.mark.slow
def test_foo_class():
    myJeans = w.Clothing("boo", False)
    assert myJeans.is_clean() == False
    assert myJeans.get_name() == "boo"

@pytest.mark.slow
def test_foobar_class():
    myJeans = w.Clothing("boo", False)
    assert myJeans.is_clean() == False
    assert myJeans.get_name() == "boo"

@pytest.mark.fail
def test_will_fail():
    assert False
