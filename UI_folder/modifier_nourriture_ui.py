# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Modifier_nourriture.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ModifyFoodView(object):
    def setupUi(self, ModifyFoodView):
        if not ModifyFoodView.objectName():
            ModifyFoodView.setObjectName(u"ModifyFoodView")
        ModifyFoodView.resize(480, 550)
        ModifyFoodView.setStyleSheet(u"/* === Global Styles === */\n"
"QWidget#ModifyFoodView {\n"
"    background-color: #F5F5F7; /* Consistent light gray background */\n"
"}\n"
"\n"
"QWidget {\n"
"    color: #333333; /* Default text color */\n"
"    /* font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif; */\n"
"}\n"
"\n"
"/* === Frame Styling (Cards) === */\n"
"QFrame#inputFrame { /* Specific ID for the input area frame */\n"
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
"    alignment: AlignCenter;\n"
"}\n"
"\n"
"/* Section Header Labels inside Frames */\n"
"QLabel#nutritionLa"
                        "bel { /* Style for the nutrition section label */\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"    color: #444444;\n"
"    background-color: transparent; /* Ensure no frame bg */\n"
"    border: none; /* Ensure no frame border */\n"
"    padding: 4px 0; /* Small padding */\n"
"    margin-top: 10px; /* Add space above nutrition section */\n"
"}\n"
"\n"
"/* Labels within the form layout */\n"
"QFormLayout QLabel {\n"
"   font-size: 10pt;\n"
"   padding-top: 4px; /* Align labels better with spin boxes */\n"
"   background-color: transparent;\n"
"   border: none;\n"
"}\n"
"\n"
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
"QPushButton#saveButton { /* Explicit style for save */\n"
"    background-color: #007AFF;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
""
                        "    border-radius: 5px;\n"
"    padding: 8px 16px;\n"
"    min-height: 24px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton#saveButton:hover {\n"
"    background-color: #3395FF;\n"
"}\n"
"QPushButton#saveButton:pressed {\n"
"    background-color: #005ECB;\n"
"}\n"
"QPushButton#saveButton:disabled {\n"
"     background-color: #DCDCDC;\n"
"     color: #A0A0A0;\n"
"}\n"
"\n"
"/* Back/Cancel Button (Link style) */\n"
"QPushButton#cancelButton {\n"
"    background: transparent;\n"
"    color: #007AFF;\n"
"    font-size: 11pt; /* Standard size */\n"
"    font-weight: normal;\n"
"    border: none;\n"
"    padding: 5px 0px; /* Minimal padding */\n"
"    min-height: 20px;\n"
"    text-align: left; /* Align text left */\n"
"    qproperty-flat: true; /* Make it look flat like the original back button */\n"
"}\n"
"QPushButton#cancelButton:hover {\n"
"    background: transparent; /* No background change */\n"
"    color: #005ECB; /* Darker blue on hover */\n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton#cancelBu"
                        "tton:pressed {\n"
"    background: transparent; /* No background change */\n"
"    text-decoration: underline;\n"
"}\n"
"\n"
"\n"
"/* Delete Button (Destructive action style - Red) */\n"
"QPushButton#deleteFoodButton { /* Specific ID for delete food */\n"
"    background: transparent;\n"
"    border: 1px solid #FF3B30; /* Red border */\n"
"    color: #FF3B30; /* Red text */\n"
"    border-radius: 5px; /* Consistent radius */\n"
"    padding: 8px 16px; /* Standard padding */\n"
"    min-height: 24px;\n"
"    font-weight: 500; /* Medium weight */\n"
"}\n"
"QPushButton#deleteFoodButton:hover {\n"
"    background-color: rgba(255, 59, 48, 0.08); /* Very subtle red background */\n"
"    border-color: #E02010;\n"
"    color: #E02010;\n"
"}\n"
"QPushButton#deleteFoodButton:pressed {\n"
"    background-color: rgba(255, 59, 48, 0.15); /* Slightly more visible red background */\n"
"}\n"
"\n"
"/* === Input Field Styling === */\n"
"QLineEdit, QDoubleSpinBox {\n"
"    border: 1px solid #D0D0D0;\n"
"    border-radius: 4px;\n"
""
                        "    padding: 6px 8px;\n"
"    background-color: #FFFFFF;\n"
"    font-size: 10pt;\n"
"    min-height: 22px; /* Ensure decent height */\n"
"}\n"
"QLineEdit:focus, QDoubleSpinBox:focus {\n"
"    border-color: #007AFF; /* Highlight focus */\n"
"}\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {\n"
"     /* Optional: style spinbox buttons if needed */\n"
"     width: 16px;\n"
"     border-left: 1px solid #D0D0D0;\n"
"     /* background-color: #F0F0F0; */\n"
"}\n"
"QDoubleSpinBox::up-arrow, QDoubleSpinBox::down-arrow {\n"
"     /* Optional: style spinbox arrows */\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"/* === Scroll Bar Styling (Included for completeness, though not strictly necessary for this short form) === */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #FFFFFF; /* Match frame background */\n"
"    width: 8px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #CFCFCF; /* Lighter handle for content areas */\n"
"    min-"
                        "height: 25px;\n"
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
"}")
        self.mainLayout = QVBoxLayout(ModifyFoodView)
        self.mainLayout.setSpacing(15)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 15, 20, 20)
        self.cancelButton = QPushButton(ModifyFoodView)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancelButton.setFlat(True)

        self.mainLayout.addWidget(self.cancelButton)

        self.headerLabel = QLabel(ModifyFoodView)
        self.headerLabel.setObjectName(u"headerLabel")
        self.headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.headerLabel.setWordWrap(True)

        self.mainLayout.addWidget(self.headerLabel)

        self.inputFrame = QFrame(ModifyFoodView)
        self.inputFrame.setObjectName(u"inputFrame")
        self.inputFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.inputFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.inputLayout = QVBoxLayout(self.inputFrame)
        self.inputLayout.setSpacing(12)
        self.inputLayout.setObjectName(u"inputLayout")
        self.inputLayout.setContentsMargins(12, 12, 12, 12)
        self.nameFormLayout = QFormLayout()
        self.nameFormLayout.setObjectName(u"nameFormLayout")
        self.nameLabel = QLabel(self.inputFrame)
        self.nameLabel.setObjectName(u"nameLabel")

        self.nameFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.inputFrame)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.nameFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameLineEdit)


        self.inputLayout.addLayout(self.nameFormLayout)

        self.nutritionFormLayout = QFormLayout()
        self.nutritionFormLayout.setObjectName(u"nutritionFormLayout")
        self.nutritionFormLayout.setVerticalSpacing(8)

        self.inputLayout.addLayout(self.nutritionFormLayout)


        self.mainLayout.addWidget(self.inputFrame)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(8)
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer_buttons = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer_buttons)

        self.saveButton = QPushButton(ModifyFoodView)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.buttonLayout.addWidget(self.saveButton)


        self.mainLayout.addLayout(self.buttonLayout)


        self.retranslateUi(ModifyFoodView)

        QMetaObject.connectSlotsByName(ModifyFoodView)
    # setupUi

    def retranslateUi(self, ModifyFoodView):
        ModifyFoodView.setWindowTitle(QCoreApplication.translate("ModifyFoodView", u"Modify Food Item", None))
        self.cancelButton.setText(QCoreApplication.translate("ModifyFoodView", u"< Cancel", None))
        self.headerLabel.setText(QCoreApplication.translate("ModifyFoodView", u"modifier nourriture", None))
        self.nameLabel.setText(QCoreApplication.translate("ModifyFoodView", u"changer portion", None))
        self.saveButton.setText(QCoreApplication.translate("ModifyFoodView", u"Save Changes", None))
    # retranslateUi

