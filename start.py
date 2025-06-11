import sys
from PySide2.QtWidgets import QApplication
from Texture_Map_Generator_v1 import ImageConverterApp

def main():
    app = QApplication(sys.argv)
    window = ImageConverterApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 