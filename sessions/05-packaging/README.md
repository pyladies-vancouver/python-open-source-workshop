# Session 5 — Packaging

**Duration:** ~60 min · **Format:** demo + build-and-publish lab
**Goal:** understand what "a Python package" actually is, read and edit a
`pyproject.toml`, build a wheel, and publish to **TestPyPI**.

---

## 1. What problem does packaging solve? (10 min)

You've been running `pip install -e .` all day. Packaging is what makes that
possible — it's the difference between "a folder of `.py` files on my laptop"
and "something anyone in the world can `pip install`".

Key ideas:

- **Distributions** are the shippable artifacts:
  - a **wheel** (`.whl`) — a pre-built, fast-to-install format
  - an **sdist** (`.tar.gz`) — the source, built on the user's machine if needed
- **PyPI** (the Python Package Index) is where public packages live.
- **TestPyPI** is a separate sandbox copy of PyPI for practising — we'll use it
  so nobody accidentally publishes to the real index.

## 2. `pyproject.toml`, the modern standard (15 min)

One file now describes how to build a project and its metadata. Open this repo's
[`../../pyproject.toml`](../../pyproject.toml) and read along:

```toml
[build-system]
requires = ["hatchling"]          # the tool that builds the package
build-backend = "hatchling.build"

[project]
name = "firstpr"                  # the pip-install name
version = "0.1.0"
description = "..."
readme = "README.md"
requires-python = ">=3.9"
license = "MIT"
dependencies = []                 # runtime deps go here

[project.optional-dependencies]
dev = ["pytest>=7.0", "ruff>=0.4", "build>=1.0"]   # extras: pip install ".[dev]"
```

Things to notice:

- **`name` vs import name.** The install name (`firstpr`) and the import name
  (`import firstpr`) happen to match here, but they don't have to.
- **`dependencies`** are what your users must have. **`optional-dependencies`**
  (extras) are opt-in groups like `dev` and `docs`.
- **`requires-python`** stops the package installing on unsupported versions.
- **Build backend.** We use `hatchling`; you'll also see `setuptools`,
  `flit`, and `pdm`. They do the same job.

## 3. src-layout and why it's here (5 min)

Our code lives in `src/firstpr/`, not `firstpr/` at the top level. This
**src-layout** prevents a classic bug where tests accidentally import the
*local folder* instead of the *installed package*, hiding packaging mistakes.
The `[tool.hatch.build.targets.wheel]` line tells the builder where to look.

## 4. Versioning (5 min)

Versions communicate change. **Semantic versioning** (`MAJOR.MINOR.PATCH`):

- **PATCH** (`0.1.0 → 0.1.1`): bug fixes, no behaviour change
- **MINOR** (`0.1.0 → 0.2.0`): new features, backwards-compatible
- **MAJOR** (`0.1.0 → 1.0.0`): breaking changes

You bumped versions during the merge-conflict lab — now you know what those
numbers *mean*.

## 5. Build it and (test-)publish it (rest → exercises)

```bash
python -m pip install build twine
python -m build            # creates dist/*.whl and dist/*.tar.gz
```

To publish to the sandbox index you'll make a free **TestPyPI** account and use
an API token. Full steps are in [`exercises.md`](exercises.md).

> **Note:** package names on TestPyPI are unique, so you'll rename yours to
> something like `firstpr-yourhandle` before uploading.

### Key terms from this session

- **wheel / sdist** — the two distribution formats
- **PyPI / TestPyPI** — the real index / the practice sandbox
- **`pyproject.toml`** — the single source of build + metadata truth
- **extras** — optional dependency groups (`pip install ".[dev]"`)
- **semantic versioning** — MAJOR.MINOR.PATCH
