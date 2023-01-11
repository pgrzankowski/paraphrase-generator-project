from poem import Author


def test_create_author():
    author = Author('Gombrowicz')
    assert author.name() == 'Gombrowicz'


def test_author_titles():
    author = Author('Emily Dickinson')
    titles = author.titles()
    title_1 = titles[0]
    assert str(title_1) == 'Not at Home to Callers'
