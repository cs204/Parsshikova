import pytest
from bank import value

def test_value():
    assert value("здравствуйте, как дела?") == 0
    assert value("здорово!") == 100
    assert value("завтра будет замечательный день") == 20

if __name__ == "__main__":
    pytest.main()
