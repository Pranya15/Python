class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_publisher(self):
        return self._publisher

    def set_publisher(self, publisher):
        self._publisher = publisher

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    
    def royalty(self, copies_sold):
        if copies_sold <= 500:
            return copies_sold * self._price * 0.10

        elif copies_sold <= 1500:
            return (500 * self._price * 0.10) + \
                   ((copies_sold - 500) * self._price * 0.125)

        else:
            return (500 * self._price * 0.10) + \
                   (1000 * self._price * 0.125) + \
                   ((copies_sold - 1500) * self._price * 0.15)


class Ebook(Book):
    def __init__(self, title, author, publisher, price, format):
        super().__init__(title, author, publisher, price)
        self._format = format

    def get_format(self):
        return self._format

    def set_format(self, format):
        self._format = format

    # Override royalty method (deduct 12% GST)
    def royalty(self, copies_sold):
        base_royalty = super().royalty(copies_sold)
        return base_royalty * 0.88   # after 12% GST deduction


# Example usage
book1 = Book("Python Basics", "Pranya", "XYZ Publisher", 500)
print("Book Royalty:", book1.royalty(2000))

ebook1 = Ebook("Python Basics", "Pranya", "XYZ Publisher", 500, "PDF")
print("Ebook Royalty (after GST):", ebook1.royalty(2000))