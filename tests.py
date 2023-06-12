from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    def test_add_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        assert collector.books_rating == {'Горе от ума': 1}



