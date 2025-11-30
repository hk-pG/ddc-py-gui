# Research: CI/CD for Linux Release

**Feature**: CI/CD for Linux Release
**Status**: Complete

## Unknowns & Clarifications

### 1. GitHub Action for Release
**Question**: Which action to use for creating releases?
**Decision**: Use `softprops/action-gh-release`.
**Rationale**: It is a widely used, stable, and simple action for creating releases and uploading assets. It handles the creation of the release from the tag automatically.
**Alternatives**: `actions/create-release` (deprecated), `ncipollo/release-action` (more features but maybe overkill).

### 2. Build Environment
**Question**: What dependencies are needed for PyInstaller on Linux?
**Decision**: Standard `ubuntu-latest` runner usually has necessary build tools. We might need `python3-dev` if compiling C extensions, but for pure Python + PyInstaller, standard setup is usually enough.
**Rationale**: Keep it simple first. If build fails due to missing libs, we add them.

### 3. Versioning
**Question**: How to extract version for the build?
**Decision**: The tag name (e.g., `v1.0.0`) will be the source of truth.
**Rationale**: Standard practice.

## Technology Choices

| Component | Choice | Rationale |
| diff | --- | --- |
| Workflow Trigger | `push: tags: ['v*']` | Standard for release workflows. |
| Runner | `ubuntu-latest` | Target platform is Linux. |
| Python Setup | `actions/setup-python@v5` | Official action, reliable. |
| Build Tool | `PyInstaller` | Already used in project. |
| Release Action | `softprops/action-gh-release@v1` | Community standard, easy to use. |

## Implementation Strategy

1.  Create `.github/workflows/release.yml`.
2.  Define job `build-and-release`.
3.  Steps:
    *   Checkout
    *   Setup Python
    *   Install dependencies (requirements.txt + dev tools)
    *   Run Tests (pytest)
    *   Run Linters (ruff)
    *   Build (pyinstaller)
    *   Release (upload `dist/ddc-control`)

