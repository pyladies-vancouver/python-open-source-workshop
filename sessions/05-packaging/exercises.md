# Session 5 — Exercises

Goal: build real distribution files and publish a package to TestPyPI.

---

## Exercise 5.1 — Read the metadata 🔎

From `pyproject.toml`, answer:

1. What is the **install name** of this package?
2. Which **Python versions** does it support?
3. What are the **dev extras**, and what command installs them?
4. Which **build backend** is used?

**Checkpoint:** you can find every answer in `pyproject.toml` unaided.

---

## Exercise 5.2 — Build the distributions 📦

```bash
python -m pip install build
python -m build
ls dist/
```

You should see two files: a `.whl` (wheel) and a `.tar.gz` (sdist).

**Checkpoint:** `dist/` contains both a wheel and an sdist.

---

## Exercise 5.3 — Inspect what's inside a wheel 🧐

A wheel is just a zip file. Peek inside:

```bash
python -m zipfile -l dist/firstpr-0.1.0-py3-none-any.whl
```

Notice it contains your package modules and a metadata folder — the description,
version, and dependencies you wrote in `pyproject.toml`.

**Checkpoint:** you can see your modules listed inside the built wheel.

---

## Exercise 5.4 — Rename for TestPyPI 🏷️

TestPyPI names must be unique. In `pyproject.toml`, change:

```toml
name = "firstpr"
```

to something personal, e.g.:

```toml
name = "firstpr-yourhandle"
```

Rebuild:

```bash
rm -rf dist
python -m build
```

**Checkpoint:** the files in `dist/` now carry your unique name.

---

## Exercise 5.5 — Publish to TestPyPI 🚀

1. Create a free account at <https://test.pypi.org/account/register/>.
2. Create an **API token** at <https://test.pypi.org/manage/account/token/>.
3. Upload with twine:

   ```bash
   python -m pip install twine
   python -m twine upload --repository testpypi dist/*
   # username: __token__
   # password: paste your TestPyPI token (starts with pypi-...)
   ```

4. Install your own package from TestPyPI in a fresh environment:

   ```bash
   python -m pip install --index-url https://test.pypi.org/simple/ firstpr-yourhandle
   ```

**Checkpoint:** your package has a public page on test.pypi.org, and you
installed it by name. You've now shipped software. 🎉

> Revert the `name` change afterwards (or keep it on a branch) so the shared
> repo's `pyproject.toml` stays as `firstpr`.

---

## Stretch goal 5.6 — Add a runtime dependency 🧩

Add a small dependency (say `rich`) to `dependencies` in `pyproject.toml`, use
it in a new function, reinstall with `pip install -e .`, and confirm pip pulls
the dependency in automatically. Then remove it — this teaches you how
`dependencies` actually drives installation.
