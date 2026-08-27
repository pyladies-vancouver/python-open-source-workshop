"""Small text-processing helpers.

Good candidates for "good first issue" style improvements: edge cases,
extra options, better docstrings, and more tests. See the session 04 and
session 01 exercises for suggested contributions.
"""

from __future__ import annotations


def shout(text: str) -> str:
    """Return ``text`` uppercased with an exclamation mark.

    Args:
        text: Any string.

    Returns:
        The text in upper case, followed by ``"!"``.

    Examples:
        >>> shout("hello")
        'HELLO!'
    """
    return text.upper() + "!"


def titleize(text: str) -> str:
    """Return ``text`` with the first letter of each word capitalised.

    Unlike :meth:`str.title`, this splits only on spaces, so apostrophes
    inside a word are left alone.

    Args:
        text: Any string.

    Returns:
        A title-cased version of the text.

    Examples:
        >>> titleize("the zen of python")
        'The Zen Of Python'
    """
    return " ".join(word[:1].upper() + word[1:] for word in text.split(" "))


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``.

    Args:
        text: Any string.

    Returns:
        The word count. An empty or whitespace-only string returns ``0``.

    Examples:
        >>> word_count("open source is great")
        4
        >>> word_count("   ")
        0
    """
    return len(text.split())
