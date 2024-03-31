# Import necessary libraries for web scraping
import pprint  # Import the pretty printer module for neat output
import requests  # Import the requests library for making HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML content

# Send an HTTP GET request to the specified URL and store the response
response = requests.get("https://news.ycombinator.com/news")

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Select all the HTML elements with class 'titleline' followed by 'a' tag
links = soup.select('.titleline > a')

# Select all the HTML elements with class 'subtext'
sub_text = soup.select('.subtext')

# Define a function to sort a list of dictionaries based on the 'score' key in reverse order
def sort_list(h_list) -> list:
    return sorted(h_list, key=lambda x: x['score'], reverse=True)

# Define a function to extract and filter Hacker News articles with a score greater than 99
def custom_news(links, sub_text):
    hacker_news = []
    for inx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = sub_text[inx].select('.score')
        if len(vote):
            score = int(vote[0].getText().replace(' points', ''))
            if score > 99:
                hacker_news.append({'title': title, 'link': href, 'score': score})
    return sort_list(hacker_news)

# Pretty print the sorted list of Hacker News articles
pprint.pprint(custom_news(links, sub_text))
