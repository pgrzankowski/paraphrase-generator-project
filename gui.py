from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWidgets import QListWidgetItem

import sys

from ui_paraphrase_generator import Ui_MainWindow
from operations import swap_text, add_text
from poems import get_authors


class ParaphraseGeneratorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupAuthorList()
        self._setupOperations()
        self.ui.stack.setCurrentIndex(0)

    def _setupOperations(self):
        self.ui.swapRhymes.clicked.connect(self._swapRhymes)
        self.ui.swapSynonyms.clicked.connect(self._swapSynonyms)
        self.ui.addAdjectives.clicked.connect(self._addAdjectives)

    def _swapRhymes(self):
        input_text = self.ui.inputText.toPlainText()
        self.ui.outputText.setText(swap_text(input_text, 'rhymes'))

    def _swapSynonyms(self):
        input_text = self.ui.inputText.toPlainText()
        self.ui.outputText.setText(swap_text(input_text, 'synonyms'))

    def _addAdjectives(self):
        input_text = self.ui.inputText.toPlainText()
        self.ui.outputText.setText(add_text(input_text, 'adjectives'))

    def _setupAuthorList(self):
        authors = get_authors()
        for author in authors:
            item = QListWidgetItem(str(author))
            item.author = author
            self.ui.artistList.addItem(item)
        self.ui.artistList.itemClicked.connect(self._selectAuthor)
        self.ui.titleList.itemClicked.connect(self._selectTitle)

    def _selectAuthor(self, item):
        self.ui.stack.setCurrentIndex(1)
        titles = item.author.titles()
        self.ui.titleList.clear()
        for title in titles:
            title_item = QListWidgetItem(title.title())
            title_item.title = title
            self.ui.titleList.addItem(title_item)

    def _selectTitle(self, item):
        poem = item.title.text()
        self.ui.inputText.setPlainText(poem)


def guiMain(args):
    app = QApplication(args)
    window = ParaphraseGeneratorWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
