#import wardrobe_2 as w
import wardrobe_app.wardrobe_3 as w
import pytest
import sys

# Python Version as tuple
python_version = (sys.version_info[0], sys.version_info[1], sys.version_info[2])
# Python Version as string
python_version_str = str(python_version).replace(', ', '.').strip('()')
print("Python Version --> {}".format(python_version_str))

@pytest.mark.default
def test_get_name():
    my_jeans = w.Clothing("blue jeans")
    assert my_jeans.get_name() == "blue jeans"
