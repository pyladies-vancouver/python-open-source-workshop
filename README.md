# Python Open Source Workshop

A hands-on, ~6-hour workshop that takes you from "I've never contributed to open
source" to "I've opened a real pull request, updated docs, built a package, and
watched CI run on my change."

Everything happens on **one small repository — this one.** It ships as a tiny,
working Python package called `firstpr`, complete with tests, documentation,
packaging metadata, and continuous integration. You'll practice the *entire*
contribution lifecycle on it, safely, before taking those skills to any project
you like.

> **Status: tentative / draft.** Timings, ordering, and depth are adjustable to
> the room. See [`SCHEDULE.md`](SCHEDULE.md).

## Who this is for

Anyone comfortable writing a little Python who has never (or rarely) contributed
to an open source project. No prior git, GitHub, packaging, or CI experience is
assumed.

## What you'll be able to do by the end

- Find beginner-friendly projects and issues, and read a repository confidently
- Fork, clone, branch, commit, push, and open a pull request — and update it after review
- Improve documentation and build the docs locally
- Turn code into an installable package and publish it to TestPyPI
- Read and extend a GitHub Actions CI pipeline, and fix a failing check

## The six sessions

| # | Session | You'll practice |
|---|---------|-----------------|
| 1 | [Getting started in open source](sessions/01-getting-started/) | Setup, community norms, your first PR |
| 2 | [Finding projects & reading a repo](sessions/02-finding-projects/) | Issue triage, "good first issue", repo anatomy |
| 3 | [Git & GitHub for contributors](sessions/03-git-and-github/) | The full fork → PR cycle, merge conflicts |
| 4 | [Documentation contributions](sessions/04-documentation/) | Docstrings, Sphinx, building docs, doctests |
| 5 | [Packaging](sessions/05-packaging/) | `pyproject.toml`, wheels, TestPyPI |
| 6 | [CI/CD](sessions/06-ci-cd/) | GitHub Actions, linting, reading failures |

Each session folder has a `README.md` (the teaching material) and an
`exercises.md` (what you'll do with your hands).

## Setup (do this before the workshop if you can)

You need **Python 3.9+**, **git**, and a free **GitHub account**.

```bash
# 1. Fork this repo on GitHub (button, top-right), then clone YOUR fork:
git clone https://github.com/YOUR-USERNAME/python-open-source-workshop.git
cd python-open-source-workshop

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install the package plus the dev + docs tools
python -m pip install -e ".[dev,docs]"

# 4. Confirm everything works
pytest            # tests should pass
ruff check .      # linter should be clean
```

If that all runs, you're ready. If not, bring the error to session 1 — debugging
setup together is part of the fun.

## Repository map

```
python-open-source-workshop/
├── README.md                 <- you are here
├── SCHEDULE.md               <- the tentative running order
├── CONTRIBUTING.md           <- how to contribute (you'll follow this for real)
├── CODE_OF_CONDUCT.md
├── CONTRIBUTORS.md           <- add yourself in Session 1!
├── LICENSE
├── pyproject.toml            <- packaging + tool config (Session 5)
├── .pre-commit-config.yaml   <- local checks (Session 6)
├── .github/workflows/ci.yml  <- continuous integration (Session 6)
├── src/firstpr/              <- the practice package
├── tests/                    <- its test suite
├── docs/                     <- Sphinx documentation (Session 4)
└── sessions/                 <- the curriculum, one folder per session
```

## License

Curriculum and code are released under the [MIT License](LICENSE) so you can
reuse, remix, and re-teach this workshop freely.
