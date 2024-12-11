import sys
import random
from PyQt5 import QtWidgets, uic, QtGui

class CircleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CircleApp, self).__init__()
        uic.loadUi('UI.ui', self)

        # Подключаем кнопку к методу
        self.pushButton.clicked.connect(self.add_circle)

        # Создаем область для рисования
        self.canvas = QtWidgets.QLabel(self)
        self.canvas.setGeometry(5, 5, 550, 700)  # Устанавливаем размер области
        self.canvas.setStyleSheet("background-color: white;")
        self.canvas.setPixmap(QtGui.QPixmap(self.canvas.size()))
        self.canvas.pixmap().fill(QtGui.QColor("orange"))

    def add_circle(self):
        # Получаем размеры области рисования
        width = self.canvas.width()
        height = self.canvas.height()

        # Генерируем случайный диаметр и позицию окружности
        diameter = random.randint(20, 100)
        x = random.randint(0, width - diameter)
        y = random.randint(0, height - diameter)

        # Рисуем окружность
        painter = QtGui.QPainter(self.canvas.pixmap())
        painter.setBrush(QtGui.QColor("yellow"))
        painter.drawEllipse(x, y, diameter, diameter)
        painter.end()

        # Обновляем виджет для отображения изменений
        self.canvas.update()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CircleApp()
    window.show()
    sys.exit(app.exec_())
