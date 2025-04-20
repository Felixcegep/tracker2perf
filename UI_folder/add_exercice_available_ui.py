# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_exercice_available.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_AddAvailableMovementWidget(object):
    def setupUi(self, AddAvailableMovementWidget):
        if not AddAvailableMovementWidget.objectName():
            AddAvailableMovementWidget.setObjectName(u"AddAvailableMovementWidget")
        AddAvailableMovementWidget.resize(450, 600)
        self.mainVLayout = QVBoxLayout(AddAvailableMovementWidget)
        self.mainVLayout.setSpacing(12)
        self.mainVLayout.setObjectName(u"mainVLayout")
        self.mainVLayout.setContentsMargins(20, 20, 20, 20)
        self.titleLabel = QLabel(AddAvailableMovementWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainVLayout.addWidget(self.titleLabel)

        self.nameDescFormLayout = QFormLayout()
        self.nameDescFormLayout.setObjectName(u"nameDescFormLayout")
        self.nameDescFormLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.nameDescFormLayout.setHorizontalSpacing(10)
        self.nameDescFormLayout.setVerticalSpacing(10)
        self.nomLabel = QLabel(AddAvailableMovementWidget)
        self.nomLabel.setObjectName(u"nomLabel")

        self.nameDescFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nomLabel)

        self.nomLineEdit = QLineEdit(AddAvailableMovementWidget)
        self.nomLineEdit.setObjectName(u"nomLineEdit")

        self.nameDescFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nomLineEdit)

        self.descriptionLabel = QLabel(AddAvailableMovementWidget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.nameDescFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.descriptionLabel)

        self.descriptionTextEdit = QTextEdit(AddAvailableMovementWidget)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setMinimumSize(QSize(0, 60))

        self.nameDescFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.descriptionTextEdit)


        self.mainVLayout.addLayout(self.nameDescFormLayout)

        self.musclesLabel = QLabel(AddAvailableMovementWidget)
        self.musclesLabel.setObjectName(u"musclesLabel")

        self.mainVLayout.addWidget(self.musclesLabel)

        self.musclesScrollArea = QScrollArea(AddAvailableMovementWidget)
        self.musclesScrollArea.setObjectName(u"musclesScrollArea")
        self.musclesScrollArea.setMinimumSize(QSize(0, 100))
        self.musclesScrollArea.setMaximumSize(QSize(16777215, 200))
        self.musclesScrollArea.setWidgetResizable(True)
        self.musclesScrollAreaContents = QWidget()
        self.musclesScrollAreaContents.setObjectName(u"musclesScrollAreaContents")
        self.musclesScrollAreaContents.setGeometry(QRect(0, 0, 408, 98))
        self.musclesVLayout = QVBoxLayout(self.musclesScrollAreaContents)
        self.musclesVLayout.setSpacing(4)
        self.musclesVLayout.setObjectName(u"musclesVLayout")
        self.musclesVLayout.setContentsMargins(9, 9, 9, 9)
        self.musclesVerticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.musclesVLayout.addItem(self.musclesVerticalSpacer)

        self.musclesScrollArea.setWidget(self.musclesScrollAreaContents)

        self.mainVLayout.addWidget(self.musclesScrollArea)

        self.typeLabel = QLabel(AddAvailableMovementWidget)
        self.typeLabel.setObjectName(u"typeLabel")

        self.mainVLayout.addWidget(self.typeLabel)

        self.typeRadioWidget = QWidget(AddAvailableMovementWidget)
        self.typeRadioWidget.setObjectName(u"typeRadioWidget")
        self.typeRadioHLayout = QHBoxLayout(self.typeRadioWidget)
        self.typeRadioHLayout.setSpacing(15)
        self.typeRadioHLayout.setObjectName(u"typeRadioHLayout")
        self.typeRadioHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardioRadioButton = QRadioButton(self.typeRadioWidget)
        self.cardioRadioButton.setObjectName(u"cardioRadioButton")

        self.typeRadioHLayout.addWidget(self.cardioRadioButton)

        self.musculationRadioButton = QRadioButton(self.typeRadioWidget)
        self.musculationRadioButton.setObjectName(u"musculationRadioButton")
        self.musculationRadioButton.setChecked(True)

        self.typeRadioHLayout.addWidget(self.musculationRadioButton)

        self.typeHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.typeRadioHLayout.addItem(self.typeHorizontalSpacer)


        self.mainVLayout.addWidget(self.typeRadioWidget)

        self.mainVerticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainVLayout.addItem(self.mainVerticalSpacer)

        self.buttonBoxHLayout = QHBoxLayout()
        self.buttonBoxHLayout.setObjectName(u"buttonBoxHLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonBoxHLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(AddAvailableMovementWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonBoxHLayout.addWidget(self.cancelButton)

        self.addButton = QPushButton(AddAvailableMovementWidget)
        self.addButton.setObjectName(u"addButton")

        self.buttonBoxHLayout.addWidget(self.addButton)


        self.mainVLayout.addLayout(self.buttonBoxHLayout)


        self.retranslateUi(AddAvailableMovementWidget)

        self.addButton.setDefault(True)


        QMetaObject.connectSlotsByName(AddAvailableMovementWidget)
    # setupUi

    def retranslateUi(self, AddAvailableMovementWidget):
        AddAvailableMovementWidget.setWindowTitle(QCoreApplication.translate("AddAvailableMovementWidget", u"Tracker2Perf - Ajouter Mouvement Disponible", None))
        AddAvailableMovementWidget.setStyleSheet(QCoreApplication.translate("AddAvailableMovementWidget", u"/* === Main Widget === */\n"
"#AddAvailableMovementWidget {\n"
"    background-color: #F0F0F0;\n"
"}\n"
"\n"
"/* === Labels === */\n"
"QLabel {\n"
"    font-size: 11pt;\n"
"    color: #333333;\n"
"    /* font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif; */\n"
"    padding-bottom: 2px; /* Small space below labels */\n"
"}\n"
"\n"
"#titleLabel {\n"
"    font-size: 18pt;\n"
"    font-weight: bold;\n"
"    color: #1c1c1e;\n"
"    padding-bottom: 15px;\n"
"}\n"
"\n"
"/* Labels used in Form Layouts */\n"
"QFormLayout QLabel {\n"
"    padding-top: 5px; /* Align nicely */\n"
"}\n"
"\n"
"/* Specific labels */\n"
"#musclesLabel, #typeLabel {\n"
"    font-weight: bold; /* Make section headers bold */\n"
"    padding-top: 8px; /* Space above section label */\n"
"}\n"
"\n"
"\n"
"/* === Line Edits === */\n"
"QLineEdit {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    min-height: 22px;\n"
"  "
                        "  font-size: 11pt;\n"
"    color: #333333;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #007AFF;\n"
"}\n"
"QLineEdit[placeholderText] {\n"
"    color: #AAAAAA;\n"
"}\n"
"\n"
"/* === Text Edit === */\n"
"QTextEdit {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    font-size: 11pt;\n"
"    color: #333333;\n"
"}\n"
"QTextEdit:focus {\n"
"    border: 1px solid #007AFF;\n"
"}\n"
"\n"
"/* === Check Boxes === */\n"
"QCheckBox {\n"
"    font-size: 10pt; /* Slightly smaller for list */\n"
"    color: #333333;\n"
"    spacing: 6px; /* Space between indicator and text */\n"
"    padding: 3px 0px; /* Vertical padding */\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    /* Optional: Add custom image */\n"
"    border: 1px solid #BDBDBD;\n"
"    border-radius: 4px; /* Squared look */\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QCheckBox::indicator:unchecke"
                        "d:hover {\n"
"    border: 1px solid #888888;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    /* Optional: Add custom checkmark image */\n"
"    border: 1px solid #007AFF;\n"
"    border-radius: 4px;\n"
"    background-color: #007AFF;\n"
"    /* image: url(:/icons/checkmark.png); */ /* Example */\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #005ECB;\n"
"    background-color: #005ECB;\n"
"}\n"
"\n"
"/* === Radio Buttons === */\n"
"QRadioButton {\n"
"    font-size: 11pt;\n"
"    color: #333333;\n"
"    spacing: 5px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 3px;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"QRadioButton::indicator:unchecked {\n"
"    border: 1px solid #BDBDBD;\n"
"    border-radius: 8px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QRadioButton::indicator:unchecked:hover { border: 1px solid #888888; }\n"
"QRadioButton::indicator:checked {\n"
"    border: 1px solid #007AFF;\n"
"    border-radius: 8px;\n"
"    backgroun"
                        "d-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4, fx:0.5, fy:0.5, stop:0 #007AFF, stop:1 #FFFFFF);\n"
"}\n"
"\n"
"\n"
"/* === Scroll Area === */\n"
"QScrollArea {\n"
"  border: 1px solid #DCDCDC; /* Border around the scroll area */\n"
"  border-radius: 6px;\n"
"  background-color: #FFFFFF; /* White background inside */\n"
"}\n"
"QWidget#musclesScrollAreaContents { /* Target the inner widget */\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"/* === Scroll Bar Styling (macOS like, adapted) === */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #FFFFFF; /* Match scroll area background */\n"
"    width: 8px;\n"
"    margin: 1px 1px 1px 1px; /* Small margin */\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #CFCFCF; /* Gray handle */\n"
"    min-height: 25px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #B0B0B0; /* Darker handle on hover */\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0p"
                        "x; width: 0px;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* === Action Buttons === */\n"
"QPushButton#addButton { /* Renamed from saveButton */\n"
"    background-color: #007AFF;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 8px 20px;\n"
"    min-height: 24px;\n"
"    font-size: 11pt;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton#addButton:hover { background-color: #3395FF; }\n"
"QPushButton#addButton:pressed { background-color: #005ECB; }\n"
"QPushButton#addButton:disabled { background-color: #DCDCDC; color: #A0A0A0; }\n"
"\n"
"QPushButton#cancelButton {\n"
"    background-color: #E9E9ED;\n"
"    color: #333333;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 6px;\n"
"    padding: 8px 20px;\n"
"    min-height: 24px;\n"
"    font-size: 11pt;\n"
"    font-weight: normal;\n"
"}\n"
"QPushButton#cancelButton:hover { background-color: #DDDDDF; border-color: #CFCFCF; }\n"
"QPushButton#canc"
                        "elButton:pressed { background-color: #D5D5D7; }\n"
"   ", None))
        self.titleLabel.setText(QCoreApplication.translate("AddAvailableMovementWidget", u"Ajouter Mouvement \u00e0 la Liste", None))
        self.nomLabel.setText(QCoreApplication.translate("AddAvailableMovementWidget", u"Nom", None))
        self.nomLineEdit.setPlaceholderText(QCoreApplication.translate("AddAvailableMovementWidget", u"Nom unique du mouvement", None))
        self.descriptionLabel.setText(QCoreApplication.translate("AddAvailableMovementWidget", u"Description", None))
        self.descriptionTextEdit.setPlaceholderText(QCoreApplication.translate("AddAvailableMovementWidget", u"D\u00e9crire le mouvement, points cl\u00e9s...", None))
        self.musclesLabel.setText(QCoreApplication.translate("AddAvailableMovementWidget", u"Muscles Cibles", None))
        self.typeLabel.setText(QCoreApplication.translate("AddAvailableMovementWidget", u"Type d'Exercice", None))
        self.cardioRadioButton.setText(QCoreApplication.translate("AddAvailableMovementWidget", u"Cardio", None))
        self.musculationRadioButton.setText(QCoreApplication.translate("AddAvailableMovementWidget", u"Musculation", None))
        self.cancelButton.setText(QCoreApplication.translate("AddAvailableMovementWidget", u"Annuler", None))
        self.addButton.setText(QCoreApplication.translate("AddAvailableMovementWidget", u"Ajouter", None))
    # retranslateUi

