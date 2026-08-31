# Contributing

Welcome! This project exists to be contributed to. Every step below is
something you'll practice during the workshop — and the same pattern works on
most Python projects you'll meet in the wild.

## The contribution loop, in short

1. **Find or open an issue** describing what you want to change.
2. **Fork** the repo and **clone** your fork.
3. Create a **branch** with a descriptive name: `git switch -c fix-titleize-docstring`.
4. Make your change. Keep it focused — one idea per pull request.
5. **Run the checks locally**: `pytest` and `ruff check .` should both pass.
6. **Commit** with a clear message, **push** your branch, and **open a pull request**.
7. Respond to review feedback by pushing more commits to the same branch.

## Setting up

```bash
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
python -m pip install -e ".[dev,docs]"
pre-commit install                    # optional but recommended
```

## Before you push, check your work

```bash
pytest             # all tests pass?
ruff check .       # linter clean?
ruff format .      # auto-format your code
```

If you added a feature, add a test for it. If you fixed a bug, add a test that
would have caught it. If you changed behaviour, update the docstring and docs.

## What makes a good first contribution here

- Fixing a typo or clarifying a docstring
- Adding a test for an edge case (empty strings, unicode, very long input…)
- Handling an edge case the code currently ignores
- Improving an error message
- Adding an example to the documentation

Look for issues labelled **`good first issue`** and **`documentation`**.

## Commit message style

Short imperative summary line (≤ 50 chars), e.g. `Add test for empty word_count`.
Add a body if the *why* isn't obvious from the summary.

## Licensing your contribution

This repository is dual licensed: the curriculum under CC BY-SA 4.0 and the
code under MIT (see [README](README.md#license)). By opening a pull request you
agree to license your contribution under whichever of the two covers the files
you touched. You keep the copyright on what you wrote.

## Code of conduct

By participating you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).
Be kind. Assume good faith. Ask questions freely — everyone here was new once.
