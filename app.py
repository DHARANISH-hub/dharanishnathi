"""Simple, well-structured example module.

This file provides a small arithmetic utility with validation and a tiny
command-line entrypoint.
"""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """Return the sum of two numeric values.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The arithmetic sum of ``a`` and ``b``.

    Raises:
        TypeError: If either argument is not ``int`` or ``float``.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("'a' must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("'b' must be a number")
    return float(a + b)


def main() -> None:
    """Run a tiny demo when executed as a script."""
    result = add(2, 3)
    print(f"2 + 3 = {result}")


if __name__ == "__main__":
    main()
