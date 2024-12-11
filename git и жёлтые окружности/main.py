import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

class CircleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(QColor(circle['color']))
            painter.drawEllipse(circle['x'], circle['y'], circle['size'], circle['size'])

    def add_circle(self):
        size = random.randint(20, 100)  # Случайный размер окружности
        x = random.randint(0, self.width() - size)
        y = random.randint(0, self.height() - size)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append({'x': x, 'y': y, 'size': size, 'color': color.name()})
        self.update()  # Обновляем виджет для перерисовки

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Drawer")
        self.setGeometry(100, 100, 800, 600)

        self.circle_drawer = CircleDrawer()
        self.setCentralWidget(self.circle_drawer)

        button = QPushButton("Добавить круг", self) # Добавление кнопки и её изменения
        button.clicked.connect(self.circle_drawer.add_circle)
        button.resize(200, 100)
        button.move(270, 10)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
