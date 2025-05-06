# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dashboard1.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(1000, 750)
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_main = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_main.setSpacing(0)
        self.horizontalLayout_main.setObjectName(u"horizontalLayout_main")
        self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.leftSidebarWidget = QWidget(self.centralwidget)
        self.leftSidebarWidget.setObjectName(u"leftSidebarWidget")
        self.leftSidebarWidget.setMaximumSize(QSize(220, 16777215))
        self.verticalLayout_sidebar = QVBoxLayout(self.leftSidebarWidget)
        self.verticalLayout_sidebar.setSpacing(10)
        self.verticalLayout_sidebar.setObjectName(u"verticalLayout_sidebar")
        self.verticalLayout_sidebar.setContentsMargins(12, 12, 12, 12)
        self.searchLineEdit = QLineEdit(self.leftSidebarWidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.verticalLayout_sidebar.addWidget(self.searchLineEdit)

        self.label = QLabel(self.leftSidebarWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_sidebar.addWidget(self.label)

        self.scrollArea_days = QScrollArea(self.leftSidebarWidget)
        self.scrollArea_days.setObjectName(u"scrollArea_days")
        self.scrollArea_days.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_days.setWidgetResizable(True)
        self.scrollAreaWidgetContents_days = QWidget()
        self.scrollAreaWidgetContents_days.setObjectName(u"scrollAreaWidgetContents_days")
        self.scrollAreaWidgetContents_days.setGeometry(QRect(0, 0, 196, 540))
        self.verticalLayout_scroll_content = QVBoxLayout(self.scrollAreaWidgetContents_days)
        self.verticalLayout_scroll_content.setSpacing(0)
        self.verticalLayout_scroll_content.setObjectName(u"verticalLayout_scroll_content")
        self.verticalLayout_scroll_content.setContentsMargins(0, 0, 0, 0)
        self.listejourney = QListWidget(self.scrollAreaWidgetContents_days)
        self.listejourney.setObjectName(u"listejourney")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listejourney.sizePolicy().hasHeightForWidth())
        self.listejourney.setSizePolicy(sizePolicy)

        self.verticalLayout_scroll_content.addWidget(self.listejourney)

        self.scrollArea_days.setWidget(self.scrollAreaWidgetContents_days)

        self.verticalLayout_sidebar.addWidget(self.scrollArea_days)

        self.ajouterjournee = QPushButton(self.leftSidebarWidget)
        self.ajouterjournee.setObjectName(u"ajouterjournee")

        self.verticalLayout_sidebar.addWidget(self.ajouterjournee)


        self.horizontalLayout_main.addWidget(self.leftSidebarWidget)

        self.mainContentArea = QWidget(self.centralwidget)
        self.mainContentArea.setObjectName(u"mainContentArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainContentArea.sizePolicy().hasHeightForWidth())
        self.mainContentArea.setSizePolicy(sizePolicy1)
        self.verticalLayout_mainContent = QVBoxLayout(self.mainContentArea)
        self.verticalLayout_mainContent.setSpacing(15)
        self.verticalLayout_mainContent.setObjectName(u"verticalLayout_mainContent")
        self.verticalLayout_mainContent.setContentsMargins(20, 10, 20, 20)
        self.headerRowWidget = QWidget(self.mainContentArea)
        self.headerRowWidget.setObjectName(u"headerRowWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.headerRowWidget.sizePolicy().hasHeightForWidth())
        self.headerRowWidget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_header = QHBoxLayout(self.headerRowWidget)
        self.horizontalLayout_header.setSpacing(0)
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.horizontalLayout_header.setContentsMargins(0, 0, 0, 0)
        self.welcomeLabel = QLabel(self.headerRowWidget)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        self.welcomeLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_header.addWidget(self.welcomeLabel)


        self.verticalLayout_mainContent.addWidget(self.headerRowWidget)

        self.statsTimelineRowWidget = QWidget(self.mainContentArea)
        self.statsTimelineRowWidget.setObjectName(u"statsTimelineRowWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.statsTimelineRowWidget.sizePolicy().hasHeightForWidth())
        self.statsTimelineRowWidget.setSizePolicy(sizePolicy3)
        self.horizontalLayout_statsTimeline = QHBoxLayout(self.statsTimelineRowWidget)
        self.horizontalLayout_statsTimeline.setSpacing(15)
        self.horizontalLayout_statsTimeline.setObjectName(u"horizontalLayout_statsTimeline")
        self.horizontalLayout_statsTimeline.setContentsMargins(0, 0, 0, 0)
        self.frame_1 = QFrame(self.statsTimelineRowWidget)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setMinimumSize(QSize(150, 100))
        self.frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_1 = QVBoxLayout(self.frame_1)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.label_1 = QLabel(self.frame_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_1.addWidget(self.label_1)

        self.description_1 = QLabel(self.frame_1)
        self.description_1.setObjectName(u"description_1")
        sizePolicy.setHeightForWidth(self.description_1.sizePolicy().hasHeightForWidth())
        self.description_1.setSizePolicy(sizePolicy)
        self.description_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.description_1.setWordWrap(True)

        self.verticalLayout_1.addWidget(self.description_1)


        self.horizontalLayout_statsTimeline.addWidget(self.frame_1)

        self.frame_2 = QFrame(self.statsTimelineRowWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(150, 100))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.description_2 = QLabel(self.frame_2)
        self.description_2.setObjectName(u"description_2")
        sizePolicy.setHeightForWidth(self.description_2.sizePolicy().hasHeightForWidth())
        self.description_2.setSizePolicy(sizePolicy)
        self.description_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.description_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.description_2)


        self.horizontalLayout_statsTimeline.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.statsTimelineRowWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(150, 100))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.description_3 = QLabel(self.frame_3)
        self.description_3.setObjectName(u"description_3")
        sizePolicy.setHeightForWidth(self.description_3.sizePolicy().hasHeightForWidth())
        self.description_3.setSizePolicy(sizePolicy)
        self.description_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.description_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.description_3)


        self.horizontalLayout_statsTimeline.addWidget(self.frame_3)

        self.horizontalSpacer_stats_timeline = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_statsTimeline.addItem(self.horizontalSpacer_stats_timeline)

        self.rightAreaWidget = QWidget(self.statsTimelineRowWidget)
        self.rightAreaWidget.setObjectName(u"rightAreaWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.rightAreaWidget.sizePolicy().hasHeightForWidth())
        self.rightAreaWidget.setSizePolicy(sizePolicy4)
        self.rightAreaWidget.setMinimumSize(QSize(180, 0))
        self.verticalLayout_right = QVBoxLayout(self.rightAreaWidget)
        self.verticalLayout_right.setObjectName(u"verticalLayout_right")
        self.verticalLayout_right.setContentsMargins(0, 0, 0, 0)
        self.timelineLabel = QLabel(self.rightAreaWidget)
        self.timelineLabel.setObjectName(u"timelineLabel")
        self.timelineLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_right.addWidget(self.timelineLabel)

        self.button7Days = QPushButton(self.rightAreaWidget)
        self.button7Days.setObjectName(u"button7Days")

        self.verticalLayout_right.addWidget(self.button7Days)

        self.button30Days = QPushButton(self.rightAreaWidget)
        self.button30Days.setObjectName(u"button30Days")

        self.verticalLayout_right.addWidget(self.button30Days)

        self.buttonSinceStart = QPushButton(self.rightAreaWidget)
        self.buttonSinceStart.setObjectName(u"buttonSinceStart")

        self.verticalLayout_right.addWidget(self.buttonSinceStart)

        self.changer_graph = QPushButton(self.rightAreaWidget)
        self.changer_graph.setObjectName(u"changer_graph")

        self.verticalLayout_right.addWidget(self.changer_graph)

        self.verticalSpacer_right = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_right.addItem(self.verticalSpacer_right)


        self.horizontalLayout_statsTimeline.addWidget(self.rightAreaWidget)


        self.verticalLayout_mainContent.addWidget(self.statsTimelineRowWidget)

        self.graphsRowWidget = QWidget(self.mainContentArea)
        self.graphsRowWidget.setObjectName(u"graphsRowWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.graphsRowWidget.sizePolicy().hasHeightForWidth())
        self.graphsRowWidget.setSizePolicy(sizePolicy5)
        self.horizontalLayout_graphs = QHBoxLayout(self.graphsRowWidget)
        self.horizontalLayout_graphs.setSpacing(15)
        self.horizontalLayout_graphs.setObjectName(u"horizontalLayout_graphs")
        self.horizontalLayout_graphs.setContentsMargins(0, 0, 0, 0)
        self.bottomLeftFrame = QFrame(self.graphsRowWidget)
        self.bottomLeftFrame.setObjectName(u"bottomLeftFrame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.bottomLeftFrame.sizePolicy().hasHeightForWidth())
        self.bottomLeftFrame.setSizePolicy(sizePolicy6)
        self.bottomLeftFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomLeftFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout = QVBoxLayout(self.bottomLeftFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.legraph1 = QWidget(self.bottomLeftFrame)
        self.legraph1.setObjectName(u"legraph1")

        self.verticalLayout.addWidget(self.legraph1)


        self.horizontalLayout_graphs.addWidget(self.bottomLeftFrame)

        self.bottomRightFrame = QFrame(self.graphsRowWidget)
        self.bottomRightFrame.setObjectName(u"bottomRightFrame")
        sizePolicy6.setHeightForWidth(self.bottomRightFrame.sizePolicy().hasHeightForWidth())
        self.bottomRightFrame.setSizePolicy(sizePolicy6)
        self.bottomRightFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomRightFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.bottomRightFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.legraph2 = QWidget(self.bottomRightFrame)
        self.legraph2.setObjectName(u"legraph2")

        self.horizontalLayout.addWidget(self.legraph2)


        self.horizontalLayout_graphs.addWidget(self.bottomRightFrame)


        self.verticalLayout_mainContent.addWidget(self.graphsRowWidget)


        self.horizontalLayout_main.addWidget(self.mainContentArea)

        dashboard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dashboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        dashboard.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dashboard)
        self.statusbar.setObjectName(u"statusbar")
        dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(dashboard)

        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"Sport Tracker", None))
        dashboard.setStyleSheet(QCoreApplication.translate("dashboard", u"\n"
"/* Global Styles */\n"
"QMainWindow {\n"
"    background-color: #F5F5F7; /* Light gray background */\n"
"}\n"
"\n"
"QWidget {\n"
"    color: #333333; /* Default text color */\n"
"    /* font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif; */\n"
"}\n"
"\n"
"/* Sidebar Styling */\n"
"#leftSidebarWidget {\n"
"    background-color: #E8E8ED; /* Slightly darker gray for sidebar */\n"
"    border-right: 1px solid #DCDCDC; /* Subtle separator line */\n"
"}\n"
"\n"
"/* Main Content Area - Give it some padding */\n"
"#mainContentArea {\n"
"    background-color: transparent; /* Make container transparent */\n"
"    border: none;\n"
"}\n"
"\n"
"/* Transparent background for layout containers */\n"
"#statsTimelineRowWidget, #graphsRowWidget {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"/* Search Input Styling */\n"
"QLineEdit {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #DCDCDC;\n"
"    border-radius: 5px;\n"
"    pad"
                        "ding: 6px 10px; /* Slightly more padding */\n"
"    min-height: 24px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #007AFF; /* Blue border on focus */\n"
"}\n"
"\n"
"/* List Widget Styling */\n"
"QListWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: none; /* Remove default border */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 8px 10px; /* More padding */\n"
"    border-bottom: 1px solid #F0F0F0; /* Subtle separator for items */\n"
"}\n"
"QListWidget::item:last {\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #007AFF; /* Blue selection */\n"
"    color: #FFFFFF; /* White text for selected item */\n"
"    border-radius: 4px; /* Slightly rounded selection */\n"
"}\n"
"\n"
"QListWidget::item:hover:!selected { /* Hover, but not selected */\n"
"     background-color: #E8F3FF; /* Very light blue hover */\n"
"     color: #222222;\n"
"     border-radius: 4px;\n"
"}\n"
"\n"
"/* Button Styling */\n"
"QPushButt"
                        "on {\n"
"    background-color: #007AFF; /* Blue background */\n"
"    color: #FFFFFF; /* White text */\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px;\n"
"    min-height: 24px; /* Match input field roughly */\n"
"    font-weight: 500; /* Medium weight */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3395FF; /* Lighter blue on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #005ECB; /* Darker blue when pressed */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"     background-color: #DCDCDC;\n"
"     color: #A0A0A0;\n"
"}\n"
"\n"
"#ajouterjournee {\n"
"    margin-top: 8px; /* Add some space above the add button */\n"
"}\n"
"\n"
"/* Frame Styling (Cards) */\n"
"QFrame {\n"
"    background-color: #FFFFFF; /* White background for content areas */\n"
"    border: 1px solid #E0E0E0; /* Very subtle border */\n"
"    border-radius: 8px; /* Rounded corners for frames */\n"
"}\n"
"\n"
"/* Specific Labels */\n"
"#welcomeLabel {\n"
"    font-size: 14pt; /* Sli"
                        "ghtly smaller */\n"
"    font-weight: normal; /* Less emphasis */\n"
"    color: #555555; /* Grayer text */\n"
"    padding: 10px 0 10px 10px; /* Padding Top, Right, Bottom, Left */\n"
"}\n"
"\n"
"#titleLabel {\n"
"    font-size: 18pt; /* Larger for page title */\n"
"    font-weight: bold;\n"
"    color: #222222; /* Darker text */\n"
"    padding: 10px 10px 10px 0; /* Padding Top, Right, Bottom, Left */\n"
"    border-bottom: none; /* Remove the previous border */\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Labels inside Frames - ensure they don't inherit frame border/bg */\n"
"QFrame QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 0px; /* Reset border-radius */\n"
"}\n"
"\n"
"#label_1, #label_2, #label_3 {\n"
"    font-weight: bold;\n"
"    padding: 8px 8px 4px 8px; /* Adjust padding */\n"
"    color: #333333;\n"
"    font-size: 11pt;\n"
"}\n"
"#description_1, #description_2, #description_3 {\n"
"    padding: 4px 8px 8px 8px; /* Adjust padding */\n"
" "
                        "   color: #555555;\n"
"}\n"
"\n"
"\n"
"/* Scroll Area Styling */\n"
"QScrollArea {\n"
"  border: none; /* Remove border from scroll area itself */\n"
"  background-color: transparent; /* Make background transparent */\n"
"}\n"
"\n"
"/* Scroll Bar Styling (macOS like) */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #E8E8ED; /* Match sidebar background */\n"
"    width: 8px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #B0B0B0; /* Gray handle */\n"
"    min-height: 25px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #909090; /* Darker handle on hover */\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"/* Remove border from specific containers if graph handles drawing "
                        "*/\n"
"#legraph1, #legraph2 {\n"
"    border: none;\n"
"    background-color: transparent; /* Let the parent frame provide bg */\n"
"}\n"
"\n"
"/* Style the timeline area */\n"
"#rightAreaWidget {\n"
"    background-color: transparent; /* Make container transparent */\n"
"    border: none;\n"
"}\n"
"#timelineLabel { /* Style the 'timeline' label */\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"    border-radius: 5px;\n"
"    border: none; /* Removed border, maybe rely on card border if put inside one */\n"
"    background-color: transparent; /* Remove background */\n"
"    padding: 8px 0; /* Vertical padding */\n"
"    margin-bottom: 5px; /* Space below label */\n"
"    color: #444444;\n"
"}\n"
"#rightAreaWidget QPushButton { /* Buttons in this area */\n"
"    padding: 6px 12px; /* Slightly smaller padding */\n"
"    min-height: 22px;\n"
"}\n"
"\n"
"   ", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("dashboard", u"Recherche jours...", None))
        self.label.setText(QCoreApplication.translate("dashboard", u"appuyer sur les dates pour modifier", None))
#if QT_CONFIG(tooltip)
        self.listejourney.setToolTip(QCoreApplication.translate("dashboard", u"Liste des jours", None))
#endif // QT_CONFIG(tooltip)
        self.ajouterjournee.setText(QCoreApplication.translate("dashboard", u"Ajouter Journ\u00e9e", None))
        self.welcomeLabel.setText(QCoreApplication.translate("dashboard", u"Bienvenue", None))
        self.label_1.setText(QCoreApplication.translate("dashboard", u"Stat 1", None))
        self.description_1.setText(QCoreApplication.translate("dashboard", u"Description", None))
        self.label_2.setText(QCoreApplication.translate("dashboard", u"Stat 2", None))
        self.description_2.setText(QCoreApplication.translate("dashboard", u"Description", None))
        self.label_3.setText(QCoreApplication.translate("dashboard", u"Stat 3", None))
        self.description_3.setText(QCoreApplication.translate("dashboard", u"Description", None))
        self.timelineLabel.setText(QCoreApplication.translate("dashboard", u"Timeline", None))
        self.button7Days.setText(QCoreApplication.translate("dashboard", u"7 Derniers Jours", None))
        self.button30Days.setText(QCoreApplication.translate("dashboard", u"30 Derniers Jours", None))
        self.buttonSinceStart.setText(QCoreApplication.translate("dashboard", u"Depuis le D\u00e9but", None))
        self.changer_graph.setText(QCoreApplication.translate("dashboard", u"changer de graph", None))
    # retranslateUi

