
class NewObj:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5]

    # چون __iter__ رو براش تعریف کریدم این یک iterable تبدیل شد
    def __iter__(self):
        for i in self.items:
            yield i