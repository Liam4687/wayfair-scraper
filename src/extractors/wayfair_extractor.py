thonimport json

class WayfairExtractor:
    @staticmethod
    def extract_product_info(product):
        return {
            'sku': product['sku'],
            'name': product['name'],
            'price': product['price'],
            'manufacturer': product['manufacturer'],
            'rating': product['rating'],
            'reviews': product['reviews'],
            'productUrl': product['productUrl'],
            'features': product['features']
        }

    @staticmethod
    def extract_from_file(filename='product_data.json'):
        with open(filename, 'r') as file:
            product_data = json.load(file)
        return [WayfairExtractor.extract_product_info(product) for product in product_data]