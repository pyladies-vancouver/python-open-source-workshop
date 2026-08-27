# Session 6 — Exercises

Goal: extend a real CI pipeline, then experience the full loop of a failing
check on a PR and fixing it.

---

## Exercise 6.1 — Trace the pipeline 🧭

Reading `.github/workflows/ci.yml`, answer:

1. On which **events** does CI run?
2. How many **jobs** are there, and what does each do?
3. Which **Python versions** does the test job cover?
4. Which **step** would fail first if you introduced a lint error?

**Checkpoint:** you can describe, in plain English, everything the pipeline does.

---

## Exercise 6.2 — Watch CI run on a PR 🟢

If you opened a PR in an earlier session, open it on GitHub and find the
**Checks** section at the bottom. Watch the `lint` and `test` jobs run (or view a
completed run). Click **Details** on one job to see the live log and the steps
you just read about.

**Checkpoint:** you've seen the jobs from the YAML executing as real checks on a
PR.

---

## Exercise 6.3 — Break it on purpose, read the failure 🔴

On a throwaway branch, introduce a failure and see how CI (and local checks)
report it.

```bash
git switch -c ci-break-demo
```

Add a lint error — an unused import at the top of `src/firstpr/textutils.py`:

```python
import os   # unused: ruff will flag this
```

Run the same check CI runs:

```bash
ruff check .
```

Read the error message: it names the file, line, and rule code (`F401`). This is
*exactly* what you'd see in the CI log's `lint` job.

**Checkpoint:** you can read a ruff failure and know precisely what to fix.

---

## Exercise 6.4 — Fix it and go green ✅

Remove the bad import, then confirm both checks pass:

```bash
ruff check .
pytest
```

Clean up the demo branch:

```bash
git switch main
git branch -D ci-break-demo
```

**Checkpoint:** both checks are green again, and you understand the
break → read → fix → green loop that CI enforces on every PR.

---

## Exercise 6.5 — Extend the pipeline 🛠️

Make a real improvement to CI: also run the **doctests** explicitly and check
formatting. On a branch, edit the `test` job's steps in `ci.yml` to add:

```yaml
      - name: Check formatting
        run: |
          python -m pip install ruff
          ruff format --check .
```

Commit, push, and open a PR. Watch your *new* step appear in the checks.

**Checkpoint:** your PR shows an added CI step running successfully — you've
contributed to a project's automation, not just its code.

---

## Stretch goal 6.6 — Turn on pre-commit ⚡

```bash
pre-commit install
# now make a commit with trailing whitespace and watch the hook fix/flag it
```

**Checkpoint:** a git commit triggers the hooks locally, catching issues before
they ever reach CI.

---

## Wrap-up — where to go next 🌍

You've now done, for real, every step of contributing:

- found projects and issues,
- forked, branched, committed, and opened PRs,
- resolved a merge conflict,
- improved docs and built them,
- packaged and published to TestPyPI,
- read and extended a CI pipeline.

**Your next contribution:** revisit the `good first issue` you bookmarked in
Session 1 or 2, and apply this exact loop to it. You have everything you need.
