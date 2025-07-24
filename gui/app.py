from PyQt5.QtWidgets import QApplication
from main_window import PortScannerGUI
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PortScannerGUI()
    window.show()
    sys.exit(app.exec_())