# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_available_food.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AddAvailableFoodWidget(object):
    def setupUi(self, AddAvailableFoodWidget):
        if not AddAvailableFoodWidget.objectName():
            AddAvailableFoodWidget.setObjectName(u"AddAvailableFoodWidget")
        AddAvailableFoodWidget.resize(420, 340)
        self.mainVLayout = QVBoxLayout(AddAvailableFoodWidget)
        self.mainVLayout.setSpacing(15)
        self.mainVLayout.setObjectName(u"mainVLayout")
        self.mainVLayout.setContentsMargins(25, 25, 25, 25)
        self.titleLabel = QLabel(AddAvailableFoodWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainVLayout.addWidget(self.titleLabel)

        self.foodFormLayout = QFormLayout()
        self.foodFormLayout.setObjectName(u"foodFormLayout")
        self.foodFormLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.foodFormLayout.setHorizontalSpacing(10)
        self.foodFormLayout.setVerticalSpacing(12)
        self.nomLabel = QLabel(AddAvailableFoodWidget)
        self.nomLabel.setObjectName(u"nomLabel")

        self.foodFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nomLabel)

        self.nomLineEdit = QLineEdit(AddAvailableFoodWidget)
        self.nomLineEdit.setObjectName(u"nomLineEdit")

        self.foodFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nomLineEdit)

        self.proteinesLabel = QLabel(AddAvailableFoodWidget)
        self.proteinesLabel.setObjectName(u"proteinesLabel")

        self.foodFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.proteinesLabel)

        self.proteinesLineEdit = QLineEdit(AddAvailableFoodWidget)
        self.proteinesLineEdit.setObjectName(u"proteinesLineEdit")

        self.foodFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.proteinesLineEdit)

        self.caloriesLabel = QLabel(AddAvailableFoodWidget)
        self.caloriesLabel.setObjectName(u"caloriesLabel")

        self.foodFormLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.caloriesLabel)

        self.caloriesLineEdit = QLineEdit(AddAvailableFoodWidget)
        self.caloriesLineEdit.setObjectName(u"caloriesLineEdit")

        self.foodFormLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.caloriesLineEdit)


        self.mainVLayout.addLayout(self.foodFormLayout)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainVLayout.addItem(self.verticalSpacer)

        self.buttonBoxHLayout = QHBoxLayout()
        self.buttonBoxHLayout.setObjectName(u"buttonBoxHLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonBoxHLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(AddAvailableFoodWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonBoxHLayout.addWidget(self.cancelButton)

        self.addButton = QPushButton(AddAvailableFoodWidget)
        self.addButton.setObjectName(u"addButton")

        self.buttonBoxHLayout.addWidget(self.addButton)


        self.mainVLayout.addLayout(self.buttonBoxHLayout)


        self.retranslateUi(AddAvailableFoodWidget)

        self.addButton.setDefault(True)


        QMetaObject.connectSlotsByName(AddAvailableFoodWidget)
    # setupUi

    def retranslateUi(self, AddAvailableFoodWidget):
        AddAvailableFoodWidget.setWindowTitle(QCoreApplication.translate("AddAvailableFoodWidget", u"Tracker2Perf - Ajouter Aliment Disponible", None))
        AddAvailableFoodWidget.setStyleSheet(QCoreApplication.translate("AddAvailableFoodWidget", u"/* === Main Widget === */\n"
"#AddAvailableFoodWidget {\n"
"    background-color: #F0F0F0; /* Slightly off-white */\n"
"}\n"
"\n"
"/* === Labels === */\n"
"QLabel {\n"
"    font-size: 11pt;\n"
"    color: #333333;\n"
"    /* font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif; */\n"
"}\n"
"\n"
"#titleLabel {\n"
"    font-size: 18pt; /* Prominent title */\n"
"    font-weight: bold;\n"
"    color: #1c1c1e;\n"
"    padding-bottom: 15px; /* Space below title */\n"
"}\n"
"\n"
"/* Labels used in Form Layouts */\n"
"QFormLayout QLabel {\n"
"    padding-top: 5px; /* Align label nicely with input */\n"
"}\n"
"\n"
"/* === Line Edits === */\n"
"QLineEdit {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    min-height: 22px;\n"
"    font-size: 11pt;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #007AFF;\n"
"}\n"
"\n"
"QLineEdit[placeholderText] {\n"
"    colo"
                        "r: #AAAAAA;\n"
"}\n"
"\n"
"/* === Action Buttons === */\n"
"QPushButton#addButton { /* Renamed from saveButton for clarity */\n"
"    background-color: #007AFF; /* Primary action */\n"
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
"    background-color: #E9E9ED; /* Secondary action */\n"
"    color: #333333;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 6px;\n"
"    padding: 8px 20px;\n"
"    min-height: 24px;\n"
"    font-size: 11pt;\n"
"    font-weight: normal;\n"
"}\n"
"QPushButton#cancelButton:hover { background-color: #DDDDDF; border-color: #CFCFCF; }\n"
"QPushButton#cancelButton:pressed { background-color: #D5D5D7; "
                        "}\n"
"   ", None))
        self.titleLabel.setText(QCoreApplication.translate("AddAvailableFoodWidget", u"Ajouter Aliment \u00e0 la Liste", None))
        self.nomLabel.setText(QCoreApplication.translate("AddAvailableFoodWidget", u"Nom", None))
        self.nomLineEdit.setPlaceholderText(QCoreApplication.translate("AddAvailableFoodWidget", u"Nom unique de l'aliment", None))
        self.proteinesLabel.setText(QCoreApplication.translate("AddAvailableFoodWidget", u"Prot\u00e9ines (g/100g)", None))
        self.proteinesLineEdit.setPlaceholderText(QCoreApplication.translate("AddAvailableFoodWidget", u"e.g., 21.5", None))
        self.caloriesLabel.setText(QCoreApplication.translate("AddAvailableFoodWidget", u"Calories (kcal/100g)", None))
        self.caloriesLineEdit.setPlaceholderText(QCoreApplication.translate("AddAvailableFoodWidget", u"e.g., 165", None))
        self.cancelButton.setText(QCoreApplication.translate("AddAvailableFoodWidget", u"Annuler", None))
        self.addButton.setText(QCoreApplication.translate("AddAvailableFoodWidget", u"Ajouter", None))
    # retranslateUi

