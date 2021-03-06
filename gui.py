from __future__ import unicode_literals
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect

class Ui_Widget(object):

    def setupUi(self, Widget):

        self.ksztalt = Ksztalty.Ellipse # kształ do narysowania
        self.prost = QRect(1, 1, 101, 101) #wsp prostokata
        self.kolorO = QColor(0, 0, 0)
        self.kolorW = QColor(200, 30, 40)

        self.resize(102, 102)
        self.setWindowTitle('Widżety')

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.rysujFigury(e, qp)
        qp.end()

    def rysujFigury(self, e, qp):
        qp.setPen(self.kolorO) #kolor obramowania
        qp.setBrush(self.kolorW) #wypełnienie
        qp.setRenderHint(QPainter.Antialiasing) #wygładzanie

        if self.ksztalt == Ksztalty.Rect:
            qp.drawRect(self.prost)
        elif self.ksztalt == Ksztalty.Ellipse:
            qp.drawEllipse(self.prost)
class Ksztalty:
    Rect, Ellipse, Polygon, Line = range(4)
