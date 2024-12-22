import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class CircleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor('yellow'))
        for (x, y, diameter) in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CircleApp()
    window.show()
    sys.exit(app.exec())
