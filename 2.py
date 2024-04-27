import requests


def get_book_info(book_title, author):
    url = f'https://www.googleapis.com/books/v1/volumes?q=intitle:{book_title}+inauthor:{author}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Bir hata oluştu")

get_book_info('harry potter', 'jk rowling')