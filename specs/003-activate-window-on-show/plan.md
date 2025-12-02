# Implementation Plan: Activate Window on Show

**Branch**: `003-activate-window-on-show` | **Date**: 2025-12-02 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/003-activate-window-on-show/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

The goal is to ensure the application window is brought to the foreground and gains input focus when the "Show" action is triggered from the system tray. Currently, `self.show()` is called, which may not activate the window if it is already visible but obscured. The implementation will involve adding a method to `MainWindow` that handles showing, raising, and activating the window, and connecting the tray action to this method.

## Technical Context

**Language/Version**: Python 3.10+ (inferred from environment)
**Primary Dependencies**: PyQt6, monitorcontrol
**Storage**: N/A
**Testing**: pytest, pytest-qt (likely needed for GUI testing)
**Target Platform**: Linux (Pop!_OS/GNOME/X11/Wayland)
**Project Type**: Desktop GUI Application
**Performance Goals**: Immediate response to user action (<100ms)
**Constraints**: Must work reliably across different Linux window managers (though primarily targeting the user's environment).
**Scale/Scope**: Small change in `src/gui/main_window.py`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Code Quality**: Changes must adhere to PEP 8 and include type hints.
- **User Experience**: Directly addresses "Intuitive Controls" and responsiveness.
- **Testing**: Should add a test case if possible, though GUI focus testing can be flaky in CI.
- **Communication**: Commit messages in English, user interaction in Japanese (already established).

## Project Structure

### Documentation (this feature)

```text
specs/003-activate-window-on-show/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output (likely empty/minimal)
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (N/A)
└── tasks.md             # Phase 2 output
```

### Source Code (repository root)

```text
src/
├── core/
│   └── monitor_manager.py
└── gui/
    ├── main_window.py   # Target for modification
    └── monitor_widget.py

tests/
├── test_monitor_manager.py
└── test_system_tray.py  # Potential location for new tests
```

**Structure Decision**: Modify existing `src/gui/main_window.py`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

N/A

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
