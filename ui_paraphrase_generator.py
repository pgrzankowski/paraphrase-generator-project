# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paraphrase_generator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftWidget = QWidget(self.centralwidget)
        self.leftWidget.setObjectName(u"leftWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftWidget.sizePolicy().hasHeightForWidth())
        self.leftWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.leftWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.enterText = QLabel(self.leftWidget)
        self.enterText.setObjectName(u"enterText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enterText.sizePolicy().hasHeightForWidth())
        self.enterText.setSizePolicy(sizePolicy1)
        self.enterText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.enterText)

        self.inputText = QTextEdit(self.leftWidget)
        self.inputText.setObjectName(u"inputText")

        self.verticalLayout_2.addWidget(self.inputText)


        self.horizontalLayout_2.addWidget(self.leftWidget)

        self.rightWidget = QWidget(self.centralwidget)
        self.rightWidget.setObjectName(u"rightWidget")
        self.verticalLayout = QVBoxLayout(self.rightWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.choseOperation = QLabel(self.rightWidget)
        self.choseOperation.setObjectName(u"choseOperation")
        sizePolicy1.setHeightForWidth(self.choseOperation.sizePolicy().hasHeightForWidth())
        self.choseOperation.setSizePolicy(sizePolicy1)
        self.choseOperation.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.choseOperation)

        self.widget = QWidget(self.rightWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.swapRhymes = QPushButton(self.widget)
        self.swapRhymes.setObjectName(u"swapRhymes")

        self.verticalLayout_3.addWidget(self.swapRhymes)

        self.swapSynonyms = QPushButton(self.widget)
        self.swapSynonyms.setObjectName(u"swapSynonyms")

        self.verticalLayout_3.addWidget(self.swapSynonyms)

        self.addAdjectives = QPushButton(self.widget)
        self.addAdjectives.setObjectName(u"addAdjectives")

        self.verticalLayout_3.addWidget(self.addAdjectives)


        self.verticalLayout.addWidget(self.widget)

        self.outputText = QLabel(self.rightWidget)
        self.outputText.setObjectName(u"outputText")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.outputText.sizePolicy().hasHeightForWidth())
        self.outputText.setSizePolicy(sizePolicy2)
        self.outputText.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.outputText)


        self.horizontalLayout_2.addWidget(self.rightWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.enterText.setText(QCoreApplication.translate("MainWindow", u"Enter text to paraphrase", None))
        self.choseOperation.setText(QCoreApplication.translate("MainWindow", u"Choose Operation", None))
        self.swapRhymes.setText(QCoreApplication.translate("MainWindow", u"Swap rhymes", None))
        self.swapSynonyms.setText(QCoreApplication.translate("MainWindow", u"Swap Synonyms", None))
        self.addAdjectives.setText(QCoreApplication.translate("MainWindow", u"Add adjectives", None))
        self.outputText.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

