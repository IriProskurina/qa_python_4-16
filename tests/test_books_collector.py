import unittest
from src.main import BooksCollector


class TestBooksCollector(unittest.TestCase):

    def test_example(self):
        collector = BooksCollector()
        self.assertIsNotNone(collector)

if __name__ == '__main__':
    unittest.main()


    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()


        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')


        assert len(collector.get_books_rating()) == 2

