import requests

urls = {
    'authors': 'https://poetrydb.org/author',
    'titles': 'https://poetrydb.org/author/{author}/title',
    'poem': 'https://poetrydb.org/author,title/{author};{title}'
}


def get_authors():
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

    def name(self):
        """
        Returns name of the author.
        """
        return self._name

    def poems(self):
        """
        Returns list of poem objects.
        """
        all_titles = requests.get(urls['titles'].format(author=self._name))
        all_poems = []
        for title_item in all_titles.json():
            title = title_item['title']
            text_item = requests.get(
                urls['poem'].format(
                    author=self._name,
                    title=title
                    )
                ).json()
            text = text_item[0]['lines']
            poem = Poem(text, title, self)
            all_poems.append(poem)
        return all_poems


class Poem:
    """
    A class used to represent a Poem.

    :param text: text of the poem (in seperate lines)
    :type text: list

    :param title: title of the poem
    :type title: str

    :param author: author of the poem
    :type author: Author
    """
    def __init__(self, text, title, author):
        self._text = text
        self._title = title
        self._author = author

    def text(self):
        return self._text

    def title(self):
        return self._title

    def author(self):
        return self._author
