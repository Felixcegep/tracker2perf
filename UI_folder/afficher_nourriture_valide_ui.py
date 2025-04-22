# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'afficher_nourriture_valide.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QFrame, QLabel, QListWidget,
    QListWidgetItem, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AvailableNourritureDialog(object):
    def setupUi(self, AvailableNourritureDialog):
        if not AvailableNourritureDialog.objectName():
            AvailableNourritureDialog.setObjectName(u"AvailableNourritureDialog")
        AvailableNourritureDialog.resize(400, 550)
        AvailableNourritureDialog.setModal(True)
        self.mainLayout = QVBoxLayout(AvailableNourritureDialog)
        self.mainLayout.setSpacing(15)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(15, 15, 15, 15)
        self.headerLabel = QLabel(AvailableNourritureDialog)
        self.headerLabel.setObjectName(u"headerLabel")
        self.headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.headerLabel.setWordWrap(True)

        self.mainLayout.addWidget(self.headerLabel)

        self.exerciseListFrame = QFrame(AvailableNourritureDialog)
        self.exerciseListFrame.setObjectName(u"exerciseListFrame")
        self.exerciseListFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.exerciseListFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.exerciseListLayout = QVBoxLayout(self.exerciseListFrame)
        self.exerciseListLayout.setSpacing(8)
        self.exerciseListLayout.setObjectName(u"exerciseListLayout")
        self.exerciseListLayout.setContentsMargins(10, 10, 10, 10)
        self.exerciseListLabel = QLabel(self.exerciseListFrame)
        self.exerciseListLabel.setObjectName(u"exerciseListLabel")
        self.exerciseListLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.exerciseListLayout.addWidget(self.exerciseListLabel)

        self.exercisesScrollArea = QScrollArea(self.exerciseListFrame)
        self.exercisesScrollArea.setObjectName(u"exercisesScrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.exercisesScrollArea.sizePolicy().hasHeightForWidth())
        self.exercisesScrollArea.setSizePolicy(sizePolicy)
        self.exercisesScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 348, 346))
        self.scrollAreaLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setSpacing(0)
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")
        self.scrollAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.availableExercisesList = QListWidget(self.scrollAreaWidgetContents)
        self.availableExercisesList.setObjectName(u"availableExercisesList")
        self.availableExercisesList.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.availableExercisesList.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        self.scrollAreaLayout.addWidget(self.availableExercisesList)

        self.exercisesScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.exerciseListLayout.addWidget(self.exercisesScrollArea)


        self.mainLayout.addWidget(self.exerciseListFrame)

        self.buttonBox = QDialogButtonBox(AvailableNourritureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.mainLayout.addWidget(self.buttonBox)


        self.retranslateUi(AvailableNourritureDialog)
        self.buttonBox.accepted.connect(AvailableNourritureDialog.accept)
        self.buttonBox.rejected.connect(AvailableNourritureDialog.reject)

        QMetaObject.connectSlotsByName(AvailableNourritureDialog)
    # setupUi

    def retranslateUi(self, AvailableNourritureDialog):
        AvailableNourritureDialog.setWindowTitle(QCoreApplication.translate("AvailableNourritureDialog", u"Available Exercises", None))
        AvailableNourritureDialog.setStyleSheet(QCoreApplication.translate("AvailableNourritureDialog", u"/* === Global Styles === */\n"
"/* Apply background to the Dialog */\n"
"QDialog#AvailableExercisesDialog {\n"
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
"    font-size: 16pt; /* Slightly smaller for dialog */\n"
"    font-weight: bold; /* Bold */\n"
"    color: #222222; /* Darker text */\n"
"    padding: 5px 0; /* Vertical padding */\n"
"    margin-bottom: 5px; /* Space below header */\n"
"}\n"
"\n"
"/* Section Header Labels inside Frames */\n"
"#exerciseListLabel { /* Specific ID for this dialog's label */\n"
"    fo"
                        "nt-size: 12pt;\n"
"    font-weight: bold;\n"
"    color: #444444;\n"
"    background-color: transparent; /* Ensure no frame bg */\n"
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
"/* Style for buttons within QDialogButtonBox if needed */\n"
"QDialogButtonBox QPushButton {\n"
"    background-color: #007AFF;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px;\n"
"    min-height: 24px;\n"
"    font-weight: 500;\n"
"}\n"
"QDialogButtonBox QPushButton:hover {\n"
"    background-color: #3395FF;\n"
"}\n"
"QDialogButtonBox QPushButton:pressed {\n"
"    background-color: #005ECB;\n"
"}\n"
"QDialogButtonBox QPushButton:disabled {\n"
"     background-color: #DCDCDC;\n"
"     color: #A0A0A0;\n"
"}\n"
""
                        "\n"
"/* Remove specific button styles not used here */\n"
"/* QPushButton#backButton { ... } */\n"
"/* QPushButton#addExerciseButton, ... { ... } */\n"
"/* QPushButton#deleteDayButton { ... } */\n"
"\n"
"\n"
"/* === List Widget Styling === */\n"
"QListWidget {\n"
"    background-color: #FFFFFF; /* White background */\n"
"    border: none; /* No border for the list widget itself */\n"
"}\n"
"QListWidget::item {\n"
"    padding: 8px 10px;\n"
"    border-bottom: 1px solid #F0F0F0;\n"
"    color: #333333; /* Ensure text color */\n"
"}\n"
"QListWidget::item:last {\n"
"    border-bottom: none;\n"
"}\n"
"/* Selection styling might not be needed if it's purely display, but kept for consistency */\n"
"QListWidget::item:selected {\n"
"    background-color: #007AFF;\n"
"    color: #FFFFFF;\n"
"    border-radius: 4px;\n"
"    border-bottom-color: transparent; /* Hide border line when selected */\n"
"}\n"
"QListWidget::item:hover:!selected {\n"
"     background-color: #E8F3FF;\n"
"     color: #222222;\n"
"     border-radiu"
                        "s: 4px;\n"
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
        self.headerLabel.setText(QCoreApplication.translate("AvailableNourritureDialog", u"aliment disponible", None))
        self.exerciseListLabel.setText(QCoreApplication.translate("AvailableNourritureDialog", u"aliment", None))
    # retranslateUi

