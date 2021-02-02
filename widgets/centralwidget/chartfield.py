
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QSplineSeries, QValueAxis
from PyQt5.QtGui import QPolygonF, QPainter, QPixmap, QMovie
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QStackedWidget , QFileDialog, QLabel
from PyQt5.QtCore import Qt,QEasingCurve, QDir
from widgets.centralwidget.welcome import WelcomePage
import numpy as np
import resources


class ChartField(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("border: 0px; border-left: 1px solid #bbbbbb; padding 0px; margin 0px; background: #cccccc;")
       
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setAnimationDuration(800)
        self.chart.setAnimationEasingCurve(QEasingCurve(QEasingCurve.Linear))

        self.chart.setAxisX(XAxis())
        self.chart.setAxisY(YAxis())
        self.chart.setTitle("<h3>Frequency of occurrence and relative position</h3>")
        self.view = QChartView(self.chart)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setStyleSheet("background:#cccccc; margin: 0px; padding: 0px;  border: 0px solid #000000;")



        self.init_movie() # self.plot
        self.welcome = WelcomePage()
        self.addWidget(self.welcome)
        self.addWidget(self.plot)



    def spinnerView(self):
        self.view.setVisible(False)
        
    def chartView(self):
        self.view.setVisible(True)

    def init_movie(self):
        self.plot = QLabel()
        self.plot.setAlignment(Qt.AlignCenter)
        self.plot.setStyleSheet("background:#cccccc; margin: 0px; padding: 0px; border: 0px; ")
        self.plot.movie = QMovie(":resources/spinner.gif")
        self.plot.movie.setSpeed(100)
        self.plot.setMovie(self.plot.movie)

        self.plot.movie.start()
        self.plot.layout1 = QVBoxLayout()
        self.plot.layout1.addWidget(self.view)
        self.plot.setLayout(self.plot.layout1)

        


    def add_data(self, xdata, ydata, color,max_value, subseq = "undefined subsequences"):

        curve = QSplineSeries()
        curve.setColor(color)
        curve.setName(subseq)

        self.chart.axisY().setMax(max_value)

        curve.setUseOpenGL(True)
        curve.append(seriesToPolyline(xdata, ydata))
        
        self.chart.addSeries(curve)
        curve.attachAxis(self.chart.axisX())
        curve.attachAxis(self.chart.axisY())
    
    def save_png(self):
        
        
        format = 'png'
        initialPath = QDir.currentPath() + "/untitled." + format

        fileName, _ = QFileDialog.getSaveFileName(self, "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (format.upper(), format))
        if bool(fileName):
            self.spinnerView()
            self.view.setStyleSheet("background: #ffffff; border: 0px;")
            p = self.view.grab()
            p.save(fileName, "PNG")
            self.view.setStyleSheet("background: #cccccc; border: 0px;")
            self.chartView()

    def save_jpg(self):

        format = 'jpg'
        initialPath = QDir.currentPath() + "/untitled." + format

        fileName, _ = QFileDialog.getSaveFileName(self, "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (format.upper(), format))
        if bool(fileName):
            self.spinnerView()
            self.view.setStyleSheet("background: #ffffff; border: 0px;")
            p = self.view.grab()
            p.save(fileName, "JPG")
            self.view.setStyleSheet("background: #cccccc; border: 0px;")
            self.chartView()




class XAxis(QValueAxis):
    def __init__(self, parent=None):
        super().__init__()
        self.setRange(0,1)
        self.setTickCount(6)
        self.setTitleText("<h3>Relative intragenic position</h3>")

class YAxis(QValueAxis):
    def __init__(self, parent=None):
        super().__init__()
        self.setMin(0)
        self.setMax(100)
        self.setLabelFormat("%6.0f ")
        self.setTitleText("<h3>Count</h3>")

        

def seriesToPolyline(xdata, ydata):

    size = len(xdata)
    polyline = QPolygonF(size)
    pointer = polyline.data()
    dtype, tinfo = np.float, np.finfo  # integers: = np.int, np.iinfo
    pointer.setsize(2*polyline.size()*tinfo(dtype).dtype.itemsize)
    memory = np.frombuffer(pointer, dtype)
    memory[:(size-1)*2+1:2] = xdata
    memory[1:(size-1)*2+2:2] = ydata
    return polyline  

