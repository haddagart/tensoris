---
icon: material/tag
---

# Automatic Versioning & Release Pipeline

This project employs fully automated, tag-based versioning for both Python package bundling and multi-version documentation deployment.

---

## 1. Dynamic Python Package Versioning (`hatch-vcs`)

Version strings are determined dynamically from **Git tags and branch commits** via `hatch-vcs`. You do not need to manually update version numbers in `pyproject.toml`.

### Accessing Version in Code

```python
import dl

print(dl.__version__)
# Output on tag v1.0.0:  "1.0.0"
# Output on dev branch:  "1.0.1.dev3+gabc123"
```

---

## 2. Creating a Release Tag

To create a new release and trigger the release pipeline:

```bash
# 1. Create a semver git tag (prefixed with 'v')
git tag -a v1.0.0 -m "Release version 1.0.0"

# 2. Push the tag to GitHub
git push origin v1.0.0
```

---

## 3. Automated GitHub Release & Bundling (`release.yml`)

When a `v*` tag is pushed:

1. **Build Step**: GitHub Actions builds the Python Wheel (`.whl`) and Source Distribution (`.tar.gz`) using `uv build`.
2. **Release Step**: Automatically creates a GitHub Release under Releases, generates changelog notes, and attaches the compiled build bundles.

---

## 4. Multi-Version Documentation (`mike`)

The documentation site supports version switching via **`mike`** integrated into MaterialX.

- **`main` Branch Commits**: Automatically deployed to the `dev` version selector alias.
- **`v*` Release Tags**: Automatically deployed as permanent versions (e.g. `v1.0.0`), updating the `latest` alias and version dropdown menu.

### Testing Version Deployment Locally

```bash
# Deploy a local version alias using mike
uv run mike deploy 1.0.0 latest

# Serve multi-version documentation site locally
uv run mike serve
```