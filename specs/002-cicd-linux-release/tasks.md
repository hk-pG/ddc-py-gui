# Task List: CI/CD for Linux Release

**Branch**: `002-cicd-linux-release`
**Spec**: [spec.md](spec.md)
**Plan**: [plan.md](plan.md)

## Phase 1: Setup
*Goal: Prepare project structure for GitHub Actions.*

- [ ] T001 Create workflows directory `.github/workflows/`

## Phase 2: Foundational
*Goal: Establish the workflow file structure.*

- [ ] T002 Create `.github/workflows/release.yml` with tag trigger configuration

## Phase 3: User Story 1 - Automated Release Creation
*Goal: Automatically build and release the application when a version tag is pushed.*
*Independent Test: Push a tag `v0.0.1-test` and verify a release is created with the binary.*

- [ ] T003 [US1] Add checkout and Python setup steps to `.github/workflows/release.yml`
- [ ] T004 [US1] Add dependency installation step (requirements.txt + dev tools) to `.github/workflows/release.yml`
- [ ] T005 [US1] Add PyInstaller build step to `.github/workflows/release.yml`
- [ ] T006 [US1] Add release step using `softprops/action-gh-release` to upload `dist/ddc-control`

## Phase 4: User Story 2 - Automated Testing
*Goal: Prevent releasing broken code by running tests before build.*
*Independent Test: Introduce a failing test, push a tag, and verify the workflow fails.*

- [ ] T007 [US2] Add `pytest` execution step before build in `.github/workflows/release.yml`
- [ ] T008 [US2] Add `ruff` linting step before build in `.github/workflows/release.yml`

## Final Phase: Polish
*Goal: Ensure configuration is correct and clean.*

- [ ] T009 Verify workflow syntax and configuration

## Dependencies

1. **Setup & Foundational** (T001, T002) -> **US1** (T003-T006)
2. **US1** (Basic Release) -> **US2** (Quality Gates) - *Technically US2 steps come before US1 steps in the final YAML execution order, but we can implement the release first and then insert the checks.*

## Implementation Strategy

We will start by creating the workflow file that simply builds and releases (MVP). Once that is working (or defined), we will add the testing layers to ensure quality. This allows us to verify the "release" mechanism first, which is the primary value, and then secure it with tests.
