import json
from lyricsgenius import Genius
from dotenv import load_dotenv
import os

load_dotenv()
GENIUS_TOKEN = os.getenv("GENIUS_TOKEN")


def setup_genius() -> "Genius":
    """
    This method creates a Genius object and sets its
    atrributes to properly retrive data and returns it.
    It is done to access Genius API.

    Returns:
        genius (Genius object): Properly set up Genius object
                                which allows for precise song
                                searching.
    """
    genius = Genius(GENIUS_TOKEN)
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
    # excludes given terms from search results
    genius.excluded_terms = exclude
    genius.verbose = False
    genius.remove_section_headers = True
    return genius


def get_song(title: str, artist='') -> "Song":
    """
    This method creates Song object based on title
    and artist parameters and returns it.

    Parameters:
        title (str): Title of the searched song.
        artist (str): Artist of the searched song.

    Returns:
        song (Song object): Song found in database based
                            on given title and artist.
    """
    if title:
        genius = setup_genius()
        song_data = genius.search_song(title, artist)
        proper_title = song_data.title
        proper_artist = song_data.artist
        lyrics = song_data.lyrics
        return Song(proper_title, proper_artist, lyrics)
    else:
        raise Exception()


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
    def __init__(self, title: str, artist='', lyrics=''):
        self._title = title
        self._artist = artist
        self._lyrics = lyrics

    @property
    def title(self):
        """
        Returns title of the song.
        """
        return self._title

    @property
    def artist(self):
        """
        Returns artist of the song.
        """
        return self._artist

    @property
    def lyrics(self):
        """
        Returns lyrics of the song.
        """
        return self._lyrics
