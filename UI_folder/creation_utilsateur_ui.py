# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'creation_utilsateur.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_FormCreationCompte(object):
    def setupUi(self, FormCreationCompte):
        if not FormCreationCompte.objectName():
            FormCreationCompte.setObjectName(u"FormCreationCompte")
        FormCreationCompte.resize(628, 400)
        self.verticalLayout_Main = QVBoxLayout(FormCreationCompte)
        self.verticalLayout_Main.setObjectName(u"verticalLayout_Main")
        self.label_Bienvenue = QLabel(FormCreationCompte)
        self.label_Bienvenue.setObjectName(u"label_Bienvenue")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_Bienvenue.setFont(font)
        self.label_Bienvenue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_Main.addWidget(self.label_Bienvenue)

        self.horizontalLayout_Content = QHBoxLayout()
        self.horizontalLayout_Content.setObjectName(u"horizontalLayout_Content")
        self.horizontalSpacer_FormLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Content.addItem(self.horizontalSpacer_FormLeft)

        self.gridLayout_Form = QGridLayout()
        self.gridLayout_Form.setObjectName(u"gridLayout_Form")
        self.lineEdit_Nom = QLineEdit(FormCreationCompte)
        self.lineEdit_Nom.setObjectName(u"lineEdit_Nom")

        self.gridLayout_Form.addWidget(self.lineEdit_Nom, 0, 1, 1, 1)

        self.spinBox_Poids = QSpinBox(FormCreationCompte)
        self.spinBox_Poids.setObjectName(u"spinBox_Poids")
        self.spinBox_Poids.setMinimum(20)
        self.spinBox_Poids.setMaximum(250)
        self.spinBox_Poids.setValue(70)

        self.gridLayout_Form.addWidget(self.spinBox_Poids, 4, 1, 1, 1)

        self.label_Taille = QLabel(FormCreationCompte)
        self.label_Taille.setObjectName(u"label_Taille")

        self.gridLayout_Form.addWidget(self.label_Taille, 3, 0, 1, 1)

        self.label_Sexe = QLabel(FormCreationCompte)
        self.label_Sexe.setObjectName(u"label_Sexe")

        self.gridLayout_Form.addWidget(self.label_Sexe, 2, 0, 1, 1)

        self.comboBox_Genre = QComboBox(FormCreationCompte)
        self.comboBox_Genre.addItem("")
        self.comboBox_Genre.addItem("")
        self.comboBox_Genre.addItem("")
        self.comboBox_Genre.addItem("")
        self.comboBox_Genre.setObjectName(u"comboBox_Genre")

        self.gridLayout_Form.addWidget(self.comboBox_Genre, 2, 1, 1, 1)

        self.label_Poids = QLabel(FormCreationCompte)
        self.label_Poids.setObjectName(u"label_Poids")

        self.gridLayout_Form.addWidget(self.label_Poids, 4, 0, 1, 1)

        self.dateEdit_Naissance = QDateEdit(FormCreationCompte)
        self.dateEdit_Naissance.setObjectName(u"dateEdit_Naissance")
        self.dateEdit_Naissance.setCalendarPopup(True)
        self.dateEdit_Naissance.setDate(QDate(2000, 1, 1))

        self.gridLayout_Form.addWidget(self.dateEdit_Naissance, 1, 1, 1, 1)

        self.label_DateNaissance = QLabel(FormCreationCompte)
        self.label_DateNaissance.setObjectName(u"label_DateNaissance")

        self.gridLayout_Form.addWidget(self.label_DateNaissance, 1, 0, 1, 1)

        self.label_Nom = QLabel(FormCreationCompte)
        self.label_Nom.setObjectName(u"label_Nom")

        self.gridLayout_Form.addWidget(self.label_Nom, 0, 0, 1, 1)

        self.spinBox_Taille = QSpinBox(FormCreationCompte)
        self.spinBox_Taille.setObjectName(u"spinBox_Taille")
        self.spinBox_Taille.setMinimum(50)
        self.spinBox_Taille.setMaximum(250)
        self.spinBox_Taille.setValue(170)

        self.gridLayout_Form.addWidget(self.spinBox_Taille, 3, 1, 1, 1)


        self.horizontalLayout_Content.addLayout(self.gridLayout_Form)

        self.horizontalSpacer_FormRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Content.addItem(self.horizontalSpacer_FormRight)


        self.verticalLayout_Main.addLayout(self.horizontalLayout_Content)

        self.checkBox_Terms = QCheckBox(FormCreationCompte)
        self.checkBox_Terms.setObjectName(u"checkBox_Terms")

        self.verticalLayout_Main.addWidget(self.checkBox_Terms)

        self.verticalSpacer_Bottom = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_Main.addItem(self.verticalSpacer_Bottom)

        self.horizontalLayout_Buttons = QHBoxLayout()
        self.horizontalLayout_Buttons.setObjectName(u"horizontalLayout_Buttons")
        self.horizontalSpacer_ButtonLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Buttons.addItem(self.horizontalSpacer_ButtonLeft)

        self.pushButton_Confirm = QPushButton(FormCreationCompte)
        self.pushButton_Confirm.setObjectName(u"pushButton_Confirm")
        self.pushButton_Confirm.setMinimumSize(QSize(180, 40))
        font1 = QFont()
        font1.setWeight(QFont.Medium)
        self.pushButton_Confirm.setFont(font1)

        self.horizontalLayout_Buttons.addWidget(self.pushButton_Confirm)

        self.horizontalSpacer_ButtonRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Buttons.addItem(self.horizontalSpacer_ButtonRight)


        self.verticalLayout_Main.addLayout(self.horizontalLayout_Buttons)

#if QT_CONFIG(shortcut)
        self.label_Taille.setBuddy(self.spinBox_Taille)
        self.label_Sexe.setBuddy(self.comboBox_Genre)
        self.label_Poids.setBuddy(self.spinBox_Poids)
        self.label_DateNaissance.setBuddy(self.dateEdit_Naissance)
        self.label_Nom.setBuddy(self.lineEdit_Nom)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit_Nom, self.dateEdit_Naissance)
        QWidget.setTabOrder(self.dateEdit_Naissance, self.comboBox_Genre)
        QWidget.setTabOrder(self.comboBox_Genre, self.spinBox_Taille)
        QWidget.setTabOrder(self.spinBox_Taille, self.spinBox_Poids)
        QWidget.setTabOrder(self.spinBox_Poids, self.checkBox_Terms)
        QWidget.setTabOrder(self.checkBox_Terms, self.pushButton_Confirm)

        self.retranslateUi(FormCreationCompte)

        self.pushButton_Confirm.setDefault(True)


        QMetaObject.connectSlotsByName(FormCreationCompte)
    # setupUi

    def retranslateUi(self, FormCreationCompte):
        FormCreationCompte.setWindowTitle(QCoreApplication.translate("FormCreationCompte", u"Cr\u00e9ation de Compte", None))
        FormCreationCompte.setStyleSheet(QCoreApplication.translate("FormCreationCompte", u"/* Apply base background to the main window widget */\n"
"QWidget#FormCreationCompte {\n"
"    background-color: #F5F5F7; /* Light gray background */\n"
"}\n"
"\n"
"/* Global Styles */\n"
"QWidget {\n"
"    color: #333333; /* Default text color */\n"
"    /* font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif; */\n"
"}\n"
"\n"
"/* Input Fields Styling */\n"
"QLineEdit, QDateEdit, QSpinBox { /* Removed QComboBox from this generic rule */\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 5px;\n"
"    padding: 6px 10px;\n"
"    min-height: 24px; /* Consistent height */\n"
"}\n"
"\n"
"QLineEdit:focus, QDateEdit:focus, QSpinBox:focus {\n"
"    border: 1px solid #007AFF; /* Blue border on focus */\n"
"}\n"
"\n"
"/* Specific adjustments for SpinBox/DateEdit padding */\n"
"QSpinBox { padding: 6px 5px; }\n"
"QDateEdit { padding: 6px 5px; }\n"
"\n"
"/* QDateEdit Dropdown Styling (Kept simpler) */\n"
"QDateEdit::drop-down {\n"
"    "
                        "subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 18px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #DCDCDC;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/qt-project.org/styles/commonstyle/images/down_arrow_16x16.png); /* Example path */\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"\n"
"/* --- Enhanced QComboBox Styling --- */\n"
"QComboBox {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 5px;\n"
"    padding: 6px 28px 6px 10px; /* Increased right padding to avoid text overlapping arrow area */\n"
"    min-height: 24px;\n"
"    color: #333333; /* Ensure text color is set */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #007AFF;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding; /* Position relative to padding box */\n"
"    subcontrol-position: top r"
                        "ight; /* Position in top-right */\n"
"    width: 25px; /* Width of the dropdown area */\n"
"\n"
"    border-left-width: 1px; /* Separator line */\n"
"    border-left-color: #C0C0C0; /* Slightly darker separator */\n"
"    border-left-style: solid;\n"
"\n"
"    border-top-right-radius: 5px; /* Match main border radius */\n"
"    border-bottom-right-radius: 5px;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, /* Subtle gradient */\n"
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
"    image: url(:/qt-project.org/styles/commonstyle/images/down_arrow_16x16.png); /* Example path */\n"
"    width: 12px;\n"
""
                        "    height: 12px;\n"
"    /* Position handled by subcontrol-position and width/padding */\n"
"}\n"
"\n"
"/* You might need this if the arrow isn't centered well enough by default */\n"
"/* QComboBox::down-arrow {\n"
"    position: absolute;\n"
"    top: 50%;\n"
"    right: 8px;\n"
"    margin-top: -6px;\n"
"} */\n"
"\n"
"\n"
"QComboBox QAbstractItemView { /* Style the dropdown list */\n"
"    border: 1px solid #A0A0A0; /* Slightly darker border for popup */\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: #007AFF;\n"
"    selection-color: #FFFFFF;\n"
"    padding: 4px; /* Add padding to the view */\n"
"    outline: 0px; /* Remove focus outline from the popup */\n"
"}\n"
"/* --- End Enhanced QComboBox Styling --- */\n"
"\n"
"\n"
"/* Button Styling */\n"
"QPushButton#pushButton_Confirm {\n"
"    background-color: #007AFF;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px;\n"
"    min-height: 24px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushBut"
                        "ton#pushButton_Confirm:hover { background-color: #3395FF; }\n"
"QPushButton#pushButton_Confirm:pressed { background-color: #005ECB; }\n"
"QPushButton#pushButton_Confirm:disabled { background-color: #DCDCDC; color: #A0A0A0; }\n"
"\n"
"/* Label Styling */\n"
"QLabel { background-color: transparent; padding: 3px 0; }\n"
"#label_Bienvenue { font-size: 16pt; font-weight: bold; color: #222222; padding-bottom: 15px; }\n"
"#label_Nom, #label_DateNaissance, #label_Sexe, #label_Taille, #label_Poids { font-size: 10pt; color: #555555; }\n"
"\n"
"/* CheckBox Styling */\n"
"QCheckBox { spacing: 8px; padding: 10px 0; }\n"
"QCheckBox::indicator { width: 16px; height: 16px; border: 1px solid #B0B0B0; border-radius: 3px; background-color: #FFFFFF; }\n"
"QCheckBox::indicator:hover { border: 1px solid #808080; }\n"
"QCheckBox::indicator:checked { background-color: #007AFF; border: 1px solid #007AFF; /* image: url(:/icons/checkmark.png); */ }\n"
"QCheckBox::indicator:checked:hover { background-color: #3395FF; border: 1px solid #33"
                        "95FF; }\n"
"\n"
"/* Layout Spacing */\n"
"#verticalLayout_Main { margin: 20px; }\n"
"#gridLayout_Form { verticalSpacing: 10px; horizontalSpacing: 10px; }\n"
"", None))
        self.label_Bienvenue.setText(QCoreApplication.translate("FormCreationCompte", u"Bienvenue sur le legendaire Tracker2perf ! Cr\u00e9ez votre compte", None))
        self.lineEdit_Nom.setPlaceholderText(QCoreApplication.translate("FormCreationCompte", u"Entrez votre nom complet", None))
        self.spinBox_Poids.setSuffix(QCoreApplication.translate("FormCreationCompte", u" kg", None))
        self.label_Taille.setText(QCoreApplication.translate("FormCreationCompte", u"Taille :", None))
        self.label_Sexe.setText(QCoreApplication.translate("FormCreationCompte", u"Sexe :", None))
        self.comboBox_Genre.setItemText(0, QCoreApplication.translate("FormCreationCompte", u"Homme", None))
        self.comboBox_Genre.setItemText(1, QCoreApplication.translate("FormCreationCompte", u"Femme", None))
        self.comboBox_Genre.setItemText(2, QCoreApplication.translate("FormCreationCompte", u"Autre", None))
        self.comboBox_Genre.setItemText(3, QCoreApplication.translate("FormCreationCompte", u"Pr\u00e9f\u00e8re ne pas r\u00e9pondre", None))

        self.label_Poids.setText(QCoreApplication.translate("FormCreationCompte", u"Poids :", None))
        self.dateEdit_Naissance.setDisplayFormat(QCoreApplication.translate("FormCreationCompte", u"dd/MM/yyyy", None))
        self.label_DateNaissance.setText(QCoreApplication.translate("FormCreationCompte", u"Date de naissance* :", None))
        self.label_Nom.setText(QCoreApplication.translate("FormCreationCompte", u"Nom* :", None))
        self.spinBox_Taille.setSuffix(QCoreApplication.translate("FormCreationCompte", u" cm", None))
#if QT_CONFIG(tooltip)
        self.checkBox_Terms.setToolTip(QCoreApplication.translate("FormCreationCompte", u"Vous devez accepter les termes pour cr\u00e9er un compte", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_Terms.setText(QCoreApplication.translate("FormCreationCompte", u"J'accepte les Termes et Conditions d'Utilisation*", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Confirm.setToolTip(QCoreApplication.translate("FormCreationCompte", u"Finaliser la cr\u00e9ation de votre compte Tracker2Perf", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Confirm.setText(QCoreApplication.translate("FormCreationCompte", u"Cr\u00e9er le compte", None))
    # retranslateUi

