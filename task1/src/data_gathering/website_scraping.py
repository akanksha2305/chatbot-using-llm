import requests
from bs4 import BeautifulSoup

def extract_text_from_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = " ".join([para.get_text() for para in paragraphs])
    return text

if __name__ == "__main__":
    website_url = "https://www.apple.com/apple-vision-pro/"  # Replace with actual URL
    website_text = extract_text_from_website(website_url)
    with open("task1/data/websites/website_text.txt", "w", encoding="utf-8") as file:
        file.write(website_text)
