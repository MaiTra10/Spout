# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"../Lib/Spouticon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 260, 341, 32))
        self.buttonBox.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db; /* Button color */\n"
"    color: #ffffff; /* Text color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    border: 1px solid #2980b9; /* Border color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* Hover color */\n"
"    border: 1px solid #3498db; /* Border color on hover */\n"
"}\n"
"")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QRect(30, 10, 111, 31))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font: 700 italic 18pt \"Noto Sans\";")
        self.label_6.setPixmap(QPixmap(u"../Lib/spout4.png"))
        self.label_6.setScaledContents(True)
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 50, 351, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 40, 141, 16))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_3.setFont(font1)
        self.label_3.setMargin(2)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 130, 261, 72))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px; /* Padding inside the QLineEdit */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9; /* Border color on focus */\n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #3498db; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px; /* Padding inside the QLineEdit */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #2980b9; /* Border color on focus */\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Spout", None))
        self.label_6.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"ADD SPRINKLER", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Sprinkler Name", None))
        self.lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Seed Type", None))
    # retranslateUi

