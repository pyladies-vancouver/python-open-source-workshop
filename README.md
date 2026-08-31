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
| 1 | [Getting started in open source](sessions/01-getting-started/README.md) | Setup, community norms, your first PR |
| 2 | [Finding projects & reading a repo](sessions/02-finding-projects/README.md) | Issue triage, "good first issue", repo anatomy |
| 3 | [Git & GitHub for contributors](sessions/03-git-and-github/README.md) | The full fork → PR cycle, merge conflicts |
| 4 | [Documentation contributions](sessions/04-documentation/README.md) | Docstrings, Sphinx, building docs, doctests |
| 5 | [Packaging](sessions/05-packaging/README.md) | `pyproject.toml`, wheels, TestPyPI |
| 6 | [CI/CD](sessions/06-ci-cd/README.md) | GitHub Actions, linting, reading failures |

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
├── .github/workflows/docs.yml<- builds & deploys the handbook site to Pages
├── mkdocs.yml                <- config for the published handbook site
├── scripts/build_site.py     <- assembles + builds the MkDocs site
├── src/firstpr/              <- the practice package
├── tests/                    <- its test suite
├── docs/                     <- Sphinx documentation (Session 4)
└── sessions/                 <- the curriculum, one folder per session
```

## Published handbook (MkDocs + GitHub Pages)

The whole curriculum is also published as a searchable website using
[MkDocs](https://www.mkdocs.org/) with the Material theme. The site reads the
same Markdown files you see in the repo — nothing is duplicated — so the repo
and the site never drift apart.

Preview or build it locally:

```bash
python -m pip install mkdocs-material
python scripts/build_site.py serve     # live preview at http://127.0.0.1:8000
python scripts/build_site.py build     # one-off build into ./site
```

The helper script copies the curriculum into a generated `site-src/` folder
(git-ignored) and then runs MkDocs; this lets `README.md` and friends stay at
the repo root where GitHub expects them while still giving MkDocs a single
source directory.

**Deploying to GitHub Pages** happens automatically: the
[`docs.yml`](https://github.com/pyladies-vancouver/python-open-source-workshop/blob/main/.github/workflows/docs.yml) workflow builds and publishes the site
to a `gh-pages` branch on every push to `main`. One-time setup after you push:

1. Edit `mkdocs.yml` and replace `YOUR-ORG` in `site_url` and `repo_url` with
   your GitHub org/username (also update the clone URLs in this README).
2. Push to `main` so the workflow runs once (or trigger it from the **Actions**
   tab).
3. In **Settings → Pages**, set the source to **Deploy from a branch →
   `gh-pages` / (root)**.

Your handbook then lives at
`https://YOUR-ORG.github.io/python-open-source-workshop/`. You can also deploy
by hand anytime with `python scripts/build_site.py gh-deploy`.

## License

Two licenses, because this repository holds two different kinds of thing.

| What | License | |
| --- | --- | --- |
| The curriculum: `sessions/`, `SCHEDULE.md`, this README, `docs/` | **CC BY-SA 4.0** | [LICENSE-CONTENT](https://github.com/pyladies-vancouver/python-open-source-workshop/blob/main/LICENSE-CONTENT) |
| The code: `src/firstpr/`, `tests/`, `scripts/` | **MIT** | [LICENSE](https://github.com/pyladies-vancouver/python-open-source-workshop/blob/main/LICENSE) |

Copyright (c) 2026 PyLadies Vancouver.

**You may re-teach this workshop**, including commercially, and adapt it to
your own group. Two conditions come with the curriculum:

1. **Credit PyLadies Vancouver** and link back to this repository.
2. **Share adaptations under CC BY-SA 4.0 too**, so the next person to pick it
   up has the same freedom you did.

A credit line you can copy:

> "[PyLadies Vancouver Python Open Source Workshop](https://github.com/pyladies-vancouver/python-open-source-workshop)"
> by PyLadies Vancouver, licensed under
> [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
> Changes were made.

Drop the last line if you are using the material unmodified. If you are only
reusing the `firstpr` package or the build scripts, MIT applies and retaining
the copyright notice is all that is asked.
