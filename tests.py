from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
# pytest -v tests.py
class TestBooksCollector:
    def test_add_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        assert collector.books_rating == {'Горе от ума': 1}

    def test_add_book_same_book_two_times_false(self):
        collector = BooksCollector()
        collector.add_new_book('Крёстный отец')
        collector.add_new_book('Крёстный отец')
        assert collector.books_rating == {'Крёстный отец': 1}

    def test_set_book_rating_less_than_one_false(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин Колец')
        collector.set_book_rating('Властелин Колец', 0)
        assert collector.books_rating == {'Властелин Колец': 1}

    def test_set_book_rating_more_than_ten_false(self):
        collector = BooksCollector()
        collector.add_new_book('На западном фронте без перемен')
        collector.set_book_rating('На западном фронте без перемен', 11)
        assert collector.books_rating == {'На западном фронте без перемен': 1}

    def test_get_books_rating_true(self):
        collector = BooksCollector()
        assert collector.books_rating == {}

    def test_get_book_rating_not_in_list_false(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Капитанская дочка') == None









