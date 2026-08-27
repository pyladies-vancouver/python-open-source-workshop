# Session 3 — Exercises

Goal: do a real fork→PR cycle end to end, then deliberately create and resolve a
merge conflict so it never scares you again.

---

## Exercise 3.1 — Wire up your remotes 🔌

From inside your clone:

```bash
git remote add upstream https://github.com/YOUR-ORG/python-open-source-workshop.git
git remote -v
```

**Checkpoint:** you see both `origin` (your fork) and `upstream` (the original).

---

## Exercise 3.2 — A real feature branch → PR 🌱

Let's add a small, genuinely useful function to `textutils.py`: `whisper`, the
quiet opposite of `shout`.

```bash
git switch main
git fetch upstream && git merge upstream/main
git switch -c add-whisper
```

Add this to `src/firstpr/textutils.py`:

```python
def whisper(text: str) -> str:
    """Return ``text`` lowercased and wrapped in soft parentheses.

    Args:
        text: Any string.

    Returns:
        The text in lower case, surrounded by ``"(...)"``.

    Examples:
        >>> whisper("HELLO")
        '(hello)'
    """
    return "(" + text.lower() + ")"
```

Export it: add `whisper` to the imports and `__all__` in
`src/firstpr/__init__.py`. Then add a test in `tests/test_textutils.py`:

```python
def test_whisper():
    from firstpr.textutils import whisper
    assert whisper("HELLO") == "(hello)"
```

Verify, commit, push, and open the PR:

```bash
pytest && ruff check .
git add -A
git commit -m "Add whisper() as the counterpart to shout()"
git push -u origin add-whisper
```

**Checkpoint:** your PR is open, tests pass, and it exercises the same loop
you'll use on real projects.

---

## Exercise 3.3 — Read your own diff 👀

Before you pushed, you should have run `git diff`. Do it now on a fresh tweak:
change the `whisper` docstring wording, then run `git diff`. Identify the `+`
and `-` lines. Commit the improvement.

**Checkpoint:** you can explain, line by line, what your diff changed.

---

## Exercise 3.4 — The merge-conflict lab 💥 (safe & on purpose)

You'll make two branches edit the *same line*, then reconcile them.

```bash
# Branch A edits the version line
git switch main
git switch -c bump-a
# In src/firstpr/__init__.py change __version__ = "0.1.0" to "0.1.1"
git commit -am "Bump version to 0.1.1"

# Branch B edits the SAME line differently
git switch main
git switch -c bump-b
# In src/firstpr/__init__.py change __version__ = "0.1.0" to "0.2.0"
git commit -am "Bump version to 0.2.0"

# Now merge A into B and watch the conflict appear
git merge bump-a
```

git will report a conflict in `__init__.py`. Open it, find the
`<<<<<<< ======= >>>>>>>` markers, decide the real answer (say `"0.2.0"`),
delete the marker lines, then:

```bash
git add src/firstpr/__init__.py
git commit          # accept the default merge message
pytest              # make sure you didn't break anything
```

**Checkpoint:** the file has no conflict markers left, tests pass, and you feel
noticeably calmer about conflicts. Clean up the practice branches afterwards:

```bash
git switch main
git branch -D bump-a bump-b
```

---

## Stretch goal 3.5 — Keep your fork in sync 🔄

Practise the "catch up with upstream" dance you'll do at the start of every real
contribution:

```bash
git switch main
git fetch upstream
git merge upstream/main
git push origin main       # update your fork's main too
```

**Checkpoint:** your fork's `main` matches the upstream project's `main`.
