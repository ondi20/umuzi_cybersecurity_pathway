##  Task 1: Scraping Numbers from HTML

```markdown
#  Scraping Numbers from HTML

This Python script retrieves an HTML page from a URL, extracts all numeric values from `<span class="comments">` tags, and calculates their sum.

##  Objective

Given a webpage with a table of names and comment counts like:

```html
<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
```

...the goal is to:

1. Retrieve the HTML content from a user-provided URL.
2. Parse all `<span>` tags with class `"comments"`.
3. Extract the numeric content.
4. Compute the total count and sum of these numbers.

##  Tools Used

- Python 3
- [`urllib`](https://docs.python.org/3/library/urllib.html) — to fetch data from a web page
- [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/) — to parse and navigate HTML

##  How to Run

1. Install BeautifulSoup (if not already installed):

```bash
pip install beautifulsoup4
```

2. Run the script:

```bash
python3 scrape_sum.py
```

3. Enter the URL when prompted. Example:

```
Enter URL: http://py4e-data.dr-chuck.net/comments_42.html
```

##  Sample Output

```
Enter URL: http://py4e-data.dr-chuck.net/comments_42.html
Count 50
Sum 2553
```

##  Notes

- Your actual assignment will have a different URL.
- Make sure the URL is correct and public.

##  Related Learning

This exercise is adapted from the [Python for Everybody](https://www.py4e.com) course by Dr. Chuck.
```

---

##  Task 2: Following Links in HTML

```markdown
#  Following Links in HTML

This Python script repeatedly navigates through a series of hyperlinks found in HTML anchor tags, following the link at a specific position for a specified number of times, and prints the final name encountered.

##  Objective

Given an initial URL, follow a link at a **specific position** in the HTML multiple times.

Example:

- Start URL: `http://py4e-data.dr-chuck.net/known_by_Fikret.html`
- Count: `4`
- Position: `3`

Follow the 3rd link 4 times. Output:

```
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
Last name in sequence: Anayah
```

##  Tools Used

- Python 3
- [`urllib`](https://docs.python.org/3/library/urllib.html) — to fetch HTML content
- [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/) — to parse HTML and extract anchor tags

##  How to Run

1. Install BeautifulSoup (if not already installed):

```bash
pip install beautifulsoup4
```

2. Run the script:

```bash
python3 follow_links.py
```

3. Provide the required inputs when prompted:

```
Enter URL: http://py4e-data.dr-chuck.net/known_by_Kalvin.html
Enter count: 7
Enter position: 18
```

##  Notes

- Position is 1-based (the first link is at position 1).
- Ensure the page contains enough anchor tags or the program may error out.
- The last name is usually found in the title tag of the final page.

##  Related Learning

This task is part of the [Python for Everybody](https://www.py4e.com) series, designed to teach web scraping and navigation through hyperlinks using Python.