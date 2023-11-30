from src.services.user_fetcher_service import UserFetcherService
from src.services.user_service import UserService
import pytest


def test_list_user_multiple_users(monkeypatch):

    def mock_get_users(*args):
        return [{
            'id': 1,
            'email': 'lolo@gmail.com'


        }
        )]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    ids = book_service.list_books_ids()

    assert ids == ['aaa-001', 'aaa-002']













"""import pytest
from services.user_fetcher_service import UserFetcherService
#from services.string_service import to_lowercase

"""
"""def test_list_users_service(monkeypatch):
    def mock_get_users(*args):
        """ 
"""
        return [
            #{'user email': {user['email']}(id: {user['id']}')}
            {'id': 'aaa-001', 'email': 'user'},
            {'id': 'aaa-002', 'email': 'user'},
            {'id': 'aaa-003', 'email': 'user'}
        ] 
          
        monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_users)

        user_fetcher_service = UserFetcherService()
        user_service = UserService(user_fetcher_service=UserFetcherService())
        users = user_service.list_users()

        for user in users:
            print(f'User email : {user['email']}(id: {user['id']}')

            #print('ids : ' + ', '.join(book_service.list_books_ids())),
            #print('email: ' + ', '.join(user_service.list_users()))

        #assert users == ['aaa-001', 'aaa-002']

"""