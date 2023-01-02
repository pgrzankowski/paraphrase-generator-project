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
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.authorList = QListView(self.centralwidget)
        self.authorList.setObjectName(u"authorList")

        self.horizontalLayout.addWidget(self.authorList)

        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pickAuthor = QLabel(self.page)
        self.pickAuthor.setObjectName(u"pickAuthor")
        self.pickAuthor.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.pickAuthor)

        self.stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stack.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stack)

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
        self.pickAuthor.setText(QCoreApplication.translate("MainWindow", u"Pick Author First", None))
    # retranslateUi

