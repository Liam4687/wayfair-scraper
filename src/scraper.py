thonimport requests
from bs4 import BeautifulSoup
import json

class WayfairScraper:
    def __init__(self, url):
        self.url = url
        self.product_data = []

    def fetch_page(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch page: {self.url}")

    def extract_data(self, page_content):
        soup = BeautifulSoup(page_content, 'html.parser')
        products = soup.find_all('div', class_='product-card')
        for product in products:
            data = {
                'sku': product.get('data-sku'),
                'name': product.find('h2').text.strip(),
                'price': product.find('span', class_='price').text.strip(),
                'manufacturer': product.find('span', class_='manufacturer').text.strip(),
                'rating': product.find('span', class_='rating').text.strip(),
                'reviews': product.find('span', class_='reviews').text.strip(),
                'productUrl': product.find('a')['href'],
                'features': self.extract_features(product)
            }
            self.product_data.append(data)

    def extract_features(self, product):
        features = []
        feature_list = product.find_all('li', class_='feature')
        for feature in feature_list:
            features.append(feature.text.strip())
        return features

    def save_data(self, filename='product_data.json'):
        with open(filename, 'w') as f:
            json.dump(self.product_data, f, indent=4)

    def run(self):
        page_content = self.fetch_page()
        self.extract_data(page_content)
        self.save_data()

if __name__ == "__main__":
    url = 'https://www.wayfair.com/furniture'
    scraper = WayfairScraper(url)
    scraper.run()