from song import Song


def test_create_song():
    song = Song('Lose yourself', 'Eminem')
    assert song.title == 'Lose yourself'
    assert song.artist == 'Eminem'
