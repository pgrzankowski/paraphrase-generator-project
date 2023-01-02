class Text:
    """
    A class used to represent text inputs such as:
    - song lyrics,
    - poems,

    :param lines: list of lines (strings) of text
    :type lines: list

    :param title: title of the text, default to None
    :type title: str

    :param author: author of the text, default to None
    :type author: str
    """
    def __init__(self, lines, title=None, author=None):
        self._lines = lines
        self.title = title
        self.author = author

    def lines(self):
        """
        Returns list of lines in text.
        """
        return self._lines
