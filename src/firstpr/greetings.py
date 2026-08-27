"""Friendly greeting helpers.

These functions are deliberately simple. Their real job is to give you
something to read, document, test, and extend during the workshop.
"""

from __future__ import annotations

from collections.abc import Iterable


def greet(name: str, *, formal: bool = False) -> str:
    """Return a greeting for a single person.

    Args:
        name: The person's name. Leading/trailing whitespace is stripped.
        formal: If ``True``, use a more formal salutation.

    Returns:
        A greeting string.

    Raises:
        ValueError: If ``name`` is empty or only whitespace.

    Examples:
        >>> greet("Ada")
        'Hi, Ada!'
        >>> greet("Ada", formal=True)
        'Good day, Ada.'
    """
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    if formal:
        return f"Good day, {cleaned}."
    return f"Hi, {cleaned}!"


def greet_many(names: Iterable[str], *, formal: bool = False) -> list[str]:
    """Return a greeting for each name in ``names``.

    Args:
        names: An iterable of names.
        formal: Passed through to :func:`greet`.

    Returns:
        A list of greeting strings, one per name.

    Examples:
        >>> greet_many(["Ada", "Grace"])
        ['Hi, Ada!', 'Hi, Grace!']
    """
    return [greet(name, formal=formal) for name in names]
