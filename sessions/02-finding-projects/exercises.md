# Session 2 — Exercises

Goal: practice discovery and repo-reading so that picking up a real issue feels
routine.

---

## Exercise 2.1 — Map this repository 🗺️

Without looking at the Session 2 README's diagram, answer these by exploring the
files yourself:

1. Which file defines the package's **version number**?
2. Which function has a **deliberately documented edge case** for empty input?
   (Hint: search the `src/` folder.)
3. Where would you add a **test** for a new function in `textutils.py`?
4. What **linter** does this project run, and where is it configured?

**Checkpoint:** you found the answers by navigating, not by asking — that's the
skill.

---

## Exercise 2.2 — Trace a function end to end 🔍

Pick `word_count`.

```bash
grep -rn "word_count" src/ tests/ docs/
```

Follow the results: where is it **defined**, where is it **tested**, and where
is it **documented**? Sketch the three locations. This is exactly how you'd
orient yourself in a project you've never seen.

**Checkpoint:** you can point to definition, test, and doc for one function.

---

## Exercise 2.3 — Evaluate a real project 🚦

Go to a Python project you use or find via issue search. Spend 5 minutes
scoring it against the "green-flag" checklist:

- [ ] Commits in the last few months?
- [ ] A `CONTRIBUTING` file?
- [ ] Any `good first issue` / `help wanted` labels with open issues?
- [ ] Do recent PRs from new contributors get friendly, timely replies?

**Checkpoint:** you can say whether you'd feel comfortable opening a PR there,
and why.

---

## Exercise 2.4 — Pick and plan an issue 📝

Find one open, unclaimed beginner issue (in this repo's issue tracker if it has
seeded issues, or in a real project). Write a two-line plan:

1. File(s) I'd change:
2. How I'd know it worked (which test/output):

You do **not** have to implement it now — Session 3 gives you the git skills to
do so cleanly.

**Checkpoint:** you have a written plan for a concrete, bounded change.

---

## Stretch goal 2.5 — Draft an issue of your own ✍️

Notice something you'd improve in `firstpr` (a missing edge case? an unclear
docstring? a function you wish existed, like `whisper()` as the opposite of
`shout()`?). Draft a GitHub issue for it:

- **Title:** short and specific
- **Body:** what, why, and — if it's a bug — steps to reproduce plus expected vs
  actual behaviour

Opening it is optional today, but a well-written issue is itself a valued
contribution.
