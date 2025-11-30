from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider
from PyQt6.QtCore import Qt, pyqtSignal

class MonitorWidget(QWidget):
    def __init__(self, monitor, parent=None):
        super().__init__(parent)
        self.monitor = monitor
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Monitor Name
        self.name_label = QLabel(self.monitor.name)
        self.name_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(self.name_label)

        # Brightness Control
        b_layout = QHBoxLayout()
        b_label = QLabel("Brightness")
        self.b_slider = QSlider(Qt.Orientation.Horizontal)
        self.b_slider.setRange(0, 100)
        self.b_slider.setValue(self.monitor.get_brightness())
        self.b_slider.valueChanged.connect(self.on_brightness_changed)
        b_layout.addWidget(b_label)
        b_layout.addWidget(self.b_slider)
        layout.addLayout(b_layout)

        # Contrast Control
        c_layout = QHBoxLayout()
        c_label = QLabel("Contrast")
        self.c_slider = QSlider(Qt.Orientation.Horizontal)
        self.c_slider.setRange(0, 100)
        self.c_slider.setValue(self.monitor.get_contrast())
        self.c_slider.valueChanged.connect(self.on_contrast_changed)
        c_layout.addWidget(c_label)
        c_layout.addWidget(self.c_slider)
        layout.addLayout(c_layout)

        # Styling
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
                border-radius: 8px;
                padding: 10px;
                margin-bottom: 10px;
            }
            QSlider::groove:horizontal {
                border: 1px solid #3d3d3d;
                height: 8px;
                background: #1e1e1e;
                margin: 2px 0;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #007acc;
                border: 1px solid #007acc;
                width: 18px;
                height: 18px;
                margin: -7px 0;
                border-radius: 9px;
            }
        """)

    def on_brightness_changed(self, value):
        self.monitor.set_brightness(value)

    def on_contrast_changed(self, value):
        self.monitor.set_contrast(value)
