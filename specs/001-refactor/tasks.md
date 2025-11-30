# Tasks: Constitution Compliance

**Input**: Design documents from `/specs/001-refactor/`
**Prerequisites**: plan.md, spec.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and tooling setup

- [ ] T001 Install and configure dev dependencies (flake8, mypy, pytest, pytest-cov) in `requirements.txt`
- [ ] T002 Create/Update `run_checks.sh` to run linting, typing, and tests

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Ensure base structure supports refactoring

- [ ] T003 Verify directory structure and `__init__.py` files for `src/core`, `src/gui`, `tests`

## Phase 3: User Story 1 - Code Quality & Modularity (Priority: P1)

**Goal**: PEP 8 compliant, fully typed, and modular codebase.
**Independent Test**: `flake8` and `mypy` pass cleanly.

- [ ] T004 [US1] Fix PEP 8 violations in `src/core/monitor_manager.py`
- [ ] T005 [US1] Fix PEP 8 violations in `src/gui/main_window.py` and `src/gui/monitor_widget.py`
- [ ] T006 [US1] Add type hints to `src/core/monitor_manager.py`
- [ ] T007 [US1] Add type hints to `src/gui/` files
- [ ] T008 [US1] Add docstrings to all public classes and functions in `src/`
- [ ] T009 [US1] Verify strict separation: Ensure `src/core` does not import `PyQt6` or `src/gui`

## Phase 4: User Story 2 - Testing Infrastructure (Priority: P2)

**Goal**: Comprehensive unit test suite with hardware mocking.
**Independent Test**: `pytest` passes with >80% coverage on Core.

- [ ] T010 [US2] Create `tests/conftest.py` with DDC/I2C mocks
- [ ] T011 [US2] Implement unit tests for `src/core/monitor_manager.py` in `tests/test_monitor_manager.py`
- [ ] T012 [US2] Verify code coverage is > 80% for `src/core/`

## Phase 5: User Story 3 - Responsive UI & Performance (Priority: P3)

**Goal**: Non-blocking UI and efficient DDC communication.
**Independent Test**: UI remains responsive during simulated slow DDC calls.

- [ ] T013 [US3] Refactor `MonitorWidget` to use `QThread` or `QRunnable` for DDC set/get operations in `src/gui/monitor_widget.py`
- [ ] T014 [US3] Implement debouncing logic for brightness/contrast sliders in `src/gui/monitor_widget.py`

## Final Phase: Polish

- [ ] T015 Update `README.md` with new development/testing instructions
