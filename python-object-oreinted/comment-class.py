from datetime import datetime


class Product:
    def __init__(self, product_name: str, price: int, off: int):
        self.product_name = product_name
        self.price = price
        self.off = off

    def __str__(self):
        return self.product_name


class Comment:
    website_name = 'website khobye'

    def __init__(self, product: ['Product'], name: str, description: str, like: int, dislike: str):
        self.product = product
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.like = like
        self.dislike = dislike

    def show(self):
        print(f'Product: {self.product}\n'
              f'name: {self.name}\n'
              f'description: {self.description}\n'
              f'date: {self.date}\n'
              f'like: {self.like} and dislike: {self.dislike}')

    @classmethod
    def info(cls):
        print(f'website name: {cls.website_name}')

    @classmethod
    def censorship(cls, product, name, description, like, dislike):
        print('the comment was censorship!!')
        cs = description.replace('بیشعور', '****')
        return cls(product, name, cs, like, dislike)

    @staticmethod
    def elapsed_time(time):
        print(datetime.now() - time)