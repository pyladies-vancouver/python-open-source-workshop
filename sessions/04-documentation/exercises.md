# Session 4 — Exercises

Goal: improve real documentation, build it, and see doctests protect you.

---

## Exercise 4.1 — Build the docs 🏗️

```bash
python -m pip install -e ".[docs]"
sphinx-build -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` in your browser and click through to the API
reference page.

**Checkpoint:** you can see `greet`, `shout`, `titleize`, and `word_count`
documented on a web page that was generated from the code.

---

## Exercise 4.2 — Improve a docstring, watch it appear ✨

Pick `titleize` in `src/firstpr/textutils.py`. Its docstring mentions it differs
from `str.title`. Add a second example to the `Examples:` section showing that
difference, e.g.:

```
        >>> titleize("don't panic")
        "Don't Panic"
```

Rebuild the docs and refresh the API page.

**Checkpoint:** your new example shows up on the rendered page.

---

## Exercise 4.3 — Feel a doctest catch you 🧷

Doctests keep examples honest. Prove it:

1. In `greetings.py`, temporarily change the `greet("Ada")` **example output**
   in the docstring to something wrong, like `'Hello, Ada!'` (don't change the
   code).
2. Run `pytest`.

You'll see the doctest fail, because the example no longer matches what the code
returns. Now fix the example back and confirm `pytest` is green again.

**Checkpoint:** you understand that examples in docstrings are tested, so they
can't quietly rot.

---

## Exercise 4.4 — Ship a documentation PR 📤

Turn Exercise 4.2 into a real contribution:

```bash
git switch main && git fetch upstream && git merge upstream/main
git switch -c docs-titleize-example
# (keep your titleize example change)
pytest
git add -A
git commit -m "docs: add apostrophe example to titleize"
git push -u origin docs-titleize-example
```

Open the PR on GitHub with a one-line description.

**Checkpoint:** you have an open PR labelled (or titled) as a documentation
change — often the single most-welcomed kind of first contribution.

---

## Stretch goal 4.5 — Add a narrative page 📚

Create `docs/tutorial.md` with a short "getting started with firstpr" walkthrough
(install, import, call two functions). Add `tutorial` to the `toctree` in
`docs/index.md`, rebuild, and confirm it appears in the sidebar. Bonus: this
teaches you how `toctree` wires pages together in Sphinx.
