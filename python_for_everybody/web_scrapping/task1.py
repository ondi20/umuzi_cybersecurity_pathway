import urllib.request
from bs4 import BeautifulSoup

# Prompt for URL
url = input("Enter URL: ")

# Open and parse the HTML
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')

# Sum the numbers
count = 0
total = 0
for tag in tags:
    try:
        number = int(tag.text)
        total += number
        count += 1
    except:
        continue

print("Count", count)
print("Sum", total)
