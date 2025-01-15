import pytest
from marctools import marccount

@pytest.mark.parametrize(
    "filename,expected", [
        ("data/ex1.mrc", 1),
    ])
def test_file_counting(filename, expected):
    assert marccount.do_count(filename) == expected
