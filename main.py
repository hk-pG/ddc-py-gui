import sys
import os
import logging

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow

def main():
    logging.basicConfig(level=logging.INFO)
    
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
