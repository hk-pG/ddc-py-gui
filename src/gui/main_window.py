from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QScrollArea,
    QLabel,
    QPushButton,
    QSystemTrayIcon,
    QMenu,
    QApplication,
)
from PyQt6.QtGui import QAction, QCloseEvent
from PyQt6.QtCore import Qt
from core.monitor_manager import MonitorManager
from gui.monitor_widget import MonitorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DDC Display Control")
        self.resize(400, 600)

        self.monitor_manager = MonitorManager()

        self.init_ui()
        self.init_tray()

    def activate_window(self):
        """
        Brings the window to the foreground and requests focus.
        This handles cases where the window is minimized or obscured.
        """
        self.showNormal()
        self.raise_()
        self.activateWindow()

    def init_tray(self):
        self.tray_icon = QSystemTrayIcon(self)
        # Use a standard icon for now, or a placeholder
        self.tray_icon.setIcon(
            self.style().standardIcon(self.style().StandardPixmap.SP_ComputerIcon)
        )

        tray_menu = QMenu()

        show_action = QAction("Show", self)
        show_action.triggered.connect(self.activate_window)
        tray_menu.addAction(show_action)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(QApplication.instance().quit)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def closeEvent(self, event: QCloseEvent):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            "DDC Display Control",
            "Application minimized to tray",
            QSystemTrayIcon.MessageIcon.Information,
            2000,
        )

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Title
        title = QLabel("Display Settings")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(
            "font-size: 18px; font-weight: bold; margin: 10px; color: white;"
        )
        main_layout.addWidget(title)

        # Scroll Area for Monitors
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background-color: #1e1e1e; }")

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_content.setLayout(self.scroll_layout)
        scroll.setWidget(self.scroll_content)

        main_layout.addWidget(scroll)

        # Refresh Button
        self.refresh_btn = QPushButton("Refresh Monitors")
        self.refresh_btn.clicked.connect(self.refresh_monitors)
        self.refresh_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #007acc;
                color: white;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005c99;
            }
            QPushButton:disabled {
                background-color: #555555;
                color: #aaaaaa;
            }
        """
        )
        main_layout.addWidget(self.refresh_btn)

        # Apply global dark theme
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #1e1e1e;
            }
            QLabel {
                color: #ffffff;
            }
        """
        )

        self.refresh_monitors()

    def refresh_monitors(self):
        # Disable button and show loading state
        self.refresh_btn.setEnabled(False)
        self.refresh_btn.setText("Scanning...")
        QApplication.processEvents()  # Force UI update

        try:
            # Clear existing widgets
            for i in range(self.scroll_layout.count()):
                widget = self.scroll_layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

            # Get monitors
            monitors = self.monitor_manager.get_monitors()

            if not monitors:
                label = QLabel("No monitors detected")
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.scroll_layout.addWidget(label)
                return

            for monitor in monitors:
                widget = MonitorWidget(monitor)
                self.scroll_layout.addWidget(widget)
        finally:
            # Restore button state
            self.refresh_btn.setText("Refresh Monitors")
            self.refresh_btn.setEnabled(True)
