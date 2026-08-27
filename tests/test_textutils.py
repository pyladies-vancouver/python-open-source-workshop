"""Tests for firstpr.textutils."""

from firstpr.textutils import shout, titleize, word_count


def test_shout():
    assert shout("hello") == "HELLO!"


def test_titleize():
    assert titleize("the zen of python") == "The Zen Of Python"


def test_word_count_basic():
    assert word_count("open source is great") == 4


def test_word_count_empty():
    assert word_count("   ") == 0
