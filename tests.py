from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_default_value_rating_true(self):
        collector = BooksCollector()
        collector.add_new_book('Продается планета')
        assert collector.get_book_rating('Продается планета') == 1

    def test_add_new_book_add_the_same_book_twice_error(self):
        collector = BooksCollector()
        collector.add_new_book('Продается планета')
        collector.add_new_book('Унесенные ветром')
        collector.add_new_book('Продается планета')
        assert len(collector.get_books_rating()) == 2

    def test_set_book_rating_set_rating_nine_true(self):
        collector = BooksCollector()
        collector.add_new_book('Продается планета')
        collector.set_book_rating('Продается планета', 9)
        assert collector.get_book_rating('Продается планета') == 9

    def test_set_book_rating_set_rating_less_than_one_error(self):
        collector = BooksCollector()
        collector.add_new_book('Продается планета')
        collector.set_book_rating('Продается планета', 0)
        assert collector.get_book_rating('Продается планета') == 1

    def test_set_book_rating_set_rating_more_than_ten_error(self):
        collector = BooksCollector()
        collector.add_new_book('Продается планета')
        collector.set_book_rating('Продается планета', 12)
        assert collector.get_book_rating('Продается планета') == 1

    def test_set_book_rating_set_rating_a_book_that_is_not_on_the_list_error(self):
        collector = BooksCollector()
        collector.set_book_rating('Продается планета', 9)
        assert collector.get_book_rating('Продается планета') == 9, 'Нельзя установить рейтинг книге, которой нет в списке'

    def test_add_book_in_favorites_add_one_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Продается планета')
        collector.add_new_book('Унесенные ветром')
        collector.add_book_in_favorites('Унесенные ветром')
        assert collector.get_list_of_favorites_books() == ['Унесенные ветром']

    def test_delete_book_from_favorites_delete_one_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Продается планета')
        collector.add_new_book('Унесенные ветром')
        collector.add_book_in_favorites('Унесенные ветром')
        collector.delete_book_from_favorites('Унесенные ветром')
        assert collector.get_list_of_favorites_books() == []

    def test_get_books_with_specific_rating_get_books_with_nine_rating_true(self):
        collector = BooksCollector()
        collector.add_new_book('Продается планета')
        collector.add_new_book('Унесенные ветром')
        collector.set_book_rating('Продается планета', 9)
        assert collector.get_books_with_specific_rating(9) == ['Продается планета']

    def test_get_books_rating_get_books_rating_two_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Продается планета')
        collector.set_book_rating('Продается планета', 9)
        collector.add_new_book('Унесенные ветром')
        collector.set_book_rating('Унесенные ветром', 8)
        assert collector.get_books_rating() == {'Продается планета': 9, 'Унесенные ветром': 8}


