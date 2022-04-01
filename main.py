import time

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
import maze_puzzle as mp
import maze_dfs
import maze_bfs
import Window



App = QApplication(sys.argv)


# Get the path found by the depth first search algorithm
window = Window.Window()

sys.exit(App.exec())

