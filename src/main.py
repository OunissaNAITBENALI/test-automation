from src.services.book_fetcher_service import BookFetcherService
from src.services.book_service import BookService

user_fetcher_service = UserFetcherService()
user_service = UserService(book_fetcher_service=book_fetcher_service)

print('users ids : ' +  ', '.join(book_service.list_users_ids()))
print('users email : ' +  ', '.join(book_service.list_users_email()))


"""user_fetcher_service = UserFetcherService()
user_service = UserService(user_fetcher_service=UserFetcherService())
users = user_service.list_users()

for user in users:
    print(f'User email : {user['email']}(id: {user['id']}')"""
