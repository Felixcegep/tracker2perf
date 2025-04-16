# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_UI_Base(object):
    def setupUi(self, UI_Base):
        if not UI_Base.objectName():
            UI_Base.setObjectName(u"UI_Base")
        UI_Base.resize(800, 600)
        self.centralwidget = QWidget(UI_Base)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.legraph = QWidget(self.centralwidget)
        self.legraph.setObjectName(u"legraph")

        self.horizontalLayout.addWidget(self.legraph)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        UI_Base.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(UI_Base)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        UI_Base.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(UI_Base)
        self.statusbar.setObjectName(u"statusbar")
        UI_Base.setStatusBar(self.statusbar)

        self.retranslateUi(UI_Base)

        QMetaObject.connectSlotsByName(UI_Base)
    # setupUi

    def retranslateUi(self, UI_Base):
        UI_Base.setWindowTitle(QCoreApplication.translate("UI_Base", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("UI_Base", u"test", None))
    # retranslateUi

