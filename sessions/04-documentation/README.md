# Session 4 — Documentation contributions

**Duration:** ~55 min · **Format:** demo + docs-building lab
**Goal:** understand why docs are the friendliest place to contribute, write
good docstrings, build the docs locally, and open a documentation PR.

---

## 1. Why start with docs? (5 min)

Documentation is the highest-leverage, lowest-risk place for a new contributor:

- You **don't need to understand the whole codebase** to fix a confusing sentence.
- Mistakes are **low-stakes** — you're not going to take down production.
- **Every future reader benefits**, and maintainers are usually delighted.
- You often understand the beginner's pain *better than the maintainers do*,
  because you're living it right now.

Many major projects — including CPython itself — treat docs contributions as
first-class and actively mentor them.

## 2. The layers of Python documentation (10 min)

"Docs" isn't one thing. From closest-to-code to furthest:

1. **Docstrings** — the `"""..."""` right inside functions/classes/modules.
   They power `help()` and IDE tooltips, and tools can turn them into web pages.
2. **API reference** — pages generated *from* those docstrings (via Sphinx
   `autodoc`).
3. **Narrative docs** — tutorials, how-tos, explanations written as prose pages
   (Markdown or reStructuredText).
4. **README / CONTRIBUTING** — the front door.

This repo has all four. `src/firstpr/*.py` holds the docstrings; `docs/` builds
them into a website.

## 3. Anatomy of a good docstring (10 min)

We use **Google-style** docstrings (Sphinx's Napoleon extension understands
them). Look at `greet` in `src/firstpr/greetings.py`:

```python
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
    """
```

A strong docstring has: a **one-line summary**, then **Args**, **Returns**,
**Raises** (if it can), and **Examples**. The examples aren't decoration —
they're runnable (see doctests below).

## 4. Two markup languages you'll meet (5 min)

- **reStructuredText (.rst)** — the traditional Sphinx format. More powerful,
  slightly fussier syntax (`.. directive::`, `` `role` ``).
- **Markdown (.md)** — familiar and quick; usable in Sphinx via the **MyST**
  parser, which this repo enables.

You don't need to master reST today. Know that both exist and that a project's
docs will pick one; match whatever's already there.

## 5. Docs that can't go stale: doctests (5 min)

The `>>> greet("Ada")` lines in docstrings can be **run as tests**. This project
does exactly that — `pytest` is configured with `--doctest-modules`, so if you
change a function's behaviour but forget to update its example, the test suite
fails. Try it in the exercises.

## 6. Building the docs locally (rest → exercises)

```bash
python -m pip install -e ".[docs]"
sphinx-build -b html docs docs/_build/html
# open docs/_build/html/index.html in your browser
```

Seeing your docstring change appear on a real HTML page is one of the most
satisfying moments in open source. Go do it in [`exercises.md`](exercises.md).

### Key terms from this session

- **Docstring** — documentation inside the code, in `"""triple quotes"""`
- **autodoc** — Sphinx pulling docstrings into web pages
- **reST vs Markdown (MyST)** — the two doc markup languages
- **doctest** — runnable `>>>` examples that keep docs honest
