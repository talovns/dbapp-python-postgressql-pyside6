# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_expense.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QFormLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddExpenseDialog(object):
    def setupUi(self, AddExpenseDialog):
        if not AddExpenseDialog.objectName():
            AddExpenseDialog.setObjectName(u"AddExpenseDialog")
        AddExpenseDialog.resize(393, 206)
        AddExpenseDialog.setStyleSheet(u"background-color: rgb(95, 95, 95);")
        self.vbox = QVBoxLayout(AddExpenseDialog)
        self.vbox.setObjectName(u"vbox")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.amountEdit = QLineEdit(AddExpenseDialog)
        self.amountEdit.setObjectName(u"amountEdit")
        self.amountEdit.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.amountEdit)

        self.label = QLabel(AddExpenseDialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(55, 0))
        self.label.setStyleSheet(u"color: rgb(232, 232, 232);\n"
"background-color: rgb(71, 71, 71);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.categoryCombo = QComboBox(AddExpenseDialog)
        self.categoryCombo.setObjectName(u"categoryCombo")
        self.categoryCombo.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.categoryCombo)

        self.label1 = QLabel(AddExpenseDialog)
        self.label1.setObjectName(u"label1")
        self.label1.setMinimumSize(QSize(55, 0))
        self.label1.setStyleSheet(u"color: rgb(232, 232, 232);\n"
"background-color: rgb(71, 71, 71);")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label1)

        self.methodCombo = QComboBox(AddExpenseDialog)
        self.methodCombo.setObjectName(u"methodCombo")
        self.methodCombo.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.methodCombo)

        self.label2 = QLabel(AddExpenseDialog)
        self.label2.setObjectName(u"label2")
        self.label2.setMinimumSize(QSize(55, 0))
        self.label2.setStyleSheet(u"color: rgb(232, 232, 232);\n"
"background-color: rgb(71, 71, 71);")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label2)

        self.merchantEdit = QLineEdit(AddExpenseDialog)
        self.merchantEdit.setObjectName(u"merchantEdit")
        self.merchantEdit.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.merchantEdit)

        self.label3 = QLabel(AddExpenseDialog)
        self.label3.setObjectName(u"label3")
        self.label3.setMinimumSize(QSize(55, 0))
        self.label3.setStyleSheet(u"color: rgb(232, 232, 232);\n"
"background-color: rgb(71, 71, 71);")
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label3)

        self.dateEdit = QDateEdit(AddExpenseDialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"background-color: rgb(203, 203, 203);")
        self.dateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.dateEdit)

        self.label4 = QLabel(AddExpenseDialog)
        self.label4.setObjectName(u"label4")
        self.label4.setMinimumSize(QSize(55, 0))
        self.label4.setStyleSheet(u"color: rgb(232, 232, 232);\n"
"background-color: rgb(71, 71, 71);")
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label4)

        self.noteEdit = QLineEdit(AddExpenseDialog)
        self.noteEdit.setObjectName(u"noteEdit")
        self.noteEdit.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.noteEdit)

        self.label5 = QLabel(AddExpenseDialog)
        self.label5.setObjectName(u"label5")
        self.label5.setMinimumSize(QSize(55, 0))
        self.label5.setStyleSheet(u"color: rgb(232, 232, 232);\n"
"background-color: rgb(71, 71, 71);")
        self.label5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label5)


        self.vbox.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(AddExpenseDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"background-color: rgb(203, 203, 203);")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.vbox.addWidget(self.buttonBox)


        self.retranslateUi(AddExpenseDialog)

        QMetaObject.connectSlotsByName(AddExpenseDialog)
    # setupUi

    def retranslateUi(self, AddExpenseDialog):
        AddExpenseDialog.setWindowTitle(QCoreApplication.translate("AddExpenseDialog", u"Add expense", None))
        self.amountEdit.setPlaceholderText(QCoreApplication.translate("AddExpenseDialog", u"e.g. 12.50", None))
        self.label.setText(QCoreApplication.translate("AddExpenseDialog", u"Category", None))
        self.label1.setText(QCoreApplication.translate("AddExpenseDialog", u"Method", None))
        self.label2.setText(QCoreApplication.translate("AddExpenseDialog", u"Merchant", None))
        self.label3.setText(QCoreApplication.translate("AddExpenseDialog", u"Date", None))
        self.label4.setText(QCoreApplication.translate("AddExpenseDialog", u"Note", None))
        self.label5.setText(QCoreApplication.translate("AddExpenseDialog", u"Amount", None))
    # retranslateUi

