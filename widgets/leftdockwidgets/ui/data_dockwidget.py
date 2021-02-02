# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_dockwidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        mainWidget.setObjectName("mainWidget")
        mainWidget.resize(317, 558)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWidget.sizePolicy().hasHeightForWidth())
        mainWidget.setSizePolicy(sizePolicy)
        mainWidget.setStyleSheet("light_style.qss")
        self.verticalLayout = QtWidgets.QVBoxLayout(mainWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(10, 0, 5, 10)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(mainWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.table = QtWidgets.QTableWidget(mainWidget)
        self.table.setEnabled(False)
        self.table.setMaximumSize(QtCore.QSize(16777215, 0))
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setTabKeyNavigation(False)
        self.table.setProperty("showDropIndicator", False)
        self.table.setDragDropOverwriteMode(False)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setIconSize(QtCore.QSize(20, 20))
        self.table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table.setShowGrid(False)
        self.table.setGridStyle(QtCore.Qt.DotLine)
        self.table.setObjectName("table")
        self.table.setColumnCount(5)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setDefaultSectionSize(80)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.horizontalHeader().setMinimumSectionSize(20)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(20)
        self.table.verticalHeader().setHighlightSections(False)
        self.table.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout.addWidget(self.table)

        self.retranslateUi(mainWidget)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)

    def retranslateUi(self, mainWidget):
        _translate = QtCore.QCoreApplication.translate
        mainWidget.setWindowTitle(_translate("mainWidget", "Form"))
        self.pushButton.setText(_translate("mainWidget", "Save Data"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("mainWidget", "1"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("mainWidget", "5"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("mainWidget", "3"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("mainWidget", "4"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("mainWidget", "Новый столбец"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWidget = QtWidgets.QWidget()
    ui = Ui_mainWidget()
    ui.setupUi(mainWidget)
    mainWidget.show()
    sys.exit(app.exec_())

