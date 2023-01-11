from song import Song


def test_create_song():
    song = Song('Lose yourself', 'Eminem')
    assert song.title == 'Lose yourself'
    assert song.artist == 'Eminem'
    assert len(song.lyrics) == 90


def test_create_empty_song():
    song = Song()
    assert song.title == ''
    assert song.artist == ''
