
class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.all_books.append(self)

    @classmethod
    def all(cls):
        return cls.all_books

    def contracts(self):
        return [contract for contract in Contract.all() if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.all_authors.append(self)
        self._contracts = []

    @classmethod
    def all(cls):
        return cls.all_authors

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
