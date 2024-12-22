import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor


class CircleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 800, 600)

        self.circles = []
        self.pushButton = QtWidgets.QPushButton("Добавить окружность", self)
        self.pushButton.setGeometry(10, 10, 200, 30)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for (x, y, diameter, color) in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CircleApp()
    window.show()
    sys.exit(app.exec())
