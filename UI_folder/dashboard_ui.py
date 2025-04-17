# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(950, 724)
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_main = QGridLayout(self.centralwidget)
        self.gridLayout_main.setObjectName(u"gridLayout_main")
        self.welcomeLabel = QLabel(self.centralwidget)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomeLabel.sizePolicy().hasHeightForWidth())
        self.welcomeLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_main.addWidget(self.welcomeLabel, 0, 0, 1, 1)

        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy1)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_main.addWidget(self.titleLabel, 0, 1, 1, 4)

        self.leftSidebarWidget = QWidget(self.centralwidget)
        self.leftSidebarWidget.setObjectName(u"leftSidebarWidget")
        self.leftSidebarWidget.setMaximumSize(QSize(180, 16777215))
        self.verticalLayout_sidebar = QVBoxLayout(self.leftSidebarWidget)
        self.verticalLayout_sidebar.setSpacing(6)
        self.verticalLayout_sidebar.setObjectName(u"verticalLayout_sidebar")
        self.verticalLayout_sidebar.setContentsMargins(0, 0, 0, 0)
        self.searchLineEdit = QLineEdit(self.leftSidebarWidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.verticalLayout_sidebar.addWidget(self.searchLineEdit)

        self.scrollArea_days = QScrollArea(self.leftSidebarWidget)
        self.scrollArea_days.setObjectName(u"scrollArea_days")
        self.scrollArea_days.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_days.setWidgetResizable(True)
        self.scrollAreaWidgetContents_days = QWidget()
        self.scrollAreaWidgetContents_days.setObjectName(u"scrollAreaWidgetContents_days")
        self.scrollAreaWidgetContents_days.setGeometry(QRect(0, 0, 178, 589))
        self.verticalLayout_scroll_content = QVBoxLayout(self.scrollAreaWidgetContents_days)
        self.verticalLayout_scroll_content.setObjectName(u"verticalLayout_scroll_content")
        self.verticalLayout_scroll_content.setContentsMargins(0, 0, 0, 0)
        self.listejourney = QListWidget(self.scrollAreaWidgetContents_days)
        self.listejourney.setObjectName(u"listejourney")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listejourney.sizePolicy().hasHeightForWidth())
        self.listejourney.setSizePolicy(sizePolicy2)

        self.verticalLayout_scroll_content.addWidget(self.listejourney)

        self.ajouterjournee = QPushButton(self.scrollAreaWidgetContents_days)
        self.ajouterjournee.setObjectName(u"ajouterjournee")

        self.verticalLayout_scroll_content.addWidget(self.ajouterjournee)

        self.scrollArea_days.setWidget(self.scrollAreaWidgetContents_days)

        self.verticalLayout_sidebar.addWidget(self.scrollArea_days)


        self.gridLayout_main.addWidget(self.leftSidebarWidget, 1, 0, 2, 1)

        self.frame_1 = QFrame(self.centralwidget)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_1 = QVBoxLayout(self.frame_1)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.label_1 = QLabel(self.frame_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_1.addWidget(self.label_1)

        self.description_1 = QLabel(self.frame_1)
        self.description_1.setObjectName(u"description_1")
        sizePolicy2.setHeightForWidth(self.description_1.sizePolicy().hasHeightForWidth())
        self.description_1.setSizePolicy(sizePolicy2)
        self.description_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_1.addWidget(self.description_1)


        self.gridLayout_main.addWidget(self.frame_1, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.description_2 = QLabel(self.frame_2)
        self.description_2.setObjectName(u"description_2")
        sizePolicy2.setHeightForWidth(self.description_2.sizePolicy().hasHeightForWidth())
        self.description_2.setSizePolicy(sizePolicy2)
        self.description_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.description_2)


        self.gridLayout_main.addWidget(self.frame_2, 1, 2, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.description_3 = QLabel(self.frame_3)
        self.description_3.setObjectName(u"description_3")
        sizePolicy2.setHeightForWidth(self.description_3.sizePolicy().hasHeightForWidth())
        self.description_3.setSizePolicy(sizePolicy2)
        self.description_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.description_3)


        self.gridLayout_main.addWidget(self.frame_3, 1, 3, 1, 1)

        self.rightAreaWidget = QWidget(self.centralwidget)
        self.rightAreaWidget.setObjectName(u"rightAreaWidget")
        self.verticalLayout_right = QVBoxLayout(self.rightAreaWidget)
        self.verticalLayout_right.setObjectName(u"verticalLayout_right")
        self.timelineLabel = QLabel(self.rightAreaWidget)
        self.timelineLabel.setObjectName(u"timelineLabel")
        self.timelineLabel.setMinimumSize(QSize(0, 40))
        self.timelineLabel.setFrameShape(QFrame.Shape.Box)
        self.timelineLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_right.addWidget(self.timelineLabel)

        self.button7Days = QPushButton(self.rightAreaWidget)
        self.button7Days.setObjectName(u"button7Days")

        self.verticalLayout_right.addWidget(self.button7Days)

        self.button30Days = QPushButton(self.rightAreaWidget)
        self.button30Days.setObjectName(u"button30Days")

        self.verticalLayout_right.addWidget(self.button30Days)

        self.buttonSinceStart = QPushButton(self.rightAreaWidget)
        self.buttonSinceStart.setObjectName(u"buttonSinceStart")

        self.verticalLayout_right.addWidget(self.buttonSinceStart)

        self.verticalSpacer_right = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_right.addItem(self.verticalSpacer_right)


        self.gridLayout_main.addWidget(self.rightAreaWidget, 1, 4, 1, 1)

        self.bottomLeftFrame = QFrame(self.centralwidget)
        self.bottomLeftFrame.setObjectName(u"bottomLeftFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bottomLeftFrame.sizePolicy().hasHeightForWidth())
        self.bottomLeftFrame.setSizePolicy(sizePolicy3)
        self.bottomLeftFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomLeftFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.bottomLeftFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.legraph1 = QWidget(self.bottomLeftFrame)
        self.legraph1.setObjectName(u"legraph1")

        self.verticalLayout.addWidget(self.legraph1)


        self.gridLayout_main.addWidget(self.bottomLeftFrame, 2, 1, 1, 2)

        self.bottomRightFrame = QFrame(self.centralwidget)
        self.bottomRightFrame.setObjectName(u"bottomRightFrame")
        sizePolicy3.setHeightForWidth(self.bottomRightFrame.sizePolicy().hasHeightForWidth())
        self.bottomRightFrame.setSizePolicy(sizePolicy3)
        self.bottomRightFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomRightFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.bottomRightFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.legraph2 = QWidget(self.bottomRightFrame)
        self.legraph2.setObjectName(u"legraph2")

        self.horizontalLayout.addWidget(self.legraph2)


        self.gridLayout_main.addWidget(self.bottomRightFrame, 2, 3, 1, 2)

        dashboard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dashboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 33))
        dashboard.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dashboard)
        self.statusbar.setObjectName(u"statusbar")
        dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(dashboard)

        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"Sport Tracker", None))
        self.welcomeLabel.setText(QCoreApplication.translate("dashboard", u"bienvenue", None))
        self.titleLabel.setText(QCoreApplication.translate("dashboard", u"TRACKER DE SPORT TRACK LES HABITUDE SPORTIVE :)", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("dashboard", u"recherche jours", None))
#if QT_CONFIG(tooltip)
        self.listejourney.setToolTip(QCoreApplication.translate("dashboard", u"Liste des jours", None))
#endif // QT_CONFIG(tooltip)
        self.ajouterjournee.setText(QCoreApplication.translate("dashboard", u"ajouter Journee", None))
        self.label_1.setText(QCoreApplication.translate("dashboard", u"label", None))
        self.description_1.setText(QCoreApplication.translate("dashboard", u"description", None))
        self.label_2.setText(QCoreApplication.translate("dashboard", u"label", None))
        self.description_2.setText(QCoreApplication.translate("dashboard", u"description", None))
        self.label_3.setText(QCoreApplication.translate("dashboard", u"label", None))
        self.description_3.setText(QCoreApplication.translate("dashboard", u"description", None))
        self.timelineLabel.setText(QCoreApplication.translate("dashboard", u"timeline", None))
        self.button7Days.setText(QCoreApplication.translate("dashboard", u"BOUTON sur 7 jours", None))
        self.button30Days.setText(QCoreApplication.translate("dashboard", u"BOUTON sur les 30 derniers jour", None))
        self.buttonSinceStart.setText(QCoreApplication.translate("dashboard", u"depuis la premiere date", None))
    # retranslateUi

