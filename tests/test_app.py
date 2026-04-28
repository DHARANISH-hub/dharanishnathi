import pytest

from app import add


def test_add_integers() -> None:
    assert add(2, 3) == 5.0


def test_add_floats() -> None:
    assert add(2.5, 0.5) == 3.0


def test_add_rejects_invalid_type() -> None:
    with pytest.raises(TypeError):
        add("2", 3)
