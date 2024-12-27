import requests
import json


def get_poem_endpoints():
    """
    Gets dictionary of endpoints from json file.

    Result:
        urls (dict): Dictionary with certain endpoints
                     assigned to their keys.
    """
    with open('constants/poem_endpoints.json', 'r') as file:
        urls = json.load(file)
    return urls


def get_authors() -> list:
    """
    Retrives list of authors and returns a list
    of Author objects based on them.

    Returns:
        authors (list): List of Authors (objects).
    """
    urls = get_poem_endpoints()
    all_authors = requests.get(urls['authors']).json()
    return [Author(author_name) for author_name in all_authors['authors']]


class Author:
    """
    A class used to represent author of the text.

    :param name: name of the author
    :type name: str
    """
    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        """
        Returns authors name.
        """
        return self._name

    @property
    def name(self) -> str:
        """
        Returns authors name.
        """
        return self._name

    def poems(self) -> list:
        """
        Returns list of poems of an author.

        Returns:
            poems (list): List of Poems (objects) written by
                          the Author.
        """
        urls = get_poem_endpoints()
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
    def __init__(self, author: "Author", title: str):
        self._author = author
        self._title = title

    def __str__(self):
        """
        Returns title of the poem.
        """
        return self._title

    @property
    def author(self):
        """
        Returns Author (object) of the poems.
        """
        return self._author

    @property
    def title(self):
        """
        Returns title of the poem.
        """
        return self._title

    def text(self) -> str:
        """
        Retrives text of a poem from database and returns it.

        Returns:
            text (str): Text of the poem.
        """
        urls = get_poem_endpoints()
        author = self._author.name
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
