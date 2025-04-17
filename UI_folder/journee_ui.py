# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'journee.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_DayView(object):
    def setupUi(self, DayView):
        if not DayView.objectName():
            DayView.setObjectName(u"DayView")
        DayView.resize(400, 600)
        self.verticalLayout = QVBoxLayout(DayView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.navLayout = QHBoxLayout()
        self.navLayout.setObjectName(u"navLayout")
        self.backButton = QPushButton(DayView)
        self.backButton.setObjectName(u"backButton")

        self.navLayout.addWidget(self.backButton)


        self.verticalLayout.addLayout(self.navLayout)

        self.headerLabel = QLabel(DayView)
        self.headerLabel.setObjectName(u"headerLabel")
        self.headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.headerLabel)

        self.exercisesLabel = QLabel(DayView)
        self.exercisesLabel.setObjectName(u"exercisesLabel")

        self.verticalLayout.addWidget(self.exercisesLabel)

        self.exercisesScrollArea = QScrollArea(DayView)
        self.exercisesScrollArea.setObjectName(u"exercisesScrollArea")
        self.exercisesScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 190))
        self.scrollAreaLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")
        self.exercisesList = QListWidget(self.scrollAreaWidgetContents)
        self.exercisesList.setObjectName(u"exercisesList")

        self.scrollAreaLayout.addWidget(self.exercisesList)

        self.exercisesScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.exercisesScrollArea)

        self.exBtnLayout = QHBoxLayout()
        self.exBtnLayout.setObjectName(u"exBtnLayout")
        self.addExerciseButton = QPushButton(DayView)
        self.addExerciseButton.setObjectName(u"addExerciseButton")

        self.exBtnLayout.addWidget(self.addExerciseButton)

        self.removeExerciseButton = QPushButton(DayView)
        self.removeExerciseButton.setObjectName(u"removeExerciseButton")

        self.exBtnLayout.addWidget(self.removeExerciseButton)


        self.verticalLayout.addLayout(self.exBtnLayout)

        self.foodLabel = QLabel(DayView)
        self.foodLabel.setObjectName(u"foodLabel")

        self.verticalLayout.addWidget(self.foodLabel)

        self.foodScrollArea = QScrollArea(DayView)
        self.foodScrollArea.setObjectName(u"foodScrollArea")
        self.foodScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 380, 190))
        self.scrollAreaLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.scrollAreaLayout_2.setObjectName(u"scrollAreaLayout_2")
        self.foodList = QListWidget(self.scrollAreaWidgetContents_2)
        self.foodList.setObjectName(u"foodList")

        self.scrollAreaLayout_2.addWidget(self.foodList)

        self.foodScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.foodScrollArea)

        self.foodBtnLayout = QHBoxLayout()
        self.foodBtnLayout.setObjectName(u"foodBtnLayout")
        self.addFoodButton = QPushButton(DayView)
        self.addFoodButton.setObjectName(u"addFoodButton")

        self.foodBtnLayout.addWidget(self.addFoodButton)

        self.removeFoodButton = QPushButton(DayView)
        self.removeFoodButton.setObjectName(u"removeFoodButton")

        self.foodBtnLayout.addWidget(self.removeFoodButton)


        self.verticalLayout.addLayout(self.foodBtnLayout)

        self.deleteDayButton = QPushButton(DayView)
        self.deleteDayButton.setObjectName(u"deleteDayButton")

        self.verticalLayout.addWidget(self.deleteDayButton)


        self.retranslateUi(DayView)

        QMetaObject.connectSlotsByName(DayView)
    # setupUi

    def retranslateUi(self, DayView):
        self.backButton.setText(QCoreApplication.translate("DayView", u"\u2190 Back to Dashboard", None))
        self.headerLabel.setText(QCoreApplication.translate("DayView", u"Tuesday\\nApril 23, 2024", None))
        self.exercisesLabel.setText(QCoreApplication.translate("DayView", u"Exercises", None))
        self.addExerciseButton.setText(QCoreApplication.translate("DayView", u"+ Add Exercise", None))
        self.removeExerciseButton.setText(QCoreApplication.translate("DayView", u"\u2212 Remove Exercise", None))
        self.foodLabel.setText(QCoreApplication.translate("DayView", u"Food", None))
        self.addFoodButton.setText(QCoreApplication.translate("DayView", u"+ Add Food", None))
        self.removeFoodButton.setText(QCoreApplication.translate("DayView", u"\u2212 Remove Food", None))
        self.deleteDayButton.setText(QCoreApplication.translate("DayView", u"Delete Day", None))
        pass
    # retranslateUi

