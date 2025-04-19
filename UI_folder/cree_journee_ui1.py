# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cree_journee.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_CreateJourneeWidget(object):
    def setupUi(self, CreateJourneeWidget):
        if not CreateJourneeWidget.objectName():
            CreateJourneeWidget.setObjectName(u"CreateJourneeWidget")
        CreateJourneeWidget.resize(400, 320)
        self.mainVLayout = QVBoxLayout(CreateJourneeWidget)
        self.mainVLayout.setSpacing(15)
        self.mainVLayout.setObjectName(u"mainVLayout")
        self.mainVLayout.setContentsMargins(25, 25, 25, 25)
        self.titleLabel = QLabel(CreateJourneeWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainVLayout.addWidget(self.titleLabel)

        self.journeeFormLayout = QFormLayout()
        self.journeeFormLayout.setObjectName(u"journeeFormLayout")
        self.journeeFormLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.journeeFormLayout.setHorizontalSpacing(10)
        self.journeeFormLayout.setVerticalSpacing(12)
        self.nomJourneeLabel = QLabel(CreateJourneeWidget)
        self.nomJourneeLabel.setObjectName(u"nomJourneeLabel")

        self.journeeFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nomJourneeLabel)

        self.nomJourneeLineEdit = QLineEdit(CreateJourneeWidget)
        self.nomJourneeLineEdit.setObjectName(u"nomJourneeLineEdit")

        self.journeeFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nomJourneeLineEdit)

        self.dateLabel = QLabel(CreateJourneeWidget)
        self.dateLabel.setObjectName(u"dateLabel")

        self.journeeFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.dateLabel)

        self.dateEdit = QDateEdit(CreateJourneeWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.journeeFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateEdit)

        self.poidsAujourdhuiLabel = QLabel(CreateJourneeWidget)
        self.poidsAujourdhuiLabel.setObjectName(u"poidsAujourdhuiLabel")

        self.journeeFormLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.poidsAujourdhuiLabel)

        self.poidsAujourdhuiLineEdit = QLineEdit(CreateJourneeWidget)
        self.poidsAujourdhuiLineEdit.setObjectName(u"poidsAujourdhuiLineEdit")

        self.journeeFormLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.poidsAujourdhuiLineEdit)


        self.mainVLayout.addLayout(self.journeeFormLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainVLayout.addItem(self.verticalSpacer)

        self.buttonBoxHLayout = QHBoxLayout()
        self.buttonBoxHLayout.setObjectName(u"buttonBoxHLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonBoxHLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(CreateJourneeWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonBoxHLayout.addWidget(self.cancelButton)

        self.saveButton = QPushButton(CreateJourneeWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.buttonBoxHLayout.addWidget(self.saveButton)


        self.mainVLayout.addLayout(self.buttonBoxHLayout)


        self.retranslateUi(CreateJourneeWidget)

        self.saveButton.setDefault(True)


        QMetaObject.connectSlotsByName(CreateJourneeWidget)
    # setupUi

    def retranslateUi(self, CreateJourneeWidget):
        CreateJourneeWidget.setWindowTitle(QCoreApplication.translate("CreateJourneeWidget", u"Tracker2Perf - Ajouter Journ\u00e9e", None))
        CreateJourneeWidget.setStyleSheet(QCoreApplication.translate("CreateJourneeWidget", u"/* === Main Widget === */\n"
"#CreateJourneeWidget {\n"
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
"    color: "
                        "#AAAAAA;\n"
"}\n"
"\n"
"/* === Date Edit === */\n"
"QDateEdit {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 6px;\n"
"    padding: 5px 8px; /* Slightly less vertical padding needed */\n"
"    min-height: 22px;\n"
"    font-size: 11pt;\n"
"    color: #333333;\n"
"}\n"
"QDateEdit:focus {\n"
"    border: 1px solid #007AFF;\n"
"}\n"
"\n"
"/* Style the dropdown button (optional, basic) */\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #DCDCDC;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"QDateEdit::down-arrow {\n"
"    /* Consider adding an arrow icon using 'image:' property and a resource file */\n"
"     image: url(noexist.png); /* Placeholder, use a real icon path */\n"
"     width: 12px;\n"
"     height: 12px;\n"
"}\n"
"QDateEdit::down-arrow:on { /* shif"
                        "t the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"\n"
"/* === Action Buttons === */\n"
"QPushButton#saveButton {\n"
"    background-color: #007AFF; /* Primary action */\n"
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
"QPushButton#cancelButton:pressed { b"
                        "ackground-color: #D5D5D7; }\n"
"   ", None))
        self.titleLabel.setText(QCoreApplication.translate("CreateJourneeWidget", u"Ajouter une Journ\u00e9e", None))
        self.nomJourneeLabel.setText(QCoreApplication.translate("CreateJourneeWidget", u"Nom de la Journ\u00e9e", None))
        self.nomJourneeLineEdit.setPlaceholderText(QCoreApplication.translate("CreateJourneeWidget", u"e.g., Lundi, Jour de Jambes", None))
        self.dateLabel.setText(QCoreApplication.translate("CreateJourneeWidget", u"Date", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("CreateJourneeWidget", u"yyyy-MM-dd", None))
        self.poidsAujourdhuiLabel.setText(QCoreApplication.translate("CreateJourneeWidget", u"Poids Aujourd'hui", None))
        self.poidsAujourdhuiLineEdit.setPlaceholderText(QCoreApplication.translate("CreateJourneeWidget", u"en kg (e.g., 71.2)", None))
        self.cancelButton.setText(QCoreApplication.translate("CreateJourneeWidget", u"Annuler", None))
        self.saveButton.setText(QCoreApplication.translate("CreateJourneeWidget", u"Ajouter", None))
    # retranslateUi

