import os
import sys
from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
import webcolors
from PySide6 import QtWidgets, QtGui, QtCore
from PIL import Image

# Build Application
app = QtWidgets.QApplication(sys.argv)


class schemeThief(QtWidgets.QWidget):

  def __init__(self):
    super().__init__()

    # Application Title
    self.setWindowTitle('Scheme Thief')

    self.setLayout(layout)


# Create instance of prgram
widget = schemeThief()

widget.show()

sys.exit(app.exec())