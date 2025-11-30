from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QSlider
from PyQt6.QtCore import Qt


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

        # Controls Layout
        controls_layout = QGridLayout()
        layout.addLayout(controls_layout)

        # Brightness Control
        self.b_label = QLabel(f"Brightness: {self.monitor.get_brightness()}")
        self.b_slider = QSlider(Qt.Orientation.Horizontal)
        self.b_slider.setRange(0, 100)
        self.b_slider.setValue(self.monitor.get_brightness())
        self.b_slider.valueChanged.connect(self.on_brightness_changed)
        controls_layout.addWidget(self.b_label, 0, 0)
        controls_layout.addWidget(self.b_slider, 0, 1)

        # Contrast Control
        self.c_label = QLabel(f"Contrast: {self.monitor.get_contrast()}")
        self.c_slider = QSlider(Qt.Orientation.Horizontal)
        self.c_slider.setRange(0, 100)
        self.c_slider.setValue(self.monitor.get_contrast())
        self.c_slider.valueChanged.connect(self.on_contrast_changed)
        controls_layout.addWidget(self.c_label, 1, 0)
        controls_layout.addWidget(self.c_slider, 1, 1)

        # Ensure sliders expand
        controls_layout.setColumnStretch(1, 1)

        # Styling
        self.setStyleSheet(
            """
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
        """
        )

    def on_brightness_changed(self, value):
        self.b_label.setText(f"Brightness: {value}")
        self.monitor.set_brightness(value)

    def on_contrast_changed(self, value):
        self.c_label.setText(f"Contrast: {value}")
        self.monitor.set_contrast(value)
