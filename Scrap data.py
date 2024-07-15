import requests
from bs4 import BeautifulSoup


# URL of the web page you want to scrape
url = 'https://example.com'


# Send a GET request to the web page
response = requests.get(url)


# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
  
    
    # Example: Get the title of the page
    title = soup.find('title').get_text()
    print(f"Title: {title}")
    
    # Example: Get all paragraphs and print their text
    paragraphs = soup.find_all('p')
    for idx, paragraph in enumerate(paragraphs):
        print(f"Paragraph {idx + 1}: {paragraph.get_text()}")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
