from paraphrase_generator.song import Song, get_song
from paraphrase_generator.my_errors import TitleError
import pytest


def test_create_song():
    song = Song('Lose yourself', 'Eminem', 'test lyrics')
    assert song.title == 'Lose yourself'
    assert song.artist == 'Eminem'
    assert song.lyrics == 'test lyrics'


def test_create_song_title_only():
    song = Song('Lose yourself')
    assert song.title == 'Lose yourself'
    assert song.artist == ''
    assert song.lyrics == ''


def test_get_song():
    song = get_song('lose yourself', 'eminem')
    assert song.title == 'Lose Yourself'
    assert song.artist == 'Eminem'
    assert song.lyrics != ''


def test_get_song_no_artist():
    song = get_song('lose yourself')
    assert song.title == 'Lose Yourself'
    assert song.artist == 'Eminem'
    assert song.lyrics != ''


def test_get_song_no_title():
    with pytest.raises(TypeError):
        get_song()


def test_get_song_blank_title():
    with pytest.raises(TitleError):
        get_song('')
