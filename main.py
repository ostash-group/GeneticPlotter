import sys
from PyQt5.QtWidgets import QApplication, QStyleFactory
from genplotter import GenPlotter 
from PyQt5.QtCore import Qt, QDir,QFileInfo, QFile, QTextStream
import resources

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

 # setup stylesheet
    file = QFile(":resources/light_style.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    ex = GenPlotter()
    sys.exit(app.exec_())
    