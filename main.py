import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.flag = False
        self.pushButton.clicked.connect(self.paint)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paint(self):
        self.flag = True
        self.update()
        # Имя элемента совпадает с objectName в QTDesigner

    def paintEvent(self, event, ):
        if self.flag:
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            # Рисуем прямоугольник заданной кистью
            scale = random.randint(10, 200)
            qp.drawEllipse(100, 100, scale, scale)
            qp.end()
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
