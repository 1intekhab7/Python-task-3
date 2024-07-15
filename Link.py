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
  
  # Extract and print all links
    print("\nLinks:")
    links = soup.find_all('a', href=True)
    for idx, link in enumerate(links):
        href = link['href']
        link_text = link.get_text()
        print(f"{idx + 1}: {link_text} - {href}"
