import pytest


class TestBooksCollector:

    def test_add_new_book_true(self, collector):
        collector.add_new_book('Горе от ума')
        assert collector.books_rating == {'Горе от ума': 1}

    def test_add_book_same_book_two_times_false(self, collector):
        collector.add_new_book('Крёстный отец')
        collector.add_new_book('Крёстный отец')
        assert collector.books_rating == {'Крёстный отец': 1}

    def test_set_book_rating_not_in_list_false(self, collector):
        collector.set_book_rating('Лолита', 9)
        assert collector.books_rating == {}

    def test_set_book_rating_less_than_one_false(self, collector):
        collector.add_new_book('Властелин Колец')
        collector.set_book_rating('Властелин Колец', 0)
        assert collector.books_rating == {'Властелин Колец': 1}

    def test_set_book_rating_more_than_ten_false(self, collector):
        collector.add_new_book('На западном фронте без перемен')
        collector.set_book_rating('На западном фронте без перемен', 11)
        assert collector.books_rating == {'На западном фронте без перемен': 1}

    def test_get_books_with_specific_rating_true(self, collector):
        collector.add_new_book('Хоббит')
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Парфюмер')
        collector.set_book_rating('Хоббит', 10)
        collector.set_book_rating('Властелин колец', 10)
        collector.set_book_rating('Парфюмер', 1)
        assert collector.get_books_with_specific_rating(10) == ['Хоббит','Властелин колец']

    @pytest.mark.parametrize("book_title",['Капитанская дочка','Евгений Онегин'])
    def test_get_book_rating_not_in_list_false(self, collector, book_title):
        assert collector.get_book_rating(book_title) == None

    def test_add_book_in_favorites_true(self, collector):
        collector.add_new_book('Портрет Дориана Грея')
        collector.add_book_in_favorites('Портрет Дориана Грея')
        assert collector.favorites == ['Портрет Дориана Грея']

    @pytest.mark.parametrize("book_title", ['Вечера на хуторе вблизь диканьки', 'Ревизор', 'Мертвые души'])
    def test_book_not_in_list_add_in_favorites_false(self, collector, book_title):
        collector.add_book_in_favorites(book_title)
        assert collector.favorites == []

    def test_delete_book_from_favorites_true(self, collector):
        collector.add_new_book('Моби Дик')
        collector.add_new_book('Ведьмак')
        collector.add_book_in_favorites('Моби Дик')
        collector.add_book_in_favorites('Ведьмак')
        collector.delete_book_from_favorites('Моби Дик')
        assert collector.favorites == ['Ведьмак']

    def test_get_book_rating_by_name_true(self, collector):
        collector.add_new_book('Мемуары гейши')
        collector.set_book_rating('Мемуары гейши', 6)
        collector.add_new_book('Ведьмак')
        assert collector.get_book_rating('Мемуары гейши') == 6

    def test_get_books_rating_true(self, collector):
        collector.add_new_book('Великий Гэтсби')
        collector.add_new_book('Граф Монте-Кристо')
        collector.set_book_rating('Граф Монте-Кристо', 8)
        assert collector.get_books_rating() == {'Великий Гэтсби': 1, 'Граф Монте-Кристо': 8}

