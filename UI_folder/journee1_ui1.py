# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'journee1.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_DayView(object):
    def setupUi(self, DayView):
        if not DayView.objectName():
            DayView.setObjectName(u"DayView")
        DayView.resize(566, 757)
        self.mainLayout = QVBoxLayout(DayView)
        self.mainLayout.setSpacing(15)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 15, 20, 20)
        self.backButton = QPushButton(DayView)
        self.backButton.setObjectName(u"backButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backButton.setFlat(True)

        self.mainLayout.addWidget(self.backButton)

        self.headerLabel = QLabel(DayView)
        self.headerLabel.setObjectName(u"headerLabel")
        self.headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.headerLabel.setWordWrap(True)

        self.mainLayout.addWidget(self.headerLabel)

        self.exerciseFrame = QFrame(DayView)
        self.exerciseFrame.setObjectName(u"exerciseFrame")
        self.exerciseFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.exerciseFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.exerciseLayout = QVBoxLayout(self.exerciseFrame)
        self.exerciseLayout.setSpacing(8)
        self.exerciseLayout.setObjectName(u"exerciseLayout")
        self.exerciseLayout.setContentsMargins(12, 12, 12, 12)
        self.exercisesLabel = QLabel(self.exerciseFrame)
        self.exercisesLabel.setObjectName(u"exercisesLabel")
        self.exercisesLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.exerciseLayout.addWidget(self.exercisesLabel)

        self.exercisesScrollArea = QScrollArea(self.exerciseFrame)
        self.exercisesScrollArea.setObjectName(u"exercisesScrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.exercisesScrollArea.sizePolicy().hasHeightForWidth())
        self.exercisesScrollArea.setSizePolicy(sizePolicy1)
        self.exercisesScrollArea.setMinimumSize(QSize(0, 150))
        self.exercisesScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 500, 150))
        self.scrollAreaLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setSpacing(0)
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")
        self.scrollAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.exercisesList = QListWidget(self.scrollAreaWidgetContents)
        self.exercisesList.setObjectName(u"exercisesList")

        self.scrollAreaLayout.addWidget(self.exercisesList)

        self.exercisesScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.exerciseLayout.addWidget(self.exercisesScrollArea)

        self.exBtnLayout = QHBoxLayout()
        self.exBtnLayout.setSpacing(8)
        self.exBtnLayout.setObjectName(u"exBtnLayout")
        self.horizontalSpacer_ex = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.exBtnLayout.addItem(self.horizontalSpacer_ex)

        self.addExerciseButton = QPushButton(self.exerciseFrame)
        self.addExerciseButton.setObjectName(u"addExerciseButton")

        self.exBtnLayout.addWidget(self.addExerciseButton)

        self.removeExerciseButton = QPushButton(self.exerciseFrame)
        self.removeExerciseButton.setObjectName(u"removeExerciseButton")

        self.exBtnLayout.addWidget(self.removeExerciseButton)

        self.pushButton = QPushButton(self.exerciseFrame)
        self.pushButton.setObjectName(u"pushButton")

        self.exBtnLayout.addWidget(self.pushButton)


        self.exerciseLayout.addLayout(self.exBtnLayout)


        self.mainLayout.addWidget(self.exerciseFrame)

        self.foodFrame = QFrame(DayView)
        self.foodFrame.setObjectName(u"foodFrame")
        self.foodFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.foodFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.foodLayout = QVBoxLayout(self.foodFrame)
        self.foodLayout.setSpacing(8)
        self.foodLayout.setObjectName(u"foodLayout")
        self.foodLayout.setContentsMargins(12, 12, 12, 12)
        self.foodLabel = QLabel(self.foodFrame)
        self.foodLabel.setObjectName(u"foodLabel")
        self.foodLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.foodLayout.addWidget(self.foodLabel)

        self.foodScrollArea = QScrollArea(self.foodFrame)
        self.foodScrollArea.setObjectName(u"foodScrollArea")
        sizePolicy1.setHeightForWidth(self.foodScrollArea.sizePolicy().hasHeightForWidth())
        self.foodScrollArea.setSizePolicy(sizePolicy1)
        self.foodScrollArea.setMinimumSize(QSize(0, 150))
        self.foodScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 500, 150))
        self.scrollAreaLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.scrollAreaLayout_2.setSpacing(0)
        self.scrollAreaLayout_2.setObjectName(u"scrollAreaLayout_2")
        self.scrollAreaLayout_2.setContentsMargins(0, 0, 0, 0)
        self.foodList = QListWidget(self.scrollAreaWidgetContents_2)
        self.foodList.setObjectName(u"foodList")

        self.scrollAreaLayout_2.addWidget(self.foodList)

        self.foodScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.foodLayout.addWidget(self.foodScrollArea)

        self.foodBtnLayout = QHBoxLayout()
        self.foodBtnLayout.setSpacing(8)
        self.foodBtnLayout.setObjectName(u"foodBtnLayout")
        self.horizontalSpacer_food = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.foodBtnLayout.addItem(self.horizontalSpacer_food)

        self.addFoodButton = QPushButton(self.foodFrame)
        self.addFoodButton.setObjectName(u"addFoodButton")

        self.foodBtnLayout.addWidget(self.addFoodButton)

        self.removeFoodButton = QPushButton(self.foodFrame)
        self.removeFoodButton.setObjectName(u"removeFoodButton")

        self.foodBtnLayout.addWidget(self.removeFoodButton)

        self.pushButton_3 = QPushButton(self.foodFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: rgb(232, 233, 236)\n"
"")

        self.foodBtnLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.foodFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.foodBtnLayout.addWidget(self.pushButton_2)


        self.foodLayout.addLayout(self.foodBtnLayout)


        self.mainLayout.addWidget(self.foodFrame)

        self.verticalSpacer_bottom = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer_bottom)

        self.deleteDayButton = QPushButton(DayView)
        self.deleteDayButton.setObjectName(u"deleteDayButton")
        self.deleteDayButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.mainLayout.addWidget(self.deleteDayButton)


        self.retranslateUi(DayView)

        QMetaObject.connectSlotsByName(DayView)
    # setupUi

    def retranslateUi(self, DayView):
        DayView.setWindowTitle(QCoreApplication.translate("DayView", u"Day Details", None))
        DayView.setStyleSheet(QCoreApplication.translate("DayView", u"/* === Global Styles === */\n"
"QWidget#DayView {\n"
"    background-color: #F5F5F7; /* Consistent light gray background */\n"
"}\n"
"\n"
"QWidget {\n"
"    color: #333333; /* Default text color */\n"
"    /* font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif; */\n"
"}\n"
"\n"
"/* === Frame Styling (Cards) === */\n"
"QFrame {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px; /* Consistent radius */\n"
"}\n"
"\n"
"/* === Label Styling === */\n"
"/* Main Header Label */\n"
"QLabel#headerLabel {\n"
"    font-size: 18pt; /* Slightly smaller than original, more title-like */\n"
"    font-weight: bold; /* Bold */\n"
"    color: #222222; /* Darker text */\n"
"    padding: 5px 0; /* Vertical padding */\n"
"    margin-bottom: 5px; /* Space below header */\n"
"}\n"
"\n"
"/* Section Header Labels inside Frames */\n"
"#exercisesLabel, #foodLabel {\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"    color: #444444;\n"
" "
                        "   background-color: transparent; /* Ensure no frame bg */\n"
"    border: none; /* Ensure no frame border */\n"
"    padding: 4px 0; /* Small padding */\n"
"}\n"
"\n"
"/* Ensure labels inside frames don't inherit wrong styles */\n"
"QFrame QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* === Button Styling === */\n"
"/* Default Button Style (Blue) - applied if no specific ID matches */\n"
"QPushButton {\n"
"    background-color: #007AFF;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px;\n"
"    min-height: 24px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #3395FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #005ECB;\n"
"}\n"
"QPushButton:disabled {\n"
"     background-color: #DCDCDC;\n"
"     color: #A0A0A0;\n"
"}\n"
"\n"
"/* Back Button (Link style) */\n"
"QPushButton#backButton {\n"
"    background: transparent;\n"
"    color: #007AFF;\n"
""
                        "    font-size: 11pt; /* Standard size */\n"
"    font-weight: normal;\n"
"    border: none;\n"
"    padding: 5px 0px; /* Minimal padding */\n"
"    min-height: 20px;\n"
"    text-align: left; /* Align text left */\n"
"}\n"
"QPushButton#backButton:hover {\n"
"    background: transparent; /* No background change */\n"
"    color: #005ECB; /* Darker blue on hover */\n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton#backButton:pressed {\n"
"    background: transparent; /* No background change */\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"/* Add/Remove Buttons (Secondary action style - Gray) */\n"
"QPushButton#addExerciseButton, QPushButton#addFoodButton,\n"
"QPushButton#removeExerciseButton, QPushButton#removeFoodButton {\n"
"    background-color: #E9E9ED; /* Subtle gray */\n"
"    color: #333333; /* Standard text color */\n"
"    border: 1px solid #DCDCDC; /* Subtle border */\n"
"    border-radius: 5px; /* Consistent radius */\n"
"    padding: 6px 12px; /* Slightly smaller padding */\n"
"    min-h"
                        "eight: 22px;\n"
"    font-size: 10pt; /* Slightly smaller font */\n"
"    font-weight: normal;\n"
"}\n"
"QPushButton#addExerciseButton:hover, QPushButton#addFoodButton:hover,\n"
"QPushButton#removeExerciseButton:hover, QPushButton#removeFoodButton:hover {\n"
"    background-color: #DDDDDF; /* Slightly darker gray on hover */\n"
"    border-color: #CFCFCF;\n"
"}\n"
"QPushButton#addExerciseButton:pressed, QPushButton#addFoodButton:pressed,\n"
"QPushButton#removeExerciseButton:pressed, QPushButton#removeFoodButton:pressed {\n"
"    background-color: #D5D5D7; /* Even darker gray when pressed */\n"
"}\n"
"\n"
"/* Delete Button (Destructive action style - Red) */\n"
"QPushButton#deleteDayButton {\n"
"    background: transparent;\n"
"    border: 1px solid #FF3B30; /* Red border */\n"
"    color: #FF3B30; /* Red text */\n"
"    border-radius: 5px; /* Consistent radius */\n"
"    padding: 8px 16px; /* Standard padding */\n"
"    min-height: 24px;\n"
"    font-weight: 500; /* Medium weight */\n"
"}\n"
"QPushButton#delet"
                        "eDayButton:hover {\n"
"    background-color: rgba(255, 59, 48, 0.08); /* Very subtle red background */\n"
"    border-color: #E02010;\n"
"    color: #E02010;\n"
"}\n"
"QPushButton#deleteDayButton:pressed {\n"
"    background-color: rgba(255, 59, 48, 0.15); /* Slightly more visible red background */\n"
"}\n"
"\n"
"/* === List Widget Styling === */\n"
"QListWidget {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: none; /* No border for the list widget itself */\n"
"    /* border-radius: 5px; Optional: if list is directly visible */\n"
"}\n"
"QListWidget::item {\n"
"    padding: 8px 10px;\n"
"    border-bottom: 1px solid #F0F0F0;\n"
"    color: #333333; /* Ensure text color */\n"
"}\n"
"QListWidget::item:last {\n"
"    border-bottom: none;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: #007AFF;\n"
"    color: #FFFFFF;\n"
"    border-radius: 4px;\n"
"    border-bottom-color: transparent; /* Hide border line when selected */\n"
"}\n"
"QListWidget::item:hover:!selected {\n"
""
                        "     background-color: #E8F3FF;\n"
"     color: #222222;\n"
"     border-radius: 4px;\n"
"}\n"
"\n"
"/* === Scroll Area Styling === */\n"
"QScrollArea {\n"
"  border: none;\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"/* === Scroll Bar Styling === */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #FFFFFF; /* Match frame background */\n"
"    width: 8px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #CFCFCF; /* Lighter handle for content areas */\n"
"    min-height: 25px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #B0B0B0;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none; background: none; height: 0px; width: 0px;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"   ", None))
        self.backButton.setText(QCoreApplication.translate("DayView", u"\u2190 Back to Dashboard", None))
        self.headerLabel.setText(QCoreApplication.translate("DayView", u"Tuesday, April 23, 2024", None))
        self.exercisesLabel.setText(QCoreApplication.translate("DayView", u"Exercises", None))
        self.addExerciseButton.setText(QCoreApplication.translate("DayView", u"+ Add", None))
        self.removeExerciseButton.setText(QCoreApplication.translate("DayView", u"\u2212 Remove", None))
        self.pushButton.setText(QCoreApplication.translate("DayView", u"afficher exercices disponible", None))
        self.foodLabel.setText(QCoreApplication.translate("DayView", u"Food Intake", None))
        self.addFoodButton.setText(QCoreApplication.translate("DayView", u"+ Add", None))
        self.removeFoodButton.setText(QCoreApplication.translate("DayView", u"\u2212 Remove", None))
        self.pushButton_3.setText(QCoreApplication.translate("DayView", u"changer nourriture", None))
        self.pushButton_2.setText(QCoreApplication.translate("DayView", u"afficher nourriture disponible", None))
        self.deleteDayButton.setText(QCoreApplication.translate("DayView", u"Delete Day", None))
    # retranslateUi

