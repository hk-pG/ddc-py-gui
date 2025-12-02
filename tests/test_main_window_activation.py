import pytest
from unittest.mock import MagicMock, patch
import sys
import os

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from gui.main_window import MainWindow


@pytest.fixture
def mock_monitor_manager():
    with patch("gui.main_window.MonitorManager") as mock:
        yield mock


def test_activate_window_calls_correct_methods(qtbot, mock_monitor_manager):
    """
    Verify that activate_window calls the necessary Qt methods to bring the window to front.
    """
    # Arrange
    window = MainWindow()
    qtbot.addWidget(window)

    # Mock the methods on the instance to verify they are called
    # Note: Mocking PyQt methods on an instance works for verification
    window.showNormal = MagicMock()
    window.raise_ = MagicMock()
    window.activateWindow = MagicMock()

    # Act
    # This method doesn't exist yet, so this test is expected to fail
    if hasattr(window, "activate_window"):
        window.activate_window()
    else:
        pytest.fail("MainWindow does not have activate_window method")

    # Assert
    window.showNormal.assert_called_once()
    window.raise_.assert_called_once()
    window.activateWindow.assert_called_once()
