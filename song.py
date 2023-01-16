import json
from lyricsgenius import Genius
from errors import TitleError


def setup_genius():
    """
    This method sets genius object atrributes to
    properly retrive data and returns it.
    """
    with open('genius_authorization.json', 'r') as file:
        genius_data = json.load(file)
    genius = Genius(genius_data["access_token"])
    exclude = [
        'track?list',
        'album art(work)?',
        'liner notes',
        'booklet',
        'credits',
        'inteview',
        'skit',
        'instrumental',
        'setlist',
        'album',
        'genius'
    ]
    genius.excluded_terms = exclude
    genius.verbose = False
    genius.remove_section_headers = True
    return genius


def get_song(title, artist=''):
    """
    This method creates Song object based on title
    and artist parameters and returns it.
    """
    if title:
        genius = setup_genius()
        song_data = genius.search_song(title, artist)
        proper_title = song_data.title
        proper_artist = song_data.artist
        lyrics = song_data.lyrics
        start_pos = lyrics.find(proper_title) + len(proper_title) + 8
        end_pos = lyrics.find('You might also like')
        lyrics = lyrics[start_pos:end_pos]
        return Song(proper_title, proper_artist, lyrics)
    else:
        raise TitleError()


class Song:
    """
    Class which allows to store songs.

    :param title: title of the song
    :type title: str

    :param artist: name of the artist
    :type artist: str

    :param lyrics: lyrics of the song
    :type lyrics: str
    """
    def __init__(self, title, artist='', lyrics=''):
        self._title = title
        self._artist = artist
        self._lyrics = lyrics

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    @property
    def lyrics(self):
        return self._lyrics
