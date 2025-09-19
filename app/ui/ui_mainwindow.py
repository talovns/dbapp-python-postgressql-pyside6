# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(304, 217)
        MainWindow.setStyleSheet(u"background-color: rgb(95, 95, 95);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnSchema = QPushButton(self.centralwidget)
        self.btnSchema.setObjectName(u"btnSchema")
        self.btnSchema.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.verticalLayout.addWidget(self.btnSchema)

        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.verticalLayout.addWidget(self.btnAdd)

        self.btnShow = QPushButton(self.centralwidget)
        self.btnShow.setObjectName(u"btnShow")
        self.btnShow.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.verticalLayout.addWidget(self.btnShow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 304, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DB Manager", None))
        self.btnSchema.setText(QCoreApplication.translate("MainWindow", u"Create schema", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"Add data", None))
        self.btnShow.setText(QCoreApplication.translate("MainWindow", u"Show data", None))
    # retranslateUi

