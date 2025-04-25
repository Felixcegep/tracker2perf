# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'creation_utilsateur.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
        FormCreationCompte.resize(628, 348)
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
        self.comboBox_Genre.setObjectName(u"comboBox_Genre")

        self.gridLayout_Form.addWidget(self.comboBox_Genre, 2, 1, 1, 1)

        self.label_Poids = QLabel(FormCreationCompte)
        self.label_Poids.setObjectName(u"label_Poids")

        self.gridLayout_Form.addWidget(self.label_Poids, 4, 0, 1, 1)

        self.dateEdit_Naissance = QDateEdit(FormCreationCompte)
        self.dateEdit_Naissance.setObjectName(u"dateEdit_Naissance")
        self.dateEdit_Naissance.setCalendarPopup(True)

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


        self.verticalLayout_Main.addLayout(self.horizontalLayout_Content)

        self.checkBox_Terms = QCheckBox(FormCreationCompte)
        self.checkBox_Terms.setObjectName(u"checkBox_Terms")

        self.verticalLayout_Main.addWidget(self.checkBox_Terms)

        self.verticalSpacer_Bottom = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_Main.addItem(self.verticalSpacer_Bottom)

        self.horizontalLayout_Buttons = QHBoxLayout()
        self.horizontalLayout_Buttons.setObjectName(u"horizontalLayout_Buttons")
        self.horizontalSpacer_ButtonLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_Buttons.addItem(self.horizontalSpacer_ButtonLeft)

        self.pushButton_Confirm = QPushButton(FormCreationCompte)
        self.pushButton_Confirm.setObjectName(u"pushButton_Confirm")
        self.pushButton_Confirm.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setBold(True)
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

        QMetaObject.connectSlotsByName(FormCreationCompte)
    # setupUi

    def retranslateUi(self, FormCreationCompte):
        FormCreationCompte.setWindowTitle(QCoreApplication.translate("FormCreationCompte", u"Cr\u00e9ation de Compte", None))
        self.label_Bienvenue.setText(QCoreApplication.translate("FormCreationCompte", u"Bienvenue sur le legendaire Tracker2perf ! Cr\u00e9ez votre compte", None))
        self.lineEdit_Nom.setPlaceholderText(QCoreApplication.translate("FormCreationCompte", u"Entrez votre nom complet", None))
        self.label_Taille.setText(QCoreApplication.translate("FormCreationCompte", u"Taille (cm) :", None))
        self.label_Sexe.setText(QCoreApplication.translate("FormCreationCompte", u"Sexe :", None))
        self.comboBox_Genre.setItemText(0, QCoreApplication.translate("FormCreationCompte", u"Homme", None))
        self.comboBox_Genre.setItemText(1, QCoreApplication.translate("FormCreationCompte", u"Femme", None))

        self.label_Poids.setText(QCoreApplication.translate("FormCreationCompte", u"Poids (kg) :", None))
        self.dateEdit_Naissance.setDisplayFormat(QCoreApplication.translate("FormCreationCompte", u"dd/MM/yyyy", None))
        self.label_DateNaissance.setText(QCoreApplication.translate("FormCreationCompte", u"Date de naissance :", None))
        self.label_Nom.setText(QCoreApplication.translate("FormCreationCompte", u"Nom* :", None))
        self.checkBox_Terms.setText(QCoreApplication.translate("FormCreationCompte", u"J'accepte les Termes et Conditions d'Utilisation*", None))
        self.pushButton_Confirm.setText(QCoreApplication.translate("FormCreationCompte", u"Cr\u00e9er le compte", None))
    # retranslateUi

