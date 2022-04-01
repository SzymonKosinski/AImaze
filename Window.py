import time

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import maze_puzzle as mp
import maze_dfs, maze_bfs
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Drawing Rectangle"
        self.top = 100
        self.left = 100
        self.width = 1000
        self.height = 800

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 400)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        self.maze = mp.MazePuzzle(20,20)

        self.draw_something(self.maze)
        #create buttom1
        self.button1 = QPushButton(self)
        self.button1.setText("dfs")
        self.button1.move(700, 600)
        self.button1.resize(100, 32)
        self.button1.clicked.connect(self.button1_clicked)

        #create button2
        self.button2 = QPushButton(self)
        self.button2.setText("bfs")
        self.button2.move(700, 632)
        self.button2.resize(100, 32)
        self.button2.clicked.connect(self.button2_clicked)

        #create button3
        self.button3 = QPushButton(self)
        self.button3.setText("new maze")
        self.button3.move(700, 664)
        self.button3.resize(100, 32)
        self.button3.clicked.connect(self.button3_clicked)

        self.InitWindow()

    def button1_clicked(self):
        self.draw_something(self.maze)
        print("Button 1 clicked")
        starting_point = mp.Point(int(self.maze.maze_size_x / 2), int(self.maze.maze_size_y / 2))
        outcome = maze_dfs.run_dfs(self.maze, starting_point, [])
        dfs_path = mp.get_path(outcome)
        for point in dfs_path[::-1]:
            print(point.x, point.y)
            self.draw_animation(point, Qt.green)
            time.sleep(0.1)
            self.draw_animation(point, Qt.yellow)

    def button2_clicked(self):
        self.draw_something(self.maze)
        print("Button 2 clicked")
        starting_point = mp.Point(int(self.maze.maze_size_x / 2), int(self.maze.maze_size_y / 2))
        outcome = maze_bfs.run_bfs(self.maze, starting_point, [])
        dfs_path = mp.get_path(outcome)
        for point in dfs_path[::-1]:
            print(point.x, point.y)
            self.draw_animation(point, Qt.green)
            time.sleep(0.1)
            self.draw_animation(point, Qt.yellow)

    def button3_clicked(self):
        print("Button 3 clicked")
        self.maze = mp.MazePuzzle(20,20)
        self.draw_something(self.maze)

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

        '''    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        painter.drawRect(100, 50, 400,400)
        for i in range(0,20):
            for j in range(0,20):
                painter.drawRect(100+(20*i),50+(20*j),20,20)'''
    def draw_something(self,maze):
        painter = QPainter(self.label.pixmap())
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        for i in range(0,20):
            for j in range(0,20):
                if(maze.maze[i][j]=="0"):
                    painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
                elif(maze.maze[i][j]=="*"):
                    painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
                else:
                    painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
                painter.drawRect((20*i),(20*j),20,20)
        self.label.repaint()
        painter.end()
    def draw_animation(self, point, brush):
        painter = QPainter(self.label.pixmap())
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(brush, Qt.SolidPattern))
        painter.drawRect((20 * point.x), (20 * point.y), 20, 20)
        self.label.repaint()


