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

  
  # Extract and print all images
    print("\nImages:")
    images = soup.find_all('img', src=True)
    for idx, img in enumerate(images):
        src = img['src']
        alt_text = img.get('alt', 'No alt text')
        print(f"{idx + 1}: {alt_text} - {src}")
