from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWidgets import QListWidgetItem

import sys

from ui_paraphrase_generator import Ui_MainWindow
from operations import swap_synonyms, swap_rhymes, add_adjectives
from poem import get_authors
from song import get_song
from requests import Timeout


class ParaphraseGeneratorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupAuthorList()
        self._setupOperations()
        self._setupSearchDetails()
        self._setupTabBar()
        self._setupKeywords()
        self.ui.stack.setCurrentIndex(0)
        self.ui.tabWidget.setCurrentIndex(0)

    def _setupOperations(self):
        """
        Assigns operations to given buttons.
        """
        self.ui.swapRhymes.clicked.connect(self._swapRhymes)
        self.ui.swapSynonyms.clicked.connect(self._swapSynonyms)
        self.ui.addAdjectives.clicked.connect(self._addAdjectives)

    def _swapRhymes(self):
        """
        Writes out output after its transformed with
        swap_rhymes function.
        """
        input_text, keyword = self._getInputData()
        self.ui.outputText.setText(swap_rhymes(input_text, keyword))

    def _swapSynonyms(self):
        """
        Writes out output after its transformed with
        swap_synonyms function.
        """
        input_text, keyword = self._getInputData()
        self.ui.outputText.setText(swap_synonyms(input_text, keyword))

    def _addAdjectives(self):
        """
        Writes out output after its transformed with
        add_adjectives function.
        """
        input_text, keyword = self._getInputData()
        self.ui.outputText.setText(add_adjectives(input_text, keyword))

    def _getInputData(self):
        input_text = self.ui.inputText.toPlainText()
        keywords = self.keywords
        return input_text, keywords

    def _setupKeywords(self):
        self.keywords = []
        self.ui.addKeyword.clicked.connect(self._addKeyword)
        self.ui.clearKeywords.clicked.connect(self._clearKeywords)

    def _clearKeywords(self):
        self.keywords = []
        self.ui.keywordsList.clear()

    def _addKeyword(self):
        new_keyword = self.ui.inputKeyword.text().lower()
        keywords = self.keywords
        if new_keyword and len(keywords) < 5 and new_keyword not in keywords:
            self.keywords.append(new_keyword)
            self.ui.keywordsList.setText((', '.join(keywords).lstrip(', ')))
            self.ui.inputKeyword.clear()

    def _setupAuthorList(self):
        """
        Sets up list of authors in a QListWidget.
        """
        authors = get_authors()
        for author in authors:
            item = QListWidgetItem(str(author))
            item.author = author
            self.ui.artistList.addItem(item)
        self.ui.artistList.itemClicked.connect(self._selectAuthor)
        self.ui.titleList.itemClicked.connect(self._selectTitle)

    def _selectAuthor(self, item):
        """
        Sets up list of poems from selected author.
        """
        self.ui.stack.setCurrentIndex(1)
        titles = item.author.titles()
        self.ui.titleList.clear()
        for title in titles:
            title_item = QListWidgetItem(title.title())
            title_item.title = title
            self.ui.titleList.addItem(title_item)

    def _selectTitle(self, item):
        """
        Writes out chosen poem into an input
        PlainText widget.
        """
        poem = item.title.text()
        self.ui.inputText.setPlainText(poem)

    def _setupTabBar(self):
        """
        Calls _clearInput method.
        """
        self.ui.tabWidget.currentChanged.connect(self._clearInput)

    def _clearInput(self):
        """
        Clears input PlainText widget and search results
        in song tab.
        """
        self.ui.inputText.clear()
        self.ui.resultsLabel.clear()
        self.ui.foundArtist.clear()
        self.ui.foundTitle.clear()

    def _setupSearchDetails(self):
        """
        Calls _searchForSong method.
        """
        self.ui.searchButton.clicked.connect(self._searchForSong)

    def _searchForSong(self):
        """
        Searches for a song from given title and artist
        and writes out lyrics of song found in database
        into input PlainText widget.
        """
        title = self.ui.titleInput.text()
        artist = self.ui.artistInput.text()
        try:
            song = get_song(title, artist)
            self.ui.inputText.setPlainText(song.lyrics)
            self.ui.resultsLabel.setText('Search results:')
            self.ui.foundTitle.setText('Title: ' + song.title)
            self.ui.foundArtist.setText('Artist: ' + song.artist)
        except AttributeError:
            message = 'Song not found'
            self.ui.inputText.setPlainText(message)
        except Timeout:
            message = 'Couldn\'t connect to database\nPlease try again'
            self.ui.inputText.setPlainText(message)


def guiMain(args):
    app = QApplication(args)
    window = ParaphraseGeneratorWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
