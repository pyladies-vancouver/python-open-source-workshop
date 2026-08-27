# Workshop schedule (tentative)

**Python Open Source Workshop — a one-day, ~6-hour hands-on workshop**

> Everything here is a draft and adjustable to the room. Total facilitated time
> is about 6 hours 10 minutes including breaks; the six teaching sessions are
> ~5 hours 35 minutes of that. A shorter half-day version is sketched at the
> bottom.

## Full-day running order

| Time | Block | Min | What happens |
|------|-------|-----|--------------|
| 09:00 – 09:20 | **Welcome & setup check** | 20 | Intros, goals, confirm Python/git/GitHub work, fix stragglers |
| 09:20 – 10:10 | **Session 1 — Getting started in open source** | 50 | What contribution is, community norms, **first PR** (add yourself to CONTRIBUTORS) |
| 10:10 – 11:00 | **Session 2 — Finding projects & reading a repo** | 50 | Discovery, `good first issue`, issue triage, repo anatomy |
| 11:00 – 11:15 | ☕ Break | 15 | |
| 11:15 – 12:15 | **Session 3 — Git & GitHub for contributors** | 60 | Full fork→PR cycle, remotes, diffs, **merge-conflict lab** |
| 12:15 – 13:00 | 🍱 Lunch | 45 | |
| 13:00 – 13:55 | **Session 4 — Documentation contributions** | 55 | Docstrings, Sphinx, doctests, **build docs + docs PR** |
| 13:55 – 14:05 | ☕ Break | 10 | |
| 14:05 – 15:05 | **Session 5 — Packaging** | 60 | `pyproject.toml`, wheels/sdists, **publish to TestPyPI** |
| 15:05 – 15:15 | ☕ Break | 10 | |
| 15:15 – 16:15 | **Session 6 — CI/CD** | 60 | GitHub Actions, read/extend the pipeline, **break & fix a check** |
| 16:15 – 16:30 | **Wrap-up & next steps** | 15 | Recap the full loop, pick your next real issue, Q&A |

**Totals:** teaching sessions 335 min (~5h35) · breaks + lunch 80 min ·
welcome + wrap 35 min · **workshop day ≈ 6h10 (09:00–16:30).**

## Design notes for facilitators

- **One repo, whole lifecycle.** Every hands-on task runs on this repository, so
  by 16:30 participants have personally done find → fork → branch → PR → docs →
  package → CI on a single project.
- **Each session = short teaching + hands-on**, roughly a 40/60 split. The
  `README.md` in each session folder is the teaching material; `exercises.md` is
  the hands-on part with checkpoints.
- **Buffer built in.** Sessions 3, 5, 6 get 60 min because setup friction
  (auth, tokens, first-time git) tends to land there. If a room moves fast,
  spend the slack on the stretch goals in each `exercises.md`.
- **Pre-work saves time.** Ask participants to install Python 3.9+, git, and
  create a GitHub account beforehand (see README "Setup"). Keep the 09:00 block
  for catching whoever couldn't.
- **Accessibility & pace.** Checkpoints let faster folks help neighbours or
  attempt stretch goals while others catch up — nobody is stranded.

## Shorter half-day variant (~3 hours)

If you only have a half day, run the "contribute-a-change" spine and defer
packaging/CI to a follow-up:

| Time | Block | Min |
|------|-------|-----|
| 00:00 – 00:15 | Welcome & setup check | 15 |
| 00:15 – 00:55 | Session 1 — Getting started (first PR) | 40 |
| 00:55 – 01:30 | Session 2 — Finding projects & reading a repo | 35 |
| 01:30 – 01:40 | Break | 10 |
| 01:40 – 02:40 | Session 3 — Git & GitHub (fork→PR + conflict) | 60 |
| 02:40 – 03:15 | Session 4 — Documentation (docs PR) | 35 |
| 03:15 – 03:30 | Wrap-up & where to go next | 15 |

Sessions 5 (Packaging) and 6 (CI/CD) then make an ideal standalone "part 2".
