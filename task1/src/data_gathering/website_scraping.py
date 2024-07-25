import requests
from bs4 import BeautifulSoup
import os

def extract_text_from_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = " ".join([para.get_text() for para in paragraphs])
    return text

if __name__ == "__main__":
    website_url = "https://www.apple.com/apple-vision-pro/"  # URL to scrape
    website_text = extract_text_from_website(website_url)

    # Ensure directory exists
    output_dir = "task1/data/websites"
    os.makedirs(output_dir, exist_ok=True)

    # Save the text to a file with UTF-8 encoding
    output_file = os.path.join(output_dir, "website_text.txt")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(website_text)
