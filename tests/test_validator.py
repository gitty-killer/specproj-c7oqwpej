from src.models import Record
from src.validator import is_valid


def test_is_valid():
    assert is_valid(Record(key='k', value='v'))
    assert not is_valid(Record(key='', value='v'))
