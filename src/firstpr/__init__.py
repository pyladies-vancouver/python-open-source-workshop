"""firstpr: a tiny practice library for the Python Open Source Workshop.

This package exists so workshop participants have a small, friendly, *real*
codebase to contribute to. Nothing here is production-critical, which means
you can experiment freely: open issues, send pull requests, break things on a
branch, and learn the full contribution lifecycle end to end.

Public API:
    greet, greet_many   -- from :mod:`firstpr.greetings`
    shout, titleize, word_count -- from :mod:`firstpr.textutils`
"""

from firstpr.greetings import greet, greet_many
from firstpr.textutils import shout, titleize, word_count

__all__ = ["greet", "greet_many", "shout", "titleize", "word_count"]
__version__ = "0.1.0"
