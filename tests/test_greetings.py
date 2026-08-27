"""Tests for firstpr.greetings.

New to testing? Read these top to bottom -- each test is a tiny, readable
statement of "given this input, expect this output". Adding a test is one of
the easiest and most welcome open source contributions you can make.
"""

import pytest

from firstpr.greetings import greet, greet_many


def test_greet_casual():
    assert greet("Ada") == "Hi, Ada!"


def test_greet_formal():
    assert greet("Ada", formal=True) == "Good day, Ada."


def test_greet_strips_whitespace():
    assert greet("  Ada  ") == "Hi, Ada!"


def test_greet_empty_raises():
    with pytest.raises(ValueError):
        greet("   ")


def test_greet_many():
    assert greet_many(["Ada", "Grace"]) == ["Hi, Ada!", "Hi, Grace!"]


def test_greet_many_formal():
    assert greet_many(["Ada"], formal=True) == ["Good day, Ada."]
