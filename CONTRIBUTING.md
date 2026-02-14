## Contributing

Thanks for your interest in `dlf4p`! Below is a short guide on how to help.

## Reporting issues

1. Check that the issue is not already reported in the Issue tracker.
2. Create a new issue with a short description.
3. Include:
   - Python version
   - package version
   - a minimal reproducible example
   - expected vs actual behavior

## Proposing changes

1. Create an issue describing the idea/task.
2. Discuss the solution before large changes.
3. Fork the repo and open a MR/PR.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

## Run example

Recommended way from the project root:

```bash
python3 -m test.main
```

## Tests and code quality

Run checks locally before opening MR/PR:

```bash
ruff check .
python -m pytest -q
```

The recommended style is PEP 8 and readability. Please:
- do not break public API without discussion;
- add examples or documentation for new features.

## MR/PR guidelines

- One MR/PR per logical change.
- Use a clear title and short description.
- If the change is notable, update `CHANGELOG`.

## Releases and versions

1. Update `VERSION` in `dlf4p/config.py`.
2. Before a release, update `CHANGELOG` (new version section and date).

## Build and publish

Install build and upload dependencies:

```bash
pip install setuptools wheel twine
```

Build:

```bash
python setup.py sdist bdist_wheel
```

Publish to PyPI:

```bash
python -m twine upload --repository pypi dist/*
```

## Contacts

Repository: https://gitlab.com/dexoron/dlf4p
Email: main@dexoron.su
Telegram: dexoron
Discord: dexoron
