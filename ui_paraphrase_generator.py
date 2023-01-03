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
        self.verticalLayout_4 = QVBoxLayout(self.leftWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.chooseArtist = QLabel(self.leftWidget)
        self.chooseArtist.setObjectName(u"chooseArtist")
        self.chooseArtist.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.chooseArtist)

        self.artistList = QListWidget(self.leftWidget)
        self.artistList.setObjectName(u"artistList")

        self.verticalLayout_4.addWidget(self.artistList)

        self.stack = QStackedWidget(self.leftWidget)
        self.stack.setObjectName(u"stack")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackLabel = QLabel(self.page)
        self.stackLabel.setObjectName(u"stackLabel")
        self.stackLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.stackLabel)

        self.stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.choosePoem = QLabel(self.page_2)
        self.choosePoem.setObjectName(u"choosePoem")
        self.choosePoem.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.choosePoem)

        self.titleList = QListWidget(self.page_2)
        self.titleList.setObjectName(u"titleList")

        self.verticalLayout_6.addWidget(self.titleList)

        self.stack.addWidget(self.page_2)

        self.verticalLayout_4.addWidget(self.stack)


        self.horizontalLayout_2.addWidget(self.leftWidget)

        self.midWidget = QWidget(self.centralwidget)
        self.midWidget.setObjectName(u"midWidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.midWidget.sizePolicy().hasHeightForWidth())
        self.midWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.midWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.enterText = QLabel(self.midWidget)
        self.enterText.setObjectName(u"enterText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enterText.sizePolicy().hasHeightForWidth())
        self.enterText.setSizePolicy(sizePolicy1)
        self.enterText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.enterText)

        self.inputText = QTextEdit(self.midWidget)
        self.inputText.setObjectName(u"inputText")

        self.verticalLayout_2.addWidget(self.inputText)


        self.horizontalLayout_2.addWidget(self.midWidget)

        self.rightWidget = QWidget(self.centralwidget)
        self.rightWidget.setObjectName(u"rightWidget")
        self.verticalLayout = QVBoxLayout(self.rightWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chooseOperation = QLabel(self.rightWidget)
        self.chooseOperation.setObjectName(u"chooseOperation")
        sizePolicy1.setHeightForWidth(self.chooseOperation.sizePolicy().hasHeightForWidth())
        self.chooseOperation.setSizePolicy(sizePolicy1)
        self.chooseOperation.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.chooseOperation)

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

        self.outputText = QTextBrowser(self.rightWidget)
        self.outputText.setObjectName(u"outputText")

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

        self.stack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.chooseArtist.setText(QCoreApplication.translate("MainWindow", u"Choose an artist", None))
        self.stackLabel.setText(QCoreApplication.translate("MainWindow", u"Choose Artist First", None))
        self.choosePoem.setText(QCoreApplication.translate("MainWindow", u"Choose a poem", None))
        self.enterText.setText(QCoreApplication.translate("MainWindow", u"Enter text to paraphrase", None))
        self.chooseOperation.setText(QCoreApplication.translate("MainWindow", u"Choose Operation", None))
        self.swapRhymes.setText(QCoreApplication.translate("MainWindow", u"Swap rhymes", None))
        self.swapSynonyms.setText(QCoreApplication.translate("MainWindow", u"Swap Synonyms", None))
        self.addAdjectives.setText(QCoreApplication.translate("MainWindow", u"Add adjectives", None))
    # retranslateUi

