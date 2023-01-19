from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWidgets import QListWidgetItem
from ui_paraphrase_generator import Ui_MainWindow
from operations import (
    swap_synonyms,
    swap_rhymes,
    swap_homophones,
    swap_homonyms,
    add_adjectives
)
from poem import get_authors
from song import get_song
from requests import Timeout, ConnectionError
import sys


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
        self.showMaximized()

    def _setupOperations(self):
        """
        Method wich assigns operations to given buttons.
        """
        self.ui.swapRhymes.clicked.connect(self._swapRhymes)
        self.ui.swapSynonyms.clicked.connect(self._swapSynonyms)
        self.ui.swapHomophones.clicked.connect(self._swapHomophones)
        self.ui.swapHomonyms.clicked.connect(self._swapHomonyms)
        self.ui.addAdjectives.clicked.connect(self._addAdjectives)

    def _swapRhymes(self):
        """
        Method which swaps given keywords in text for their
        rhymes and writes it out as output.
        """
        input_text, keyword = self._getInputData()
        self.ui.outputText.setText(swap_rhymes(input_text, keyword))

    def _swapSynonyms(self):
        """
        Method which swaps given keywords in text for their
        synonyms and writes it out as output.
        """
        input_text, keyword = self._getInputData()
        self.ui.outputText.setText(swap_synonyms(input_text, keyword))

    def _swapHomophones(self):
        """
        Method which swaps given keywords in text for their
        homophones(words which sound alike) and writes it out as output.
        """
        input_text, keyword = self._getInputData()
        self.ui.outputText.setText(swap_homophones(input_text, keyword))

    def _swapHomonyms(self):
        """
        Method which swaps given keywords in text for their
        homonyms(words which are spelled alike) and writes it out as output.
        """
        input_text, keyword = self._getInputData()
        self.ui.outputText.setText(swap_homonyms(input_text, keyword))

    def _addAdjectives(self):
        """
        Method which adds adjectives before given keywords in text
        and writes it out as output.
        """
        input_text, keyword = self._getInputData()
        self.ui.outputText.setText(add_adjectives(input_text, keyword))

    def _getInputData(self):
        """
        Method which retrives input data:
        text to paraphrase and keywords
        and returns them in tuple.
        """
        input_text = self.ui.inputText.toPlainText()
        keywords = self.keywords
        return input_text, keywords

    def _setupKeywords(self):
        """
        Method which assigns operations to keyword buttons.
        """
        self.keywords = []
        self.ui.addKeyword.clicked.connect(self._addKeyword)
        self.ui.clearKeywords.clicked.connect(self._clearKeywords)

    def _clearKeywords(self):
        """
        Method which clears keywords.
        """
        self.keywords = []
        self.ui.keywordsList.clear()
        self.ui.inputKeyword.clear()

    def _addKeyword(self):
        """
        Method which adds new keywords to the list.
        """
        new_keyword = self.ui.inputKeyword.text().lower().strip()
        keywords = self.keywords
        if new_keyword and len(keywords) < 10 and new_keyword not in keywords:
            self.keywords.append(new_keyword)
            self.ui.keywordsList.setText((', '.join(keywords).lstrip(', ')))
            self.ui.inputKeyword.clear()

    def _setupAuthorList(self):
        """
        Method which sets up list of authors as a QListWidget.
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
        Method which sets up list of poems from selected author
        as a QListWidget.
        """
        self.ui.stack.setCurrentIndex(1)
        poems = item.author.poems()
        self.ui.titleList.clear()
        for poem in poems:
            poem_item = QListWidgetItem(poem.title)
            poem_item.title = poem
            self.ui.titleList.addItem(poem_item)

    def _selectTitle(self, item):
        """
        Method which writes out chosen poem into an
        inputPlainText widget.
        """
        poem = item.title.text()
        self.ui.inputText.setPlainText(poem)

    def _setupTabBar(self):
        """
        Method which sets up TabBar.
        """
        self.ui.tabWidget.currentChanged.connect(self._clearTexts)

    def _clearTexts(self):
        """
        Method which clears inputPlainText widget, search results
        in song tab and outputPlainText widget.
        """
        self.ui.inputText.clear()
        self.ui.resultsLabel.clear()
        self.ui.foundArtist.clear()
        self.ui.foundTitle.clear()
        self.ui.outputText.clear()
        self.ui.titleInput.clear()
        self.ui.artistInput.clear()

    def _setupSearchDetails(self):
        """
        Method which sets up song searching system.
        """
        self.ui.searchButton.clicked.connect(self._searchForSong)

    def _searchForSong(self):
        """
        Method which searches for a song from given title and artist
        and writes out lyrics of song found in database into
        inputPlainText widget.
        If not found, or couldn't connect writes out error message.
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
        except (Timeout, ConnectionError):
            message = 'Couldn\'t connect to database\nPlease try again'
            self.ui.inputText.setPlainText(message)


def guiMain(args):
    app = QApplication(args)
    window = ParaphraseGeneratorWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
