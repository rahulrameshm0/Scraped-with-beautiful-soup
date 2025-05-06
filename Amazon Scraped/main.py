import requests
from bs4 import BeautifulSoup
import csv
url = 'https://www.amazon.in/s?k=lg+monitor&crid=2PP7EK1VCA56P&sprefix=lg+monito%2Caps%2C428&ref=nb_sb_noss_2'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response= requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

products = soup.find_all('div', class_='a-section a-spacing-small a-spacing-top-small')  

with open('products.csv', 'w', newline='', encoding='utf-8') as file:
    wrtier = csv.writer(file)
    wrtier.writerow(['Title', 'Price', 'Title Link', 'Review Link', 'Total Review'])

    for product in products:
        title = product.find('h2', class_='a-size-medium a-spacing-none a-color-base a-text-normal').text
        review_count = product.find('span', class_='a-size-base s-underline-text').text
        amount = product.find('span', class_ = 'a-offscreen').text
        review_link = product.a['href'].strip()
        title_link = product.div.a['href'].strip()
        wrtier.writerow([title, amount, 'https://www.amazon.com' + title_link,'https://www.amazon.com' + review_link, review_count])
        
        # file.write(f"{title}")
        # file.write(f"{amount}")
        # file.write(f"https://www.amazon.com" + title_link)
        # file.write(f"https://www.amazon.com" + review_link)
        # file.write(f"{review_count}\n")

print('File Saved Succesfully')