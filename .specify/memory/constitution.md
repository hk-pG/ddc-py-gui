<!--
Sync Impact Report:
- Version change: 1.0.0 -> 1.1.0
- Added principles: Communication Standards (Japanese interaction, English docs)
-->
# ddc-py-gui Constitution

## Core Principles

### I. Code Quality
Code must be readable, maintainable, and robust.
- **PEP 8 Compliance**: All Python code must adhere to PEP 8 style guidelines.
- **Type Hinting**: Public function signatures must include type hints.
- **Modularity**: Strict separation of concerns between Core logic (hardware interaction) and GUI (presentation).
- **Documentation**: All public modules, classes, and functions must have docstrings.

### II. Testing Standards
Reliability is paramount for hardware control software.
- **Unit Tests**: All core logic must be covered by unit tests.
- **Mocking**: Hardware interactions (DDC/I2C) must be mocked in tests to ensure safety and reproducibility.
- **Coverage**: Aim for at least 80% code coverage for core modules.
- **CI/CD**: Tests must pass before any code is merged into the main branch.

### III. User Experience Consistency
The application must be intuitive and responsive.
- **Responsiveness**: Long-running operations (e.g., DDC communication) must never block the main GUI thread.
- **Intuitive Controls**: Use standard widgets and clear, descriptive labels.
- **System Integration**: Proper integration with the system tray and OS-level notifications.
- **Error Handling**: Errors must be reported to the user in a clear, non-technical manner where possible.

### IV. Performance Requirements
Efficiency is critical for system utilities.
- **Efficient Communication**: DDC/I2C calls are expensive; minimize them through caching and batching where appropriate.
- **Startup Time**: The application should start and be ready for interaction quickly.
- **Resource Usage**: Background monitoring processes must have minimal CPU and memory footprint.

### V. Communication Standards
Clear communication is essential for collaboration.
- **Interaction Language**: All conversational interactions with the user must be in Japanese.
- **Documentation Language**: All technical documentation, code comments, and commit messages must be in English.ただし、日本語でも分かるようにようやく程度は日本語で書いてほしい。あくまで英語で書いた上でそれを翻訳・意訳する形でよい。

## Governance

### Amendment Process
- Amendments to this constitution must be proposed via Pull Request.
- Changes require review and approval from project maintainers.
- Significant changes to principles trigger a Major version bump.

### Versioning Policy
- **Major**: Backward incompatible governance or principle redefinitions.
- **Minor**: New principles added or materially expanded guidance.
- **Patch**: Clarifications, wording, typo fixes.

### Compliance
- All Pull Requests must be reviewed against these principles.
- Non-compliant code should be rejected until fixed.

**Version**: 1.1.0 | **Ratified**: 2025-11-30 | **Last Amended**: 2025-11-30
