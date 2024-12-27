from PyQt6.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from PyQt6 import uic
from requests import Timeout, ConnectionError
import sys
from utils.operations import (swap_synonyms,
                              swap_rhymes,
                              swap_homophones,
                              swap_homonyms,
                              add_adjectives)
from utils.poem import get_authors
from utils.song import get_song
from assistant import Assistant


class ParaphraseGeneratorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/paraphrase_generator.ui', self)
        self._setup_author_list()
        self._setup_assistant()
        self._setup_operations()
        self._setup_search_details()
        self._setup_tab_bar()
        self._setup_keywords()
        self.stack.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.showMaximized()

    def _setup_assistant(self):
        """
        Method which sets up asssistant operations.
        """
        self._assistant = Assistant()
        self.runAssistantButton.clicked.connect(self._run_assistant)

    def _run_assistant(self):
        user_prompt = self.userPrompt.toPlainText()
        to_paraphrase = self.inputText.toPlainText()
        self.assistantComment.setPlainText('Paraphrasing...')
        try:
            QApplication.processEvents()
            response = self._assistant.get_response(to_paraphrase, user_prompt)
            # self.outputText.setText(response.paraphrased)
            # self.assistantComment.setPlainText(response.comment)
            self.outputText.setText(response)
            self.assistantComment.setPlainText('Paraphrased')
        except Exception:
            self.assistantComment.setPlainText('Couldn\'t connect to assistant\nPlease try again')

    def _setup_operations(self):
        """
        Method wich assigns operations to given buttons.
        """
        self.swapRhymes.clicked.connect(self._swap_rhymes)
        self.swapSynonyms.clicked.connect(self._swap_synonyms)
        self.swapHomophones.clicked.connect(self._swap_homophones)
        self.swapHomonyms.clicked.connect(self._swap_homonyms)
        self.addAdjectives.clicked.connect(self._add_adjectives)

    def _swap_rhymes(self):
        """
        Method which swaps given keywords in text for their
        rhymes and writes it out as output.
        """
        input_text, keyword = self._get_input_data()
        self.outputText.setText(swap_rhymes(input_text, keyword))

    def _swap_synonyms(self):
        """
        Method which swaps given keywords in text for their
        synonyms and writes it out as output.
        """
        input_text, keyword = self._get_input_data()
        self.outputText.setText(swap_synonyms(input_text, keyword))

    def _swap_homophones(self):
        """
        Method which swaps given keywords in text for their
        homophones(words which sound alike) and writes it out as output.
        """
        input_text, keyword = self._get_input_data()
        self.outputText.setText(swap_homophones(input_text, keyword))

    def _swap_homonyms(self):
        """
        Method which swaps given keywords in text for their
        homonyms(words which are spelled alike) and writes it out as output.
        """
        input_text, keyword = self._get_input_data()
        self.outputText.setText(swap_homonyms(input_text, keyword))

    def _add_adjectives(self):
        """
        Method which adds adjectives before given keywords in text
        and writes it out as output.
        """
        input_text, keyword = self._get_input_data()
        self.outputText.setText(add_adjectives(input_text, keyword))

    def _get_input_data(self):
        """
        Method which retrives input data:
        text to paraphrase and keywords
        and returns them in tuple.
        """
        input_text = self.inputText.toPlainText()
        keywords = self.keywords
        return input_text, keywords

    def _setup_keywords(self):
        """
        Method which assigns operations to keyword buttons.
        """
        self.keywords = []
        self.addKeyword.clicked.connect(self._add_keyword)
        self.clearKeywords.clicked.connect(self._clear_keywords)

    def _clear_keywords(self):
        """
        Method which clears keywords.
        """
        self.keywords = []
        self.keywordsList.clear()
        self.inputKeyword.clear()

    def _add_keyword(self):
        """
        Method which adds new keywords to the list.
        """
        new_keyword = self.inputKeyword.text().lower().strip()
        keywords = self.keywords
        if new_keyword and len(keywords) < 10 and new_keyword not in keywords:
            self.keywords.append(new_keyword)
            self.keywordsList.setText((', '.join(keywords).lstrip(', ')))
            self.inputKeyword.clear()

    def _setup_author_list(self):
        """
        Method which sets up list of authors as a QListWidget.
        """
        authors = get_authors()
        for author in authors:
            item = QListWidgetItem(str(author))
            item.author = author
            self.artistList.addItem(item)
        self.artistList.itemClicked.connect(self._select_author)
        self.titleList.itemClicked.connect(self._select_title)

    def _select_author(self, item):
        """
        Method which sets up list of poems from selected author
        as a QListWidget.
        """
        self.stack.setCurrentIndex(1)
        poems = item.author.poems()
        self.titleList.clear()
        for poem in poems:
            poem_item = QListWidgetItem(poem.title)
            poem_item.title = poem
            self.titleList.addItem(poem_item)

    def _select_title(self, item):
        """
        Method which writes out chosen poem into an
        inputPlainText widget.
        """
        poem = item.title.text()
        self.inputText.setPlainText(poem)

    def _setup_tab_bar(self):
        """
        Method which sets up TabBar.
        """
        self.tabWidget.currentChanged.connect(self._clear_texts)

    def _clear_texts(self):
        """
        Method which clears inputPlainText widget, search results
        in song tab and outputPlainText widget.
        """
        self.inputText.clear()
        self.resultsLabel.clear()
        self.foundArtist.clear()
        self.foundTitle.clear()
        self.outputText.clear()
        self.titleInput.clear()
        self.artistInput.clear()

    def _setup_search_details(self):
        """
        Method which sets up song searching system.
        """
        self.searchButton.clicked.connect(self._search_for_song)

    def _search_for_song(self):
        """
        Method which searches for a song from given title and artist
        and writes out lyrics of song found in database into
        inputPlainText widget.
        If not found, or couldn't connect writes out error message.
        """
        self.resultsLabel.setText('Searching...')
        self.foundTitle.clear()
        self.foundArtist.clear()
        QApplication.processEvents()
        title = self.titleInput.text()
        artist = self.artistInput.text()
        try:
            song = get_song(title, artist)
            self.inputText.setPlainText(song.lyrics)
            self.resultsLabel.setText('Search results:')
            self.foundTitle.setText('Title: ' + song.title)
            self.foundArtist.setText('Artist: ' + song.artist)
        except AttributeError:
            message = 'Song not found'
            self.inputText.setPlainText(message)
        except (Timeout, ConnectionError):
            message = 'Couldn\'t connect to database\nPlease try again'
            self.inputText.setPlainText(message)


def main(args):
    app = QApplication(args)
    window = ParaphraseGeneratorWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    main(sys.argv)
