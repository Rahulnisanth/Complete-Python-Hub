import re

ITALICS = re.compile(r'<em>(.+?)</em>')
SPACES = re.compile(r'\s+')
PARAGRAPHS = re.compile(r'<p>(.+?)</p>')
URLS = re.compile(r'<a href="(.+?)">(.+?)</a>')

def html2markdown(html):
    markdown = ITALICS.sub(r'*\1*', html)
    markdown = SPACES.sub(r' ', markdown)
    markdown = PARAGRAPHS.sub(r'\1\n\n', markdown)
    markdown = URLS.sub(r'[\2](\1)', markdown)
    return markdown.strip()
