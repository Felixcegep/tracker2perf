# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Dashboard(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nom = QLabel(self.centralwidget)
        self.nom.setObjectName(u"nom")

        self.verticalLayout.addWidget(self.nom)

        self.taille = QLabel(self.centralwidget)
        self.taille.setObjectName(u"taille")

        self.verticalLayout.addWidget(self.taille)

        self.poid = QLabel(self.centralwidget)
        self.poid.setObjectName(u"poid")

        self.verticalLayout.addWidget(self.poid)

        self.age = QLabel(self.centralwidget)
        self.age.setObjectName(u"age")

        self.verticalLayout.addWidget(self.age)

        self.genre = QLabel(self.centralwidget)
        self.genre.setObjectName(u"genre")

        self.verticalLayout.addWidget(self.genre)

        self.listejourney = QScrollArea(self.centralwidget)
        self.listejourney.setObjectName(u"listejourney")
        self.listejourney.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 780, 386))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listejourney.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.listejourney)

        self.aller = QPushButton(self.centralwidget)
        self.aller.setObjectName(u"aller")

        self.verticalLayout.addWidget(self.aller)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.nom.setText(QCoreApplication.translate("MainWindow", u"nom", None))
        self.taille.setText(QCoreApplication.translate("MainWindow", u"taille", None))
        self.poid.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.age.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.genre.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.aller.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

