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
        MainWindow.resize(870, 528)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_1 = QWidget(self.centralwidget)
        self.widget_1.setObjectName(u"widget_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
        self.widget_1.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.widget_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.songMainTitle = QLabel(self.widget_1)
        self.songMainTitle.setObjectName(u"songMainTitle")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.songMainTitle.setFont(font)
        self.songMainTitle.setAlignment(Qt.AlignCenter)
        self.songMainTitle.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.songMainTitle)

        self.songTitleLabel = QLabel(self.widget_1)
        self.songTitleLabel.setObjectName(u"songTitleLabel")

        self.verticalLayout_7.addWidget(self.songTitleLabel)

        self.titleInput = QLineEdit(self.widget_1)
        self.titleInput.setObjectName(u"titleInput")

        self.verticalLayout_7.addWidget(self.titleInput)

        self.songArtistLabel = QLabel(self.widget_1)
        self.songArtistLabel.setObjectName(u"songArtistLabel")

        self.verticalLayout_7.addWidget(self.songArtistLabel)

        self.artistInput = QLineEdit(self.widget_1)
        self.artistInput.setObjectName(u"artistInput")

        self.verticalLayout_7.addWidget(self.artistInput)

        self.searchButton = QPushButton(self.widget_1)
        self.searchButton.setObjectName(u"searchButton")

        self.verticalLayout_7.addWidget(self.searchButton)

        self.testOutputTitle = QLabel(self.widget_1)
        self.testOutputTitle.setObjectName(u"testOutputTitle")

        self.verticalLayout_7.addWidget(self.testOutputTitle)

        self.testOutputArtist = QLabel(self.widget_1)
        self.testOutputArtist.setObjectName(u"testOutputArtist")

        self.verticalLayout_7.addWidget(self.testOutputArtist)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget_1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.poemTitleLabel = QLabel(self.widget_2)
        self.poemTitleLabel.setObjectName(u"poemTitleLabel")
        self.poemTitleLabel.setFont(font)
        self.poemTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.poemTitleLabel)

        self.chooseArtist = QLabel(self.widget_2)
        self.chooseArtist.setObjectName(u"chooseArtist")
        self.chooseArtist.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.chooseArtist)

        self.artistList = QListWidget(self.widget_2)
        self.artistList.setObjectName(u"artistList")

        self.verticalLayout_4.addWidget(self.artistList)

        self.stack = QStackedWidget(self.widget_2)
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


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.enterText = QLabel(self.widget_3)
        self.enterText.setObjectName(u"enterText")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.enterText.sizePolicy().hasHeightForWidth())
        self.enterText.setSizePolicy(sizePolicy2)
        self.enterText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.enterText)

        self.inputText = QTextEdit(self.widget_3)
        self.inputText.setObjectName(u"inputText")

        self.verticalLayout_2.addWidget(self.inputText)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chooseOperation = QLabel(self.widget_4)
        self.chooseOperation.setObjectName(u"chooseOperation")
        sizePolicy2.setHeightForWidth(self.chooseOperation.sizePolicy().hasHeightForWidth())
        self.chooseOperation.setSizePolicy(sizePolicy2)
        self.chooseOperation.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.chooseOperation)

        self.widget = QWidget(self.widget_4)
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

        self.outputText = QTextBrowser(self.widget_4)
        self.outputText.setObjectName(u"outputText")

        self.verticalLayout.addWidget(self.outputText)


        self.horizontalLayout.addWidget(self.widget_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 870, 20))
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
        self.songMainTitle.setText(QCoreApplication.translate("MainWindow", u"Search for a song", None))
        self.songTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Enter title:", None))
        self.songArtistLabel.setText(QCoreApplication.translate("MainWindow", u"Enter artist:", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.testOutputTitle.setText(QCoreApplication.translate("MainWindow", u"test title", None))
        self.testOutputArtist.setText(QCoreApplication.translate("MainWindow", u"test artist", None))
        self.poemTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Search for a poem", None))
        self.chooseArtist.setText(QCoreApplication.translate("MainWindow", u"Choose an artist", None))
        self.stackLabel.setText(QCoreApplication.translate("MainWindow", u"Choose Artist First", None))
        self.choosePoem.setText(QCoreApplication.translate("MainWindow", u"Choose a poem", None))
        self.enterText.setText(QCoreApplication.translate("MainWindow", u"Enter text to paraphrase", None))
        self.chooseOperation.setText(QCoreApplication.translate("MainWindow", u"Choose Operation", None))
        self.swapRhymes.setText(QCoreApplication.translate("MainWindow", u"Swap rhymes", None))
        self.swapSynonyms.setText(QCoreApplication.translate("MainWindow", u"Swap Synonyms", None))
        self.addAdjectives.setText(QCoreApplication.translate("MainWindow", u"Add adjectives", None))
    # retranslateUi

