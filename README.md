# DDC Display Control

A Python-based GUI application to control external monitor brightness and contrast using DDC/CI.

## Features

-   **Monitor Detection**: Automatically detects connected monitors.
-   **Brightness & Contrast Control**: Adjust values via sliders with numerical indicators.
-   **System Tray Integration**: Minimizes to system tray for background operation.
-   **Modern Dark UI**: Built with PyQt6 for a sleek look.

## Requirements

-   **OS**: Linux (tested on Ubuntu/Debian)
-   **Hardware**: Monitors supporting DDC/CI
-   **Permissions**: User must have access to `/dev/i2c-*` devices.

## Installation

### 1. System Dependencies

Install necessary system libraries (including `libxcb-cursor0` for Qt):

```bash
sudo apt install python3-pip python3-venv libxcb-cursor0
```

### 2. Permissions

Add your user to the `i2c` group to allow monitor control:

```bash
sudo usermod -aG i2c $USER
```

> **Note**: You must **log out and log back in** (or restart) for this change to take effect.

### 3. Python Environment

We recommend using `uv` for fast setup, but standard `pip` works too.

```bash
# Using uv (Recommended)
uv venv --python 3.10
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Usage

### Running from Source

```bash
source .venv/bin/activate
python3 main.py
```

### Running Standalone Binary

If you have the built binary (e.g., in `dist/`):

```bash
./dist/ddc-control
```

## Development

### Running Tests & Linter

Use the provided script to run `ruff` (linter) and `pytest`:

```bash
./run_checks.sh
```

### Building for Distribution

To create a standalone single-file executable using PyInstaller:

```bash
uv pip install pyinstaller
pyinstaller --name ddc-control --onefile --windowed --paths src main.py
```

The output binary will be in `dist/ddc-control`.
