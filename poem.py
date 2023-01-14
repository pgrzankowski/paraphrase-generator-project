import requests

urls = {
    'authors': 'https://poetrydb.org/author',
    'titles': 'https://poetrydb.org/author/{author}/title',
    'poem': 'https://poetrydb.org/author,title/{author};{title}'
}


def get_authors():
    """
    Retrives list of authors and returns a list
    of objects based on them.
    """
    all_authors = requests.get(urls['authors']).json()
    return [Author(author_name) for author_name in all_authors['authors']]


class Author:
    """
    A class used to represent author of the text.

    :param name: name of the author
    :type name: str
    """
    def __init__(self, name):
        self._name = name

    def __str__(self):
        """
        Returns name of the author.
        """
        return self._name

    def name(self):
        """
        Returns name of the author.
        """
        return self._name

    def titles(self):
        """
        Returns list of authors' poems.
        """
        all_poems = requests.get(
            urls['titles'].format(author=self._name)
            ).json()
        poems = []
        for poem in all_poems:
            poems.append(Poem(self, poem['title']))
        return poems


class Poem:
    def __init__(self, author, title):
        self._author = author
        self._title = title

    def __str__(self):
        return self._title

    def author(self):
        """
        Returns Author object of self.
        """
        return self._author

    def title(self):
        """
        Returns title of a poem.
        """
        return self._title

    def text(self):
        """
        Retrives text of a poem from API and returns it.
        """
        author = self._author.name()
        title = self._title
        text_item = requests.get(urls['poem'].format(
            author=author,
            title=title
            )).json()
        lines = text_item[0]['lines']
        text = ''
        for line in lines:
            text += line.strip() + '\n'
        return text
