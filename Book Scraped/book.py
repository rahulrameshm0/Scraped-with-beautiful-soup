from bs4 import BeautifulSoup
import requests
books = requests.get('https://books.toscrape.com/')

soupe = BeautifulSoup(books.text, 'lxml')

jobs = soupe.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

for index, job in enumerate(jobs):
    book_name = job.article.h3.a['title']
    book_info = job.article.h3.a['href'] 
    book_amount = job.find('p', class_ = 'price_color').text
    with open(f'Book Details/{index}', 'w') as f:
        f.write(f"BOOK NAME: {book_name}\n")
        f.write(f"BOOK INFO: {book_info}\n")
        f.write(f"BOOK AMOUNT: {book_amount}\n")
    print("File has been saved successfully")