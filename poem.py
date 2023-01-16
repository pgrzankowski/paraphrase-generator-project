import requests
import json


with open('poem_endpoints.json', 'r') as file:
    urls = json.load(file)


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
        return self._name

    @property
    def name(self):
        return self._name

    def poems(self):
        """
        Returns list of poems of an author.
        """
        all_poems = requests.get(
            urls['titles'].format(author=self._name)
            ).json()
        poems = []
        for poem in all_poems:
            poems.append(Poem(self, poem['title']))
        return poems


class Poem:
    """
    Class which can be used to store poem
    objects.

    :param author: author of the poem
    :type author: Author

    :param title: title of the poem
    :type title: str
    """
    def __init__(self, author, title):
        self._author = author
        self._title = title

    def __str__(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    def text(self):
        """
        Retrives text of a poem from database and returns it.
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
