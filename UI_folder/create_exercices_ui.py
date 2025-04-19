# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_exercices.ui'
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
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_ExerciseCreator(object):
    def setupUi(self, ExerciseCreator):
        if not ExerciseCreator.objectName():
            ExerciseCreator.setObjectName(u"ExerciseCreator")
        ExerciseCreator.resize(420, 480)
        self.mainVLayout = QVBoxLayout(ExerciseCreator)
        self.mainVLayout.setSpacing(15)
        self.mainVLayout.setObjectName(u"mainVLayout")
        self.mainVLayout.setContentsMargins(20, 20, 20, 20)
        self.titleLabel = QLabel(ExerciseCreator)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainVLayout.addWidget(self.titleLabel)

        self.typeSelectorWidget = QWidget(ExerciseCreator)
        self.typeSelectorWidget.setObjectName(u"typeSelectorWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeSelectorWidget.sizePolicy().hasHeightForWidth())
        self.typeSelectorWidget.setSizePolicy(sizePolicy)
        self.typeSelectorHLayout = QHBoxLayout(self.typeSelectorWidget)
        self.typeSelectorHLayout.setSpacing(0)
        self.typeSelectorHLayout.setObjectName(u"typeSelectorHLayout")
        self.typeSelectorHLayout.setContentsMargins(0, 0, 0, 0)
        self.cardioButton = QPushButton(self.typeSelectorWidget)
        self.cardioButton.setObjectName(u"cardioButton")
        self.cardioButton.setCheckable(True)
        self.cardioButton.setChecked(True)
        self.cardioButton.setAutoExclusive(True)

        self.typeSelectorHLayout.addWidget(self.cardioButton)

        self.musculationButton = QPushButton(self.typeSelectorWidget)
        self.musculationButton.setObjectName(u"musculationButton")
        self.musculationButton.setCheckable(True)
        self.musculationButton.setAutoExclusive(True)

        self.typeSelectorHLayout.addWidget(self.musculationButton)


        self.mainVLayout.addWidget(self.typeSelectorWidget)

        self.commonFormLayout = QFormLayout()
        self.commonFormLayout.setObjectName(u"commonFormLayout")
        self.commonFormLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.commonFormLayout.setHorizontalSpacing(10)
        self.commonFormLayout.setVerticalSpacing(10)
        self.nomExerciceLabel = QLabel(ExerciseCreator)
        self.nomExerciceLabel.setObjectName(u"nomExerciceLabel")

        self.commonFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nomExerciceLabel)

        self.nomExerciceComboBox = QComboBox(ExerciseCreator)
        self.nomExerciceComboBox.setObjectName(u"nomExerciceComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nomExerciceComboBox.sizePolicy().hasHeightForWidth())
        self.nomExerciceComboBox.setSizePolicy(sizePolicy1)
        self.nomExerciceComboBox.setStyleSheet(u"")
        self.nomExerciceComboBox.setEditable(True)
        self.nomExerciceComboBox.setInsertPolicy(QComboBox.NoInsert)

        self.commonFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nomExerciceComboBox)


        self.mainVLayout.addLayout(self.commonFormLayout)

        self.inputStackedWidget = QStackedWidget(ExerciseCreator)
        self.inputStackedWidget.setObjectName(u"inputStackedWidget")
        self.cardioPage = QWidget()
        self.cardioPage.setObjectName(u"cardioPage")
        self.cardioFormLayout = QFormLayout(self.cardioPage)
        self.cardioFormLayout.setObjectName(u"cardioFormLayout")
        self.cardioFormLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.cardioFormLayout.setHorizontalSpacing(10)
        self.cardioFormLayout.setVerticalSpacing(10)
        self.dureeLabel = QLabel(self.cardioPage)
        self.dureeLabel.setObjectName(u"dureeLabel")

        self.cardioFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.dureeLabel)

        self.dureeLineEdit = QLineEdit(self.cardioPage)
        self.dureeLineEdit.setObjectName(u"dureeLineEdit")

        self.cardioFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.dureeLineEdit)

        self.distanceLabel = QLabel(self.cardioPage)
        self.distanceLabel.setObjectName(u"distanceLabel")

        self.cardioFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.distanceLabel)

        self.distanceLineEdit = QLineEdit(self.cardioPage)
        self.distanceLineEdit.setObjectName(u"distanceLineEdit")

        self.cardioFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.distanceLineEdit)

        self.intensiteLabel = QLabel(self.cardioPage)
        self.intensiteLabel.setObjectName(u"intensiteLabel")

        self.cardioFormLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.intensiteLabel)

        self.intensiteLineEdit = QLineEdit(self.cardioPage)
        self.intensiteLineEdit.setObjectName(u"intensiteLineEdit")

        self.cardioFormLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.intensiteLineEdit)

        self.inputStackedWidget.addWidget(self.cardioPage)
        self.musculationPage = QWidget()
        self.musculationPage.setObjectName(u"musculationPage")
        self.musculationFormLayout = QFormLayout(self.musculationPage)
        self.musculationFormLayout.setObjectName(u"musculationFormLayout")
        self.musculationFormLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.musculationFormLayout.setHorizontalSpacing(10)
        self.musculationFormLayout.setVerticalSpacing(10)
        self.rpeLabel = QLabel(self.musculationPage)
        self.rpeLabel.setObjectName(u"rpeLabel")

        self.musculationFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.rpeLabel)

        self.rpeLineEdit = QLineEdit(self.musculationPage)
        self.rpeLineEdit.setObjectName(u"rpeLineEdit")

        self.musculationFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.rpeLineEdit)

        self.setsLabel = QLabel(self.musculationPage)
        self.setsLabel.setObjectName(u"setsLabel")

        self.musculationFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.setsLabel)

        self.setsLineEdit = QLineEdit(self.musculationPage)
        self.setsLineEdit.setObjectName(u"setsLineEdit")

        self.musculationFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.setsLineEdit)

        self.repsLabel = QLabel(self.musculationPage)
        self.repsLabel.setObjectName(u"repsLabel")

        self.musculationFormLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.repsLabel)

        self.repsLineEdit = QLineEdit(self.musculationPage)
        self.repsLineEdit.setObjectName(u"repsLineEdit")

        self.musculationFormLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.repsLineEdit)

        self.poidsLabel = QLabel(self.musculationPage)
        self.poidsLabel.setObjectName(u"poidsLabel")

        self.musculationFormLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.poidsLabel)

        self.poidsLineEdit = QLineEdit(self.musculationPage)
        self.poidsLineEdit.setObjectName(u"poidsLineEdit")

        self.musculationFormLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.poidsLineEdit)

        self.inputStackedWidget.addWidget(self.musculationPage)

        self.mainVLayout.addWidget(self.inputStackedWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainVLayout.addItem(self.verticalSpacer)

        self.buttonBoxHLayout = QHBoxLayout()
        self.buttonBoxHLayout.setObjectName(u"buttonBoxHLayout")
        self.addNewMovementButton = QPushButton(ExerciseCreator)
        self.addNewMovementButton.setObjectName(u"addNewMovementButton")
        sizePolicy.setHeightForWidth(self.addNewMovementButton.sizePolicy().hasHeightForWidth())
        self.addNewMovementButton.setSizePolicy(sizePolicy)
        self.addNewMovementButton.setStyleSheet(u"")

        self.buttonBoxHLayout.addWidget(self.addNewMovementButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonBoxHLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(ExerciseCreator)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonBoxHLayout.addWidget(self.cancelButton)

        self.saveButton = QPushButton(ExerciseCreator)
        self.saveButton.setObjectName(u"saveButton")

        self.buttonBoxHLayout.addWidget(self.saveButton)


        self.mainVLayout.addLayout(self.buttonBoxHLayout)


        self.retranslateUi(ExerciseCreator)

        self.inputStackedWidget.setCurrentIndex(0)
        self.saveButton.setDefault(True)


        QMetaObject.connectSlotsByName(ExerciseCreator)
    # setupUi

    def retranslateUi(self, ExerciseCreator):
        ExerciseCreator.setWindowTitle(QCoreApplication.translate("ExerciseCreator", u"Tracker2Perf - Create Exercise", None))
        ExerciseCreator.setStyleSheet(QCoreApplication.translate("ExerciseCreator", u"/* === Main Widget === */\n"
"#ExerciseCreator {\n"
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
"    font-size: 16pt;\n"
"    font-weight: bold;\n"
"    color: #1c1c1e;\n"
"    padding-bottom: 10px;\n"
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
"/* === Combo Box === */\n"
"QComboBox {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 6p"
                        "x;\n"
"    padding: 5px 10px; /* Adjusted padding for combo box */\n"
"    min-height: 22px; /* Match LineEdit */\n"
"    font-size: 11pt;\n"
"    color: #333333;\n"
"}\n"
"QComboBox:focus {\n"
"    border: 1px solid #007AFF;\n"
"}\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"/* Style the dropdown arrow */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #DCDCDC;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"     image: url(noexist.png); /* Placeholder - Use a real icon */\n"
"     width: 12px;\n"
"     height: 12px;\n"
"}\n"
"/* Style the dropdown list */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #DCDCDC;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: #007"
                        "AFF;\n"
"    selection-color: #FFFFFF;\n"
"    color: #333333;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"\n"
"/* === Segmented Buttons === */\n"
"#typeSelectorWidget {\n"
"    background-color: #E0E0E0;\n"
"    border-radius: 8px;\n"
"    border: 1px solid #cccccc;\n"
"}\n"
"#cardioButton, #musculationButton {\n"
"    background-color: transparent;\n"
"    color: #333333;\n"
"    border: none;\n"
"    padding: 6px 18px;\n"
"    font-size: 10pt;\n"
"    font-weight: 500;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"    margin: 2px;\n"
"}\n"
"#cardioButton:hover, #musculationButton:hover {\n"
"     background-color: rgba(0, 0, 0, 0.05);\n"
"}\n"
"#cardioButton:checked, #musculationButton:checked {\n"
"    background-color: #007AFF;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"/* === Standard Action Buttons === */\n"
"/* Save Button (Primary) */\n"
"QPushButton#saveButton {\n"
"    background-color: #007AFF;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 8px 20px"
                        ";\n"
"    min-height: 24px;\n"
"    font-size: 11pt;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton#saveButton:hover { background-color: #3395FF; }\n"
"QPushButton#saveButton:pressed { background-color: #005ECB; }\n"
"QPushButton#saveButton:disabled { background-color: #DCDCDC; color: #A0A0A0; }\n"
"\n"
"/* Cancel and AddNewMovement Buttons (Secondary) */\n"
"QPushButton#cancelButton, QPushButton#addNewMovementButton {\n"
"    background-color: #E9E9ED;\n"
"    color: #333333;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 6px;\n"
"    padding: 8px 15px; /* Adjusted padding */\n"
"    min-height: 24px;\n"
"    font-size: 10pt; /* Slightly smaller font for secondary */\n"
"    font-weight: normal;\n"
"}\n"
"QPushButton#cancelButton:hover, QPushButton#addNewMovementButton:hover {\n"
"     background-color: #DDDDDF; border-color: #CFCFCF;\n"
"}\n"
"QPushButton#cancelButton:pressed, QPushButton#addNewMovementButton:pressed {\n"
"     background-color: #D5D5D7;\n"
"}\n"
"\n"
"/* === Stacked Widget Pages"
                        " === */\n"
"#cardioPage, #musculationPage {\n"
"    background-color: transparent;\n"
"}\n"
"   ", None))
        self.titleLabel.setText(QCoreApplication.translate("ExerciseCreator", u"Create Exercise", None))
        self.cardioButton.setText(QCoreApplication.translate("ExerciseCreator", u"Cardio", None))
        self.musculationButton.setText(QCoreApplication.translate("ExerciseCreator", u"Musculation", None))
        self.nomExerciceLabel.setText(QCoreApplication.translate("ExerciseCreator", u"Nom Exercice", None))
        self.dureeLabel.setText(QCoreApplication.translate("ExerciseCreator", u"Dur\u00e9e", None))
        self.dureeLineEdit.setPlaceholderText(QCoreApplication.translate("ExerciseCreator", u"minutes", None))
        self.distanceLabel.setText(QCoreApplication.translate("ExerciseCreator", u"Distance", None))
        self.distanceLineEdit.setPlaceholderText(QCoreApplication.translate("ExerciseCreator", u"km", None))
        self.intensiteLabel.setText(QCoreApplication.translate("ExerciseCreator", u"Intensit\u00e9", None))
        self.intensiteLineEdit.setPlaceholderText(QCoreApplication.translate("ExerciseCreator", u"(1-10)", None))
        self.rpeLabel.setText(QCoreApplication.translate("ExerciseCreator", u"RPE", None))
#if QT_CONFIG(tooltip)
        self.rpeLineEdit.setToolTip(QCoreApplication.translate("ExerciseCreator", u"Rate of Perceived Exertion (1-10)", None))
#endif // QT_CONFIG(tooltip)
        self.rpeLineEdit.setPlaceholderText(QCoreApplication.translate("ExerciseCreator", u"(1-10)", None))
        self.setsLabel.setText(QCoreApplication.translate("ExerciseCreator", u"S\u00e9ries", None))
        self.setsLineEdit.setPlaceholderText(QCoreApplication.translate("ExerciseCreator", u"e.g., 3", None))
        self.repsLabel.setText(QCoreApplication.translate("ExerciseCreator", u"R\u00e9p\u00e9titions", None))
        self.repsLineEdit.setPlaceholderText(QCoreApplication.translate("ExerciseCreator", u"e.g., 10", None))
        self.poidsLabel.setText(QCoreApplication.translate("ExerciseCreator", u"Poids (kg)", None))
        self.poidsLineEdit.setPlaceholderText(QCoreApplication.translate("ExerciseCreator", u"e.g., 70.5", None))
        self.addNewMovementButton.setText(QCoreApplication.translate("ExerciseCreator", u"Nouveau Mouvement", None))
#if QT_CONFIG(tooltip)
        self.addNewMovementButton.setToolTip(QCoreApplication.translate("ExerciseCreator", u"Ajouter un nouveau type de mouvement \u00e0 la liste globale", None))
#endif // QT_CONFIG(tooltip)
        self.cancelButton.setText(QCoreApplication.translate("ExerciseCreator", u"Annuler", None))
        self.saveButton.setText(QCoreApplication.translate("ExerciseCreator", u"Enregistrer", None))
    # retranslateUi

