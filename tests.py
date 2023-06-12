from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    def test_add_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        assert collector.books_rating == {'Горе от ума': 1}

    def test_set_book_rating_less_than_one_false(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин Колец')
        collector.set_book_rating('Властелин Колец', 0)
        assert collector.books_rating == {'Властелин Колец': 1}






