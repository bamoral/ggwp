import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint
from PyQt5.QtGui import QPainter, QColor


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None

    def initUI(self):
        self.setGeometry(500, 20, 1000, 1000)
        self.setWindowTitle('Супрематизм')
        self.setMouseTracking(True)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        R = randint(20, 1000)
        self.qp.setBrush(QColor(*[randint(0, 255) for x in range(3)]))
        self.qp.drawEllipse(int(self.coords_[0] - R / 2),
                            int(self.coords_[1] - R / 2), R, R)

    def mouseMoveEvent(self, event):
        self.coords_ = [event.x(), event.y()]

    def mousePressEvent(self, event):
        self.coords_ = [event.x(), event.y()]
        if event.button() == Qt.LeftButton:
            self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
