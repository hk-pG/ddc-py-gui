import logging
from typing import List

# Try to import monitorcontrol, but handle if it's missing (for now)
try:
    import monitorcontrol

    HAS_MONITORCONTROL = True
except ImportError:
    HAS_MONITORCONTROL = False

logger = logging.getLogger(__name__)


class MonitorWrapper:
    def __init__(self, monitor_obj=None, display_id=None, name="Generic Display"):
        self.monitor = monitor_obj
        self.display_id = display_id
        self.name = name
        self.current_brightness = 50
        self.current_contrast = 50

    def get_brightness(self) -> int:
        if self.monitor:
            with self.monitor:
                return self.monitor.get_luminance()
        return self.current_brightness

    def set_brightness(self, value: int):
        self.current_brightness = value
        if self.monitor:
            with self.monitor:
                self.monitor.set_luminance(value)

    def get_contrast(self) -> int:
        if self.monitor:
            with self.monitor:
                # monitorcontrol might not support contrast directly on all platforms
                # but let's try or fallback to ddcutil
                if hasattr(self.monitor, "get_contrast"):
                    return self.monitor.get_contrast()
                # If monitorcontrol doesn't expose contrast, we might need ddcutil directly
                # For now, return stored value
                pass
        return self.current_contrast

    def set_contrast(self, value: int):
        self.current_contrast = value
        if self.monitor:
            with self.monitor:
                if hasattr(self.monitor, "set_contrast"):
                    self.monitor.set_contrast(value)


class MonitorManager:
    def get_monitors(self) -> List[MonitorWrapper]:
        monitors = []
        if HAS_MONITORCONTROL:
            try:
                for m in monitorcontrol.get_monitors():
                    # Attempt to get name, fallback to ID
                    name = "Display"
                    monitors.append(MonitorWrapper(m, name=name))
            except Exception as e:
                logger.error(f"Error getting monitors: {e}")

        # Fallback or additional check using ddcutil directly if monitorcontrol fails or is missing
        if not monitors:
            # Mock for testing if no monitors found or env missing
            monitors.append(MonitorWrapper(name="Mock Display 1"))
            monitors.append(MonitorWrapper(name="Mock Display 2"))

        return monitors
