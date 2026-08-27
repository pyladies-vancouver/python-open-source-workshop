# Session 1 — Getting started in open source

**Duration:** ~50 min · **Format:** short talk + guided hands-on
**Goal:** understand what open source contribution really is, get your tools
working, and open your very first pull request before the break.

---

## 1. What counts as a contribution? (10 min)

The single biggest myth about open source is that "contributing" means writing
clever code. It doesn't. Projects run on a huge range of contributions, and
many of the most valued ones aren't code at all:

- **Documentation** — fixing typos, clarifying confusing sentences, adding examples
- **Reporting bugs** — a clear, reproducible issue is a gift to maintainers
- **Reproducing / triaging** issues other people filed
- **Reviewing** pull requests
- **Tests** — adding a missing test for an edge case
- **Answering questions** in discussions and forums
- **Translations, design, tutorials, talks**
- …and yes, code and bug fixes too

> **Takeaway:** you already have something to offer today. Your fresh-beginner
> perspective is exactly what makes docs and onboarding better.

## 2. How open source projects are organised (10 min)

A quick mental model of the people and norms you'll meet:

- **Maintainers** — steward the project, review and merge changes, set direction.
- **Contributors** — anyone who submits a change. That's you, as of today.
- **Users** — people who use the project and file issues.

Every healthy project publishes its "house rules" in a few standard files.
Learn to look for them *first* on any project:

| File | What it tells you |
|------|-------------------|
| `README` | What the project is and how to start |
| `CONTRIBUTING` | How *this* project wants changes submitted |
| `CODE_OF_CONDUCT` | The behavioural expectations |
| `LICENSE` | What you're allowed to do with the code |
| `good first issue` label | Curated beginner-friendly tasks |

This very repository has all of them — open [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md)
and [`../../CODE_OF_CONDUCT.md`](../../CODE_OF_CONDUCT.md) now and skim them.

## 3. Your toolkit (10 min)

You need three things. We'll confirm each is working in the exercises:

1. **Python 3.9+** — check with `python --version`
2. **git** — check with `git --version`
3. **A GitHub account** — free at <https://github.com>

We use **git** (the version-control tool on your machine) and **GitHub** (the
website that hosts projects and pull requests). They're related but not the
same — Session 3 goes deep on both.

## 4. The shape of a first contribution (5 min)

Every contribution, from a one-character typo to a big feature, follows the same
path. Here it is in one breath, so it's familiar when we do it for real:

> **fork** the project → **clone** your fork → make a **branch** → change something →
> **commit** → **push** → open a **pull request** → respond to **review** → get **merged** 🎉

Don't worry about memorising the commands yet. Today you'll walk the whole path
once, on the easiest possible change: adding your name to `CONTRIBUTORS.md`.

## 5. Now: open your first PR (rest of session → exercises)

Head to [`exercises.md`](exercises.md). By the end you will have opened a real
pull request against this repository. That's the milestone for Session 1.

### Key terms from this session

- **Contribution** — any accepted improvement to a project, code or not
- **Maintainer / contributor / user** — the three main roles
- **Pull request (PR)** — a proposed change you ask maintainers to merge
- **`good first issue`** — a label marking beginner-friendly work
