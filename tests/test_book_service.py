from src.services.book_fetcher_service import BookFetcherService
from src.services.book_service import BookService
import pytest


def test_list_book_ids(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    ids = book_service.list_books_ids()

    assert ids == ['aaa-001', 'aaa-002']



def test_list_authors(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)
    book_service = BookService(book_fetcher_service=BookFetcherService())
    authors = book_service.list_books_authors()


   # assert collection.Counter(authors) == collections.Counter(['Brown Dan', 'Boy Danny'])c'est juste une autre façon de faire des collectiones ( tableaux, objets;;;)
   #vérifier une égalité de tableau non ordonné
    assert authors == ['Brown Dan']



def test_list_books_ids_no_books(monkeypatch):
    # arrange
    def mock_get_no_books(*args):
        return []
    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_no_books)
    book_service = BookService(book_fetcher_service=BookFetcherService())

    # act
    authors = book_service.list_books_authors()

    #assert
    assert authors == []

def test_list_books_authors_same_name(monkeypatch):
    def mock_get_list_books_authors_same_name(*args):
          return [
            {'id': 1, 'author': {'firstname': 'Brown', 'lastname': 'Dan'}},
            {'id': 2, 'author': {'firstname': 'Brown', 'lastname': 'Dan'}},
           ]


def test_list_books_authors_no_lastname(monkeypatch):
    def mock_get_list_books_authors_no_lastname(*args):
        return [{'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        ]
    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_list_books_authors_no_lastname)
    book_service = BookService(book_fetcher_service=BookFetcherService())
    authors = book_service.list_books_authors()

    assert authors == ['Brown Dan']

    #assert collection.Counter(authors) == collections.Counter(['Brown Dan', 'Boy Danny'])





     #books = self.book_fetcher_service.get_books()










