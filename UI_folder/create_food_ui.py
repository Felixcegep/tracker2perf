# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_food.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_AddFoodWidget(object):
    def setupUi(self, AddFoodWidget):
        if not AddFoodWidget.objectName():
            AddFoodWidget.setObjectName(u"AddFoodWidget")
        AddFoodWidget.resize(420, 300)
        self.mainVLayout = QVBoxLayout(AddFoodWidget)
        self.mainVLayout.setSpacing(15)
        self.mainVLayout.setObjectName(u"mainVLayout")
        self.mainVLayout.setContentsMargins(25, 25, 25, 25)
        self.titleLabel = QLabel(AddFoodWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainVLayout.addWidget(self.titleLabel)

        self.foodFormLayout = QFormLayout()
        self.foodFormLayout.setObjectName(u"foodFormLayout")
        self.foodFormLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.foodFormLayout.setHorizontalSpacing(10)
        self.foodFormLayout.setVerticalSpacing(12)
        self.nomLabel = QLabel(AddFoodWidget)
        self.nomLabel.setObjectName(u"nomLabel")

        self.foodFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nomLabel)

        self.nomComboBox = QComboBox(AddFoodWidget)
        self.nomComboBox.setObjectName(u"nomComboBox")
        self.nomComboBox.setEditable(False)
        self.nomComboBox.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.foodFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nomComboBox)

        self.caloriesLabel = QLabel(AddFoodWidget)
        self.caloriesLabel.setObjectName(u"caloriesLabel")

        self.foodFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.caloriesLabel)

        self.quantityLineEdit = QLineEdit(AddFoodWidget)
        self.quantityLineEdit.setObjectName(u"quantityLineEdit")

        self.foodFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.quantityLineEdit)


        self.mainVLayout.addLayout(self.foodFormLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainVLayout.addItem(self.verticalSpacer)

        self.buttonBoxHLayout = QHBoxLayout()
        self.buttonBoxHLayout.setObjectName(u"buttonBoxHLayout")
        self.addAvailableFoodButton = QPushButton(AddFoodWidget)
        self.addAvailableFoodButton.setObjectName(u"addAvailableFoodButton")

        self.buttonBoxHLayout.addWidget(self.addAvailableFoodButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonBoxHLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(AddFoodWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonBoxHLayout.addWidget(self.cancelButton)

        self.saveButton = QPushButton(AddFoodWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.buttonBoxHLayout.addWidget(self.saveButton)


        self.mainVLayout.addLayout(self.buttonBoxHLayout)


        self.retranslateUi(AddFoodWidget)

        self.saveButton.setDefault(True)


        QMetaObject.connectSlotsByName(AddFoodWidget)
    # setupUi

    def retranslateUi(self, AddFoodWidget):
        AddFoodWidget.setWindowTitle(QCoreApplication.translate("AddFoodWidget", u"Tracker2Perf - Ajouter Aliment Consomm\u00e9", None))
        AddFoodWidget.setStyleSheet(QCoreApplication.translate("AddFoodWidget", u"/* === Main Widget === */\n"
"#AddFoodWidget {\n"
"    background-color: #F0F0F0;\n"
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
"    font-size: 18pt;\n"
"    font-weight: bold;\n"
"    color: #1c1c1e;\n"
"    padding-bottom: 15px;\n"
"}\n"
"\n"
"QFormLayout QLabel {\n"
"    padding-top: 5px;\n"
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
"QLineEdit:focus {\n"
"    border: 1px solid #007AFF;\n"
"}\n"
"QLineEdit[placeholderText] {\n"
"    color: #AAAAAA;\n"
"}\n"
"\n"
"/* === Enhanced Combo Box Styling === */\n"
"QComboBox {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #DCDCDC;\n"
"    bo"
                        "rder-radius: 6px;\n"
"    padding: 6px 28px 6px 10px; /* Adjusted right padding for dropdown area */\n"
"    min-height: 22px; /* Match LineEdit */\n"
"    font-size: 11pt;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #007AFF;\n"
"}\n"
"\n"
"/* :on style less relevant for non-editable combos */\n"
"/* QComboBox:on {\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"} */\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding; /* Position relative to padding */\n"
"    subcontrol-position: top right; /* Position in top-right */\n"
"    width: 25px; /* Width of the dropdown clickable area */\n"
"\n"
"    border-left-width: 1px; /* Separator line */\n"
"    border-left-color: #C0C0C0; /* Slightly darker separator */\n"
"    border-left-style: solid;\n"
"\n"
"    border-top-right-radius: 6px; /* Match main border radius */\n"
"    border-bottom-right-radius: 6px;\n"
"\n"
"    /* Use a gradient or distinct background for the button area */\n"
"    background-c"
                        "olor: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #F8F8F8, stop: 1 #EAEAEA);\n"
"\n"
"    margin: 1px; /* Small margin to inset the button slightly */\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FFFFFF, stop: 1 #E0E0E0); /* Lighter on hover */\n"
"    border-left-color: #A0A0A0;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"     /* Replace with your icon path if desired */\n"
"     /* image: url(:/icons/down_arrow.png); */\n"
"     width: 12px;\n"
"     height: 12px;\n"
"}\n"
"\n"
"/* Style the dropdown list */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #A0A0A0; /* Match hover border */\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: #007AFF;\n"
"    selection-color: #FFFFFF;\n"
"    color: #333333;\n"
"    padding: 4px;\n"
"    outline: 0px; /* Remove focus outline from popup */\n"
"}\n"
"/* === End Enhan"
                        "ced Combo Box Styling === */\n"
"\n"
"\n"
"/* === Action Buttons === */\n"
"/* Save Button (Primary) */\n"
"QPushButton#saveButton {\n"
"    background-color: #007AFF;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 8px 20px;\n"
"    min-height: 24px;\n"
"    font-size: 11pt;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton#saveButton:hover { background-color: #3395FF; }\n"
"QPushButton#saveButton:pressed { background-color: #005ECB; }\n"
"QPushButton#saveButton:disabled { background-color: #DCDCDC; color: #A0A0A0; }\n"
"\n"
"/* Cancel and AddAvailableFood Buttons (Secondary) */\n"
"QPushButton#cancelButton, QPushButton#addAvailableFoodButton {\n"
"    background-color: #E9E9ED;\n"
"    color: #333333;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 6px;\n"
"    padding: 8px 15px; /* Adjusted padding */\n"
"    min-height: 24px;\n"
"    font-size: 10pt; /* Slightly smaller font for secondary */\n"
"    font-weight: normal;\n"
"}\n"
"QPushButton#cancelButton:h"
                        "over, QPushButton#addAvailableFoodButton:hover {\n"
"     background-color: #DDDDDF; border-color: #CFCFCF;\n"
"}\n"
"QPushButton#cancelButton:pressed, QPushButton#addAvailableFoodButton:pressed {\n"
"     background-color: #D5D5D7;\n"
"}\n"
"   ", None))
        self.titleLabel.setText(QCoreApplication.translate("AddFoodWidget", u"Ajouter un Aliment Consomm\u00e9", None))
        self.nomLabel.setText(QCoreApplication.translate("AddFoodWidget", u"Nom", None))
        self.caloriesLabel.setText(QCoreApplication.translate("AddFoodWidget", u"Quantit\u00e9 (grammes)", None))
        self.quantityLineEdit.setPlaceholderText(QCoreApplication.translate("AddFoodWidget", u"e.g., 150", None))
#if QT_CONFIG(tooltip)
        self.addAvailableFoodButton.setToolTip(QCoreApplication.translate("AddFoodWidget", u"Ajouter un nouvel aliment \u00e0 la liste globale", None))
#endif // QT_CONFIG(tooltip)
        self.addAvailableFoodButton.setText(QCoreApplication.translate("AddFoodWidget", u"Nouvel Aliment Dispo", None))
        self.cancelButton.setText(QCoreApplication.translate("AddFoodWidget", u"Annuler", None))
        self.saveButton.setText(QCoreApplication.translate("AddFoodWidget", u"Ajouter", None))
    # retranslateUi

