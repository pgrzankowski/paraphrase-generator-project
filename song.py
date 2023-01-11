import json
from lyricsgenius import Genius


with open('genius_authorization.json', 'r') as file:
    genius_data = json.load(file)
genius = Genius(genius_data["access_token"])

# Turn off status messages
genius.verbose = False
# Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.remove_section_headers = True

# Exclude hits thought to be non-songs (e.g. track lists)
genius.skip_non_songs = True


class Song:
    def __init__(self, title='', artist=''):
        self._title = title
        self._artist = artist

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    @property
    def lyrics(self):
        try:
            lyrics = genius.search_song(
                title=self._title,
                artist=self._artist
                ).lyrics
            # return lyrics.split('\n')[1:]
            return lyrics
        except AttributeError:
            return 'Lyrics not found'
