# Session 1 — Exercises

By the end of these you'll have a working environment and your first pull
request. Take them one at a time; ask for help the moment you're stuck.

---

## Exercise 1.1 — Confirm your tools ✅

Run each command and check the output looks sensible:

```bash
python --version      # expect Python 3.9 or higher
git --version         # expect any recent version
```

If either is missing, flag a facilitator. Also make sure you're **logged in to
GitHub** in your browser.

**Checkpoint:** you can see version numbers for both Python and git.

---

## Exercise 1.2 — Read the house rules 📖

Open and skim these files in this repo:

- `README.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`

Write down one thing from `CONTRIBUTING.md` you didn't expect. We'll share a few
answers with the room.

**Checkpoint:** you can name where this project asks you to run `pytest` before
pushing.

---

## Exercise 1.3 — Fork & clone this repository 🍴

1. On the repo's GitHub page, click **Fork** (top-right). This makes *your own
   copy* under your account.
2. On your fork, click the green **Code** button, copy the HTTPS URL, and clone:

   ```bash
   git clone https://github.com/YOUR-USERNAME/python-open-source-workshop.git
   cd python-open-source-workshop
   ```

**Checkpoint:** you're inside the project folder on your own machine.

---

## Exercise 1.4 — Set up the environment 🧪

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -e ".[dev,docs]"
pytest
```

You should see all tests pass. That green output is your safety net for the rest
of the day.

**Checkpoint:** `pytest` reports all tests passing.

---

## Exercise 1.5 — Your first pull request 🚀

This is the big one. You'll add yourself to `CONTRIBUTORS.md`.

```bash
# 1. Make a branch named for the change
git switch -c add-my-name

# 2. Edit CONTRIBUTORS.md and add a line with your name or GitHub handle,
#    below the "Add yourself below this line" comment. Save the file.

# 3. Stage and commit
git add CONTRIBUTORS.md
git commit -m "Add <your-name> to contributors"

# 4. Push the branch to your fork
git push -u origin add-my-name
```

Now open the pull request:

5. Go to your fork on GitHub. A yellow banner offers **Compare & pull request** —
   click it.
6. Give the PR a clear title, write one sentence of description, and click
   **Create pull request**.

**Checkpoint:** your pull request page loads with a green "Able to merge" state.
Congratulations — you are officially an open source contributor. 🎉

---

## Stretch goal 1.6 — Find a real "good first issue" 🔭

Browse <https://github.com/search?q=label%3A%22good+first+issue%22+language%3APython&type=issues>
and bookmark one issue in a project that interests you. We'll come back to
choosing projects in Session 2.
