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
        MainWindow.resize(1081, 747)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_1 = QWidget(self.centralwidget)
        self.widget_1.setObjectName(u"widget_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
        self.widget_1.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.widget_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.searchTableLabel = QLabel(self.widget_1)
        self.searchTableLabel.setObjectName(u"searchTableLabel")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.searchTableLabel.setFont(font)
        self.searchTableLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.searchTableLabel)

        self.tabWidget = QTabWidget(self.widget_1)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.songTitleLabel = QLabel(self.tab)
        self.songTitleLabel.setObjectName(u"songTitleLabel")

        self.verticalLayout_8.addWidget(self.songTitleLabel)

        self.titleInput = QLineEdit(self.tab)
        self.titleInput.setObjectName(u"titleInput")

        self.verticalLayout_8.addWidget(self.titleInput)

        self.songArtistLabel = QLabel(self.tab)
        self.songArtistLabel.setObjectName(u"songArtistLabel")

        self.verticalLayout_8.addWidget(self.songArtistLabel)

        self.artistInput = QLineEdit(self.tab)
        self.artistInput.setObjectName(u"artistInput")

        self.verticalLayout_8.addWidget(self.artistInput)

        self.searchButton = QPushButton(self.tab)
        self.searchButton.setObjectName(u"searchButton")

        self.verticalLayout_8.addWidget(self.searchButton)

        self.resultsLabel = QLabel(self.tab)
        self.resultsLabel.setObjectName(u"resultsLabel")
        self.resultsLabel.setFont(font)

        self.verticalLayout_8.addWidget(self.resultsLabel)

        self.foundTitle = QLabel(self.tab)
        self.foundTitle.setObjectName(u"foundTitle")

        self.verticalLayout_8.addWidget(self.foundTitle)

        self.foundArtist = QLabel(self.tab)
        self.foundArtist.setObjectName(u"foundArtist")

        self.verticalLayout_8.addWidget(self.foundArtist)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.chooseAuthor = QLabel(self.tab_2)
        self.chooseAuthor.setObjectName(u"chooseAuthor")
        self.chooseAuthor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.chooseAuthor)

        self.artistList = QListWidget(self.tab_2)
        self.artistList.setObjectName(u"artistList")

        self.verticalLayout_9.addWidget(self.artistList)

        self.choosePoem = QLabel(self.tab_2)
        self.choosePoem.setObjectName(u"choosePoem")
        self.choosePoem.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.choosePoem)

        self.stack = QStackedWidget(self.tab_2)
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
        self.titleList = QListWidget(self.page_2)
        self.titleList.setObjectName(u"titleList")

        self.verticalLayout_6.addWidget(self.titleList)

        self.stack.addWidget(self.page_2)

        self.verticalLayout_9.addWidget(self.stack)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)


        self.gridLayout.addWidget(self.widget_1, 0, 0, 1, 1)

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
        self.enterText.setFont(font)
        self.enterText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.enterText)

        self.inputText = QTextEdit(self.widget_3)
        self.inputText.setObjectName(u"inputText")

        self.verticalLayout_2.addWidget(self.inputText)

        self.keywordLabel = QLabel(self.widget_3)
        self.keywordLabel.setObjectName(u"keywordLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.keywordLabel.sizePolicy().hasHeightForWidth())
        self.keywordLabel.setSizePolicy(sizePolicy3)
        self.keywordLabel.setFont(font)
        self.keywordLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.keywordLabel)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.inputKeyword = QLineEdit(self.widget_2)
        self.inputKeyword.setObjectName(u"inputKeyword")

        self.horizontalLayout.addWidget(self.inputKeyword)

        self.addKeyword = QPushButton(self.widget_2)
        self.addKeyword.setObjectName(u"addKeyword")

        self.horizontalLayout.addWidget(self.addKeyword)

        self.clearKeywords = QPushButton(self.widget_2)
        self.clearKeywords.setObjectName(u"clearKeywords")

        self.horizontalLayout.addWidget(self.clearKeywords)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.selectedKeywordsLabel = QLabel(self.widget_3)
        self.selectedKeywordsLabel.setObjectName(u"selectedKeywordsLabel")

        self.verticalLayout_2.addWidget(self.selectedKeywordsLabel)

        self.keywordsList = QLabel(self.widget_3)
        self.keywordsList.setObjectName(u"keywordsList")

        self.verticalLayout_2.addWidget(self.keywordsList)

        self.chooseOperation = QLabel(self.widget_3)
        self.chooseOperation.setObjectName(u"chooseOperation")
        sizePolicy2.setHeightForWidth(self.chooseOperation.sizePolicy().hasHeightForWidth())
        self.chooseOperation.setSizePolicy(sizePolicy2)
        self.chooseOperation.setFont(font)
        self.chooseOperation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.chooseOperation)

        self.widget = QWidget(self.widget_3)
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


        self.verticalLayout_2.addWidget(self.widget)


        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.paraphrasedTextLabel = QLabel(self.widget_4)
        self.paraphrasedTextLabel.setObjectName(u"paraphrasedTextLabel")
        self.paraphrasedTextLabel.setFont(font)
        self.paraphrasedTextLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.paraphrasedTextLabel)

        self.outputText = QTextBrowser(self.widget_4)
        self.outputText.setObjectName(u"outputText")

        self.verticalLayout.addWidget(self.outputText)


        self.gridLayout.addWidget(self.widget_4, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1081, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pharaphrase generator", None))
        self.searchTableLabel.setText(QCoreApplication.translate("MainWindow", u"Search for a song or a poem to paraphrase", None))
        self.songTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Enter title:", None))
        self.titleInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter title...", None))
        self.songArtistLabel.setText(QCoreApplication.translate("MainWindow", u"Enter artist:", None))
        self.artistInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter artist...", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.resultsLabel.setText("")
        self.foundTitle.setText("")
        self.foundArtist.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Song", None))
        self.chooseAuthor.setText(QCoreApplication.translate("MainWindow", u"Choose an author", None))
        self.choosePoem.setText(QCoreApplication.translate("MainWindow", u"Choose a poem", None))
        self.stackLabel.setText(QCoreApplication.translate("MainWindow", u"Choose Author First", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Poem", None))
        self.enterText.setText(QCoreApplication.translate("MainWindow", u"Enter text to paraphrase", None))
        self.keywordLabel.setText(QCoreApplication.translate("MainWindow", u"Select keywords to paraphrase", None))
        self.inputKeyword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter word...", None))
        self.addKeyword.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.clearKeywords.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.selectedKeywordsLabel.setText(QCoreApplication.translate("MainWindow", u"Selected keywords:", None))
        self.keywordsList.setText("")
        self.chooseOperation.setText(QCoreApplication.translate("MainWindow", u"Choose Operation", None))
        self.swapRhymes.setText(QCoreApplication.translate("MainWindow", u"Swap rhymes", None))
        self.swapSynonyms.setText(QCoreApplication.translate("MainWindow", u"Swap Synonyms", None))
        self.addAdjectives.setText(QCoreApplication.translate("MainWindow", u"Add adjectives", None))
        self.paraphrasedTextLabel.setText(QCoreApplication.translate("MainWindow", u"Paraphrased text", None))
    # retranslateUi

