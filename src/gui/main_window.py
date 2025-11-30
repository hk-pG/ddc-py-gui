from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QScrollArea, QLabel, QPushButton
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

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Title
        title = QLabel("Display Settings")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin: 10px; color: white;")
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
        refresh_btn = QPushButton("Refresh Monitors")
        refresh_btn.clicked.connect(self.refresh_monitors)
        refresh_btn.setStyleSheet("""
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
        """)
        main_layout.addWidget(refresh_btn)

        # Apply global dark theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
            QLabel {
                color: #ffffff;
            }
        """)

        self.refresh_monitors()

    def refresh_monitors(self):
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
