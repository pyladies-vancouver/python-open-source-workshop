# Session 3 — Git & GitHub for contributors

**Duration:** ~60 min · **Format:** live-along + a merge-conflict lab
**Goal:** run the full fork → PR cycle confidently, keep your fork in sync, and
survive your first merge conflict without panic.

---

## 1. git vs GitHub (5 min)

- **git** is a program on *your computer* that tracks changes to files as a
  series of snapshots (commits). It works fully offline.
- **GitHub** is a *website* that hosts git repositories and adds collaboration:
  forks, pull requests, issues, reviews, CI.

You can use git without GitHub. For contributing, you use both together.

## 2. The core vocabulary (10 min)

| Term | Meaning |
|------|---------|
| **repository (repo)** | A project tracked by git |
| **fork** | Your personal copy of someone else's repo on GitHub |
| **clone** | A local copy of a repo on your machine |
| **commit** | A saved snapshot of changes, with a message |
| **branch** | A parallel line of work; `main` is the default |
| **remote** | A named link to a repo on GitHub (`origin` = your fork) |
| **push / pull** | Send commits up / bring commits down |
| **pull request (PR)** | A request to merge your branch into the project |

The standard contributor setup has **two remotes**:

- `origin` → *your fork* (you can push here)
- `upstream` → *the original project* (you pull updates from here)

```bash
# after cloning your fork, add the original project as "upstream":
git remote add upstream https://github.com/YOUR-ORG/python-open-source-workshop.git
git remote -v      # verify: you should see origin AND upstream
```

## 3. The everyday loop (15 min)

This is the rhythm you'll repeat for every contribution:

```bash
# 1. Start from an up-to-date main
git switch main
git fetch upstream
git merge upstream/main         # bring your main level with the project

# 2. Branch for the change (one branch per idea)
git switch -c fix-word-count-tabs

# 3. Edit files, then see what changed
git status                      # what's changed / staged
git diff                        # the actual line-by-line changes

# 4. Stage and commit
git add src/firstpr/textutils.py
git commit -m "Count tab-separated words in word_count"

# 5. Push your branch to your fork
git push -u origin fix-word-count-tabs

# 6. Open the PR on GitHub (Compare & pull request banner)
```

**Reading a diff:** lines starting with `+` are additions, `-` are removals.
Green good, red gone. Always run `git diff` before you commit — it's the cheapest
bug-catcher there is.

**Good commits** are small and focused, with an imperative summary line
("Add…", "Fix…", "Update…"). If you can't summarise a commit in one line, it's
probably doing too much.

## 4. Responding to review (5 min)

Reviewers will comment. To address feedback, you **don't** open a new PR — you
just add more commits to the *same branch* and push again; the PR updates
automatically:

```bash
# make the requested change, then:
git add -A
git commit -m "Address review: rename variable for clarity"
git push
```

Review is a conversation, not a verdict. "Could you add a test?" is normal and
kind, not a rejection.

## 5. Merge conflicts (10 min)

A conflict happens when two changes touch the same lines and git can't decide
which wins. It looks like this inside the file:

```
<<<<<<< HEAD
your version of the line
=======
the other version of the line
>>>>>>> upstream/main
```

To resolve: **edit the file** so it reads correctly, **delete the `<<<`, `===`,
`>>>` marker lines**, then:

```bash
git add the-conflicted-file.py
git commit                       # completes the merge
```

Conflicts feel scary the first time and routine by the third. The lab in the
exercises gives you a safe one to practice on.

Head to [`exercises.md`](exercises.md).

### Key terms from this session

- **origin vs upstream** — your fork vs the original project
- **branch per change** — never work on `main` directly
- **`git status` / `git diff`** — your two most-used commands
- **conflict markers** `<<<<<<< ======= >>>>>>>` — edit, remove, add, commit
