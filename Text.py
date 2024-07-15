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
    
    # Extract and print the text of the page
  
    text = soup.find('text').get_text()
    print(f"Text: {text}")
