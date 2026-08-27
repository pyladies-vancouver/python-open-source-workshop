# Session 6 — CI/CD

**Duration:** ~60 min · **Format:** read-the-pipeline + break-and-fix lab
**Goal:** understand what CI does, read this repo's GitHub Actions workflow line
by line, extend it, and fix a failing check on a pull request.

---

## 1. What is CI/CD, really? (10 min)

**Continuous Integration (CI)** means: every time someone pushes code or opens a
pull request, a fresh machine automatically checks out the change and runs your
tests, linters, and other checks. It's the project's immune system — it catches
problems *before* a human reviewer has to.

**Continuous Delivery/Deployment (CD)** extends that to automatically publishing
or deploying when checks pass (for a library, "deploy" often means "publish to
PyPI on a new tag"). Today we focus on CI, with a note on CD at the end.

Why contributors care:

- Your PR will show a **green check or a red X**. Reviewers often won't look
  closely until it's green.
- CI runs your change on **Python versions and operating systems you don't have**,
  catching "works on my machine" bugs.
- Reading a **CI failure log** is a core contributor skill — it tells you exactly
  what broke.

## 2. Reading this repo's pipeline (15 min)

Open [`../../.github/workflows/ci.yml`](../../.github/workflows/ci.yml) and read
along. GitHub Actions workflows are YAML files in `.github/workflows/`.

```yaml
name: CI

on:                       # WHEN it runs
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:                     # WHAT it runs (jobs run in parallel)
  lint:
    runs-on: ubuntu-latest
    steps:                # ordered steps within a job
      - uses: actions/checkout@v4        # get the code
      - uses: actions/setup-python@v5     # install Python
        with:
          python-version: "3.12"
      - run: python -m pip install ruff
      - run: ruff check .                 # fail the job if lint fails

  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:                             # run the SAME steps for each version
        python-version: ["3.9", "3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m pip install -e ".[dev]"
      - run: pytest
```

Vocabulary that unlocks the whole file:

| Term | Meaning |
|------|---------|
| **workflow** | the whole YAML file |
| **event** (`on:`) | what triggers it (push, pull_request, schedule, tag…) |
| **job** | an independent unit; jobs run in parallel by default |
| **step** | one command or action inside a job, run in order |
| **action** (`uses:`) | a reusable building block (e.g. `actions/checkout`) |
| **matrix** | run the same job across several versions/OSes |
| **runner** | the fresh virtual machine the job runs on |

## 3. Reading a red X (5 min)

When CI fails, click the **Details** link next to the failed check on the PR.
You'll land in the logs; the failed step is expanded and highlighted. The trick
is to scroll to the **first** error, not the last — later errors are often just
fallout. A failing `pytest` step shows you the exact assertion that failed, the
same output you'd see locally.

**Golden rule:** run the same checks locally *before* pushing (`pytest`,
`ruff check .`) and CI rarely surprises you.

## 4. pre-commit: catch it even earlier (5 min)

CI is the last line of defence; **pre-commit** is the first. This repo ships a
[`.pre-commit-config.yaml`](../../.pre-commit-config.yaml) that runs ruff and a
few hygiene checks *before each commit is created*:

```bash
pre-commit install     # set it up once
# now every `git commit` runs the hooks automatically
```

## 5. A word on CD (2 min)

To turn this into CD you'd add a job triggered `on: push: tags:` that builds the
package (Session 5) and uploads it to PyPI using a stored token. Same building
blocks, one more job. We won't wire real publishing today, but you'll recognise
it when you see it.

Now: extend the pipeline and fix a failing check in [`exercises.md`](exercises.md).

### Key terms from this session

- **CI / CD** — automatic checks on every change / automatic release when they pass
- **workflow / job / step / action / matrix / runner** — the Actions building blocks
- **the red X** — read the first error in the log, reproduce it locally
- **pre-commit** — local hooks that catch issues before CI does
