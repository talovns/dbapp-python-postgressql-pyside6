# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_ReportDialog(object):
    def setupUi(self, ReportDialog):
        if not ReportDialog.objectName():
            ReportDialog.setObjectName(u"ReportDialog")
        ReportDialog.resize(720, 420)
        ReportDialog.setMinimumSize(QSize(720, 420))
        self.vbox = QVBoxLayout(ReportDialog)
        self.vbox.setObjectName(u"vbox")
        self.filters = QHBoxLayout()
        self.filters.setObjectName(u"filters")
        self.fromDate = QDateEdit(ReportDialog)
        self.fromDate.setObjectName(u"fromDate")
        self.fromDate.setStyleSheet(u"background-color: rgb(222, 222, 222);\n"
"color: rgb(0, 0, 0);")
        self.fromDate.setCalendarPopup(True)

        self.filters.addWidget(self.fromDate)

        self.toDate = QDateEdit(ReportDialog)
        self.toDate.setObjectName(u"toDate")
        self.toDate.setStyleSheet(u"background-color: rgb(222, 222, 222);\n"
"color: rgb(0, 0, 0);")
        self.toDate.setCalendarPopup(True)

        self.filters.addWidget(self.toDate)

        self.categoryCombo = QComboBox(ReportDialog)
        self.categoryCombo.setObjectName(u"categoryCombo")
        self.categoryCombo.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.filters.addWidget(self.categoryCombo)

        self.queryEdit = QLineEdit(ReportDialog)
        self.queryEdit.setObjectName(u"queryEdit")
        self.queryEdit.setStyleSheet(u"background-color: rgb(222, 222, 222);\n"
"color: rgb(0, 0, 0);")

        self.filters.addWidget(self.queryEdit)

        self.applyBtn = QPushButton(ReportDialog)
        self.applyBtn.setObjectName(u"applyBtn")
        self.applyBtn.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.filters.addWidget(self.applyBtn)

        self.sp = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.filters.addItem(self.sp)


        self.vbox.addLayout(self.filters)

        self.tableView = QTableView(ReportDialog)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color: rgb(95, 95, 95);\n"
"color: rgb(238, 238, 238);")

        self.vbox.addWidget(self.tableView)


        self.retranslateUi(ReportDialog)

        QMetaObject.connectSlotsByName(ReportDialog)
    # setupUi

    def retranslateUi(self, ReportDialog):
        ReportDialog.setWindowTitle(QCoreApplication.translate("ReportDialog", u"Report", None))
        self.queryEdit.setPlaceholderText(QCoreApplication.translate("ReportDialog", u"Search note/merchant", None))
        self.applyBtn.setText(QCoreApplication.translate("ReportDialog", u"Apply", None))
    # retranslateUi

