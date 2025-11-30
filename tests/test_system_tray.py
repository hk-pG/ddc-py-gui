import pytest
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon
from unittest.mock import MagicMock, patch
import sys
import os

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from gui.main_window import MainWindow

# Fixture to create QApplication if it doesn't exist
@pytest.fixture(scope="session")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app

def test_tray_icon_creation(qapp):
    """Test that the system tray icon is created."""
    # We need to mock MonitorManager to avoid hardware calls during GUI test
    with patch('gui.main_window.MonitorManager') as MockManager:
        MockManager.return_value.get_monitors.return_value = []
        
        window = MainWindow()
        # Trigger tray creation (assuming we'll add a method or do it in init)
        # For TDD, we expect this to fail or we call a method we plan to implement
        # Let's assume we'll add a setup_tray method or it's in init.
        # Check if tray_icon exists
        assert hasattr(window, 'tray_icon')
        assert isinstance(window.tray_icon, QSystemTrayIcon)
        assert window.tray_icon.isVisible()

def test_tray_menu(qapp):
    """Test that the tray icon has a context menu with Quit."""
    with patch('gui.main_window.MonitorManager') as MockManager:
        MockManager.return_value.get_monitors.return_value = []
        window = MainWindow()
        
        assert window.tray_icon.contextMenu() is not None
        actions = window.tray_icon.contextMenu().actions()
        
        # Look for Quit action
        quit_found = False
        for action in actions:
            if "Quit" in action.text() or "Exit" in action.text():
                quit_found = True
                break
        assert quit_found

def test_close_event_minimizes(qapp):
    """Test that closing the window minimizes it (hides it) instead of exiting."""
    with patch('gui.main_window.MonitorManager') as MockManager:
        MockManager.return_value.get_monitors.return_value = []
        window = MainWindow()
        window.show()
        
        # Mock the event
        event = MagicMock()
        # We need to ensure the mock behaves like QCloseEvent if there are type checks, 
        # but Python is duck-typed. The previous error was likely due to how pytest/PyQt interacts.
        # Let's try to just call the method directly without strict type checking if possible,
        # or use a real QCloseEvent.
        from PyQt6.QtGui import QCloseEvent
        event = QCloseEvent()
        
        window.closeEvent(event)
        
        # Since we use a real event, we can't assert on event.ignore() call count directly
        # unless we mock the event object's ignore method.
        # But checking isHidden() is the real test.
        assert window.isHidden()
        assert not event.isAccepted() # ignore() sets accepted to False
