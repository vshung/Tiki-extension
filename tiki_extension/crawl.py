import requests
from bs4 import BeautifulSoup
from manage import Product, Price


class Crawler:
    def __init__(self):
        self.base_url = 'https://tiki.vn/laptop-may-vi-tinh-linh-kien/c1846?src=mega-menu&page={}'

    def run(self):
        page = 1
        flag = True
        while flag:
            print(page)
            url = self.base_url.format(page)
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'lxml')
                products_container = soup.find('div', {'class': 'product-box-list'})
                if not products_container:
                    flag = False
                page = page + 1
                products = self.get_all_products(products_container)

                for product in products:
                    product_detail = self.get_product_detail(product)
                    product = Product.query.filter_by(id=product_detail['id']).first()
                    if not product:
                        product = Product(id=product_detail['id'],
                                          product_name=product_detail['name']
                                          )
                        product.save()
                        price = Price(price=product_detail['price'], product_id=product.id)
                        price.save()
                    else:
                        price = Price(price=product_detail['price'], product_id=product.id)
                        price.save()
            except:
                pass

    def get_all_products(self, soup):
        products = soup.find_all('div', recursive=False)
        return products

    def get_product_detail(self, soup):
        attrs = soup.attrs
        product_id = attrs['data-id']
        product_name = attrs['data-title']
        product_price = attrs['data-price']
        return {
            'id': product_id,
            'name': product_name,
            'price': float(product_price)
        }


if __name__ == '__main__':
    Crawler().run()
