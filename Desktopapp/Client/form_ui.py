# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(365, 270)
        icon = QIcon()
        icon.addFile(u"../Lib/Spouticon.png", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        Widget.setAutoFillBackground(True)
        Widget.setStyleSheet(u"font: 9pt \"Noto Sans\";\n"
"\n"
"QPushButton {\n"
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
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QRect(20, 10, 111, 31))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font: 700 italic 18pt \"Noto Sans\";")
        self.label_6.setPixmap(QPixmap(u"../Lib/spout4.png"))
        self.label_6.setScaledContents(True)
        self.newWindow = QPushButton(Widget)
        self.newWindow.setObjectName(u"newWindow")
        self.newWindow.setGeometry(QRect(270, 240, 91, 24))
        self.newWindow.setStyleSheet(u"QPushButton {\n"
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
        self.line = QFrame(Widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 50, 351, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 70, 321, 151))
        self.stackedWidget.setStyleSheet(u"QStackedWidget {\n"
"    border: 1px solid #3498db; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: #ffffff; /* Background color of individual pages */\n"
"    border-radius: 5px; /* Rounded corners for individual pages */\n"
"}\n"
"\n"
"")
        self.previousButton = QPushButton(Widget)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setGeometry(QRect(20, 230, 80, 24))
        self.previousButton.setStyleSheet(u"QPushButton {\n"
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
        self.nextButton = QPushButton(Widget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(110, 230, 80, 24))
        self.nextButton.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Spout", None))
        self.label_6.setText("")
        self.newWindow.setText(QCoreApplication.translate("Widget", u"Add Sprinkler", None))
        self.previousButton.setText(QCoreApplication.translate("Widget", u"Previous", None))
        self.nextButton.setText(QCoreApplication.translate("Widget", u"Next", None))
    # retranslateUi

