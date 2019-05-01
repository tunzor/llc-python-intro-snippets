# Import requests and BeautifulSoup libraries
# requests to make a call to get a webpage
# BeautifulSoup for getting the data out of the HTML document
import requests
from bs4 import BeautifulSoup

# The page we want to get; it's the about us page that shows the team
pageUrl = 'https://www.canadalearningcode.ca/our-team/'

# Gets the HTML page and turns it into a variable BeautifulSoup can work with
page = requests.get(pageUrl)
soup = BeautifulSoup(page.text, 'html.parser')

# Find all the names and titles for the team
names = soup.find_all('h5', class_='personVerticalCard-name')
titles = soup.find_all('span', class_='personVerticalCard-title')

# Iterate over all of names and titles and print it to the command line
# Format: NAME - TITLE
for name, title in zip(names, titles):
    print(name.contents[0] + ' - ' + title.contents[0])
