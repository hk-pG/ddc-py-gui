# Research: Activate Window on Show

**Feature**: Activate Window on Show
**Status**: In Progress

## Unknowns & Clarifications

### 1. Reliable Window Activation in PyQt6 on Linux
**Question**: What is the most reliable sequence of calls to ensure a window is brought to front and focused on Linux (GNOME/KDE)?
**Context**: `QMainWindow.show()` alone is insufficient if the window is already visible but obscured.
**Findings**:
- `show()`: Makes the window visible.
- `raise_()`: Stacks the widget on top of the stack.
- `activateWindow()`: Sets the active window (focus).
- `showNormal()`: Restores the window if minimized.

**Decision**: Use the following sequence:
```python
self.showNormal()  # Restores if minimized, shows if hidden
self.raise_()      # Brings to top
self.activateWindow() # Requests focus
```

### 2. Testing Window Activation
**Question**: How can we verify this behavior in automated tests?
**Context**: CI environments often run headless or with limited window managers.
**Findings**:
- `pytest-qt` allows interacting with widgets.
- We can check `QApplication.activeWindow()` or `widget.isActiveWindow()`.
- However, on some platforms/CI, `activateWindow()` might not actually grant focus due to OS restrictions.
- **Strategy**: We will write a test that calls the method and asserts that `show()`, `raise_()`, and `activateWindow()` were called (using mocks if necessary) or check state if running in a capable environment. For the purpose of this feature, manual verification (User Story 1) is the ultimate gate, but unit tests should ensure the method calls the right Qt API.

## Technology Choices

- **Framework**: PyQt6 (Existing)
- **Method**: `showNormal()` + `raise_()` + `activateWindow()`

## Best Practices

- **Responsiveness**: The action is instantaneous.
- **UX**: Do not steal focus if the user is actively typing in another critical window (hard to detect, but standard OS behavior usually prevents focus stealing if not initiated by user action. Here, the user clicked the tray, so focus stealing is expected and desired).
