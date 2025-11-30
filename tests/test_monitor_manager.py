from unittest.mock import MagicMock, patch
import sys
import os

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from core.monitor_manager import MonitorManager, MonitorWrapper

def test_monitor_wrapper_defaults():
    m = MonitorWrapper(name="Test")
    assert m.name == "Test"
    assert m.get_brightness() == 50
    assert m.get_contrast() == 50

def test_monitor_wrapper_set_values():
    m = MonitorWrapper(name="Test")
    m.set_brightness(80)
    assert m.get_brightness() == 80
    m.set_contrast(60)
    assert m.get_contrast() == 60

@patch('core.monitor_manager.monitorcontrol')
def test_manager_get_monitors_mock(mock_mc):
    # Setup mock
    mock_monitor = MagicMock()
    mock_mc.get_monitors.return_value = [mock_monitor]
    
    manager = MonitorManager()
    # Force HAS_MONITORCONTROL to True for this test if it was False
    import core.monitor_manager
    core.monitor_manager.HAS_MONITORCONTROL = True
    
    monitors = manager.get_monitors()
    assert len(monitors) == 1
    assert isinstance(monitors[0], MonitorWrapper)

def test_manager_fallback():
    # Test fallback when monitorcontrol is missing or returns nothing
    import core.monitor_manager
    core.monitor_manager.HAS_MONITORCONTROL = False
    
    manager = MonitorManager()
    monitors = manager.get_monitors()
    assert len(monitors) >= 1
    assert "Mock" in monitors[0].name
