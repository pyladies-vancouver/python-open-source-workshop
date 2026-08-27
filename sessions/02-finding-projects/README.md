# Session 2 — Finding projects & reading a repo

**Duration:** ~50 min · **Format:** demo + guided hunting/triage
**Goal:** be able to find a beginner-friendly project and issue, and read an
unfamiliar repository well enough to know where a change would go.

---

## 1. Where to look (10 min)

You don't have to contribute to a giant project to matter. In fact, small and
mid-sized projects are often *friendlier* and faster to respond. Good hunting
grounds:

- **Projects you already use.** The best contributions scratch your own itch.
  Which libraries do you `import` most? Start there.
- **GitHub issue search** with beginner labels:
  - `label:"good first issue" language:python`
  - `label:"help wanted" language:python`
  - `label:"documentation" language:python`
- **Curated lists:** "good first issue" aggregators, `up-for-grabs`,
  and event-driven drives like Hacktoberfest (mind the quality-not-quantity rules).
- **Your community:** PyLadies, local user groups, and project Discord/Zulip/
  mailing lists often flag beginner-friendly tasks and mentored issues.

> **Green-flag signals of a welcoming project:** recent commits, a clear
> `CONTRIBUTING.md`, labelled beginner issues, maintainers who reply kindly,
> and merged PRs from first-timers. Skim the last 10 closed PRs to feel the tone.

## 2. Reading an issue like a maintainer (10 min)

Before you touch code, make sure you understand the task. A good issue to pick:

- Is **still open** and **not already assigned** or claimed in the comments
- Has a **clear, bounded scope** (a paragraph, not a redesign)
- Has **no open PR** already addressing it (check the linked PRs)
- You can **reproduce** or at least understand

**Etiquette:** comment to say you'd like to work on it (e.g. "I'd like to try
this — is it still available?") and *then* start. Don't disappear after
claiming; if life happens, say so and un-claim.

## 3. The anatomy of a Python repository (15 min)

Open any Python project and you'll recognise the same landmarks. Using *this*
repo as the example:

```
python-open-source-workshop/
├── README.md              # start here — what & why
├── CONTRIBUTING.md        # how to contribute
├── pyproject.toml         # project metadata, dependencies, tool config
├── src/firstpr/           # the actual package code
│   ├── __init__.py        # what the package exports + version
│   ├── greetings.py
│   └── textutils.py
├── tests/                 # the test suite — mirrors the source layout
├── docs/                  # documentation source
└── .github/workflows/     # CI: what runs automatically on every PR
```

Reading strategy for an unfamiliar repo:

1. **README** → what it does, how to install, how to run.
2. **`pyproject.toml`** (or `setup.py`/`setup.cfg`) → the package name, its
   dependencies, and which tools (ruff, pytest, mypy…) the project uses.
3. **`src/` or the package folder** → the code, starting from `__init__.py` to
   see the public API.
4. **`tests/`** → often the clearest documentation of how things are *meant* to
   behave. To change behaviour, you'll usually change a test too.
5. **`.github/`** → what checks your PR will have to pass.

> **Tip:** to find where a function lives, search the repo (GitHub's `/` search,
> or `grep -rn "def word_count" src/`). To find how it's used, search its name.

## 4. From issue to plan (5 min)

Once you've picked an issue, write yourself a two-line plan before coding:

1. *Which file(s)* will I change?
2. *How will I know it worked* — which test proves it?

That habit alone will make your PRs cleaner than most.

Now go hunting in [`exercises.md`](exercises.md).

### Key terms from this session

- **`good first issue` / `help wanted`** — beginner-friendly labels
- **Claiming an issue** — commenting to signal you're working on it
- **Repo anatomy** — README, metadata, `src/`, `tests/`, `.github/`
- **Reproduce** — confirm a bug happens for you before fixing it
