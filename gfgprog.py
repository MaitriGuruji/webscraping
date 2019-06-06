import requests
#import bs4
import html5lib
from bs4 import BeautifulSoup
import csv
import urllib.parse

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
# with open('data.html','w') as f:
#     f.write(str(r.content))
#print(r.content)
soup = BeautifulSoup(r.content, 'html5lib')
#print(soup)
#print("***********************************************************************************************")
#print(soup.prettify())
quotes = []  # a list to store quotes
table = soup.find('div', attrs={'class': 'container clearfix'})
#print(table)
for row in soup.find_all('div', attrs={'class':'portfolio-image'}):
    #print(row)
    quote = {}
    # quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['desc'] = row.img['alt']
#     quote['lines'] = row.h6.text
#     quote['author'] = row.p.text
    quotes.append(quote)
print(quotes)
filename = 'inspirational_quotes.csv'
with open(filename, 'w') as f:
    w = csv.DictWriter(f, ['url', 'img', 'desc'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
f.close()

# with open('inspirational_quotes.csv', newline='') as csvfile:
#      spamreader = csv.reader(csvfile)
#      for row in spamreader:
#          print(row)



