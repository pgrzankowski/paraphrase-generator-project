from PySide2.QtWidgets import QApplication, QMainWindow

import sys

from ui_paraphrase_generator import Ui_MainWindow
from operations import swap_rhymes, swap_synonyms, add_adjectives

class ParaphraseGeneratorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupOperations()

    def _setupOperations(self):
        self.ui.swapRhymes.clicked.connect(self._swapRhymes)
        self.ui.swapSynonyms.clicked.connect(self._swapSynonyms)
        self.ui.addAdjectives.clicked.connect(self._addAdjectives)

    def _swapRhymes(self):
        input_text = self.ui.inputText.toPlainText()
        self.ui.outputText.setText(swap_rhymes(input_text))

    def _swapSynonyms(self):
        input_text = self.ui.inputText.toPlainText()
        self.ui.outputText.setText(swap_synonyms(input_text))

    def _addAdjectives(self):
        input_text = self.ui.inputText.toPlainText()
        self.ui.outputText.setText(add_adjectives(input_text))


def guiMain(args):
    app = QApplication(args)
    window = ParaphraseGeneratorWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
