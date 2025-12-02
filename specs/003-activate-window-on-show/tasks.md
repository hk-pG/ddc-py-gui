# Tasks: Activate Window on Show

**Feature Branch**: `003-activate-window-on-show`
**Spec**: [spec.md](spec.md)
**Plan**: [plan.md](plan.md)

## Phase 1: Setup
*Goal: Prepare environment for development and testing.*

- [x] T001 Add `pytest-qt` to `requirements.txt` for GUI testing support

## Phase 2: Foundational
*Goal: Core infrastructure required for all user stories.*

*(No foundational tasks required for this feature)*

## Phase 3: User Story 1 - Activate Window from Tray
*Goal: Ensure window is brought to front and focused when "Show" is clicked.*

**Independent Test**: Run `pytest tests/test_main_window_activation.py` to verify the activation sequence is called. Manually verify by minimizing app and clicking "Show" in tray.

- [x] T002 [US1] Create test file `tests/test_main_window_activation.py` with test cases for window activation sequence
- [x] T003 [US1] Implement `activate_window` method in `src/gui/main_window.py` with `showNormal()`, `raise_()`, and `activateWindow()`
- [x] T004 [US1] Update `init_tray` in `src/gui/main_window.py` to connect "Show" action to `activate_window` instead of `show`

## Phase 4: Polish & Cross-Cutting
*Goal: Final cleanup and verification.*

- [x] T005 Run full test suite to ensure no regressions
- [x] T006 Verify manual acceptance criteria (window comes to front from minimized/obscured state)

## Dependencies

- **User Story 1**: Independent.

## Implementation Strategy

1.  **Setup**: Ensure testing tools are available.
2.  **Test**: Write a test that mocks `QMainWindow` methods to verify the correct sequence is called.
3.  **Implement**: Add the helper method and update the signal connection.
4.  **Verify**: Run tests and perform manual check.
