import urllib.request
from bs4 import BeautifulSoup

# User input
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: ")) - 1  # Convert to 0-based index

for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <a> tags
    tags = soup('a')
    if len(tags) <= position:
        print("Not enough links on the page.")
        break

    # Move to the next URL
    url = tags[position].get('href')

# Final page will have the name
print("Retrieving:", url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print("Last name in sequence:", soup.title.string.split()[-1])
