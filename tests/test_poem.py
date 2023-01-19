from paraphrase_generator.poem import Author, Poem, get_authors


def test_create_author():
    author = Author('Gombrowicz')
    assert author.name == 'Gombrowicz'


def test_create_poem():
    author = Author('Emily Dickinson')
    poem = Poem(author, 'Not at Home to Callers')
    assert poem.author.name == 'Emily Dickinson'
    assert poem.title == 'Not at Home to Callers'


def test_author_titles():
    author = Author('Emily Dickinson')
    titles = author.poems()
    title_1 = titles[0]
    assert str(title_1) == 'Not at Home to Callers'


def test_get_authors():
    authors = get_authors()
    assert authors[0].name == 'Adam Lindsay Gordon'


def test_poem_text():
    author = get_authors()[0]
    assert author.name == 'Adam Lindsay Gordon'
    poem = author.poems()[0]
    assert poem.title == 'A Song of Autumn'
    assert poem.author.name == 'Adam Lindsay Gordon'
    text = poem.text
    assert text != ''
