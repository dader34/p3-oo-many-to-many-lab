class Author:
    def __init__(self,name):
        self._name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if(type(name) == str):
            self._name = name

class Book:
    def __init__(self,title):
        self._title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]
    

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if(type(title) == str):
            self._title = title

class Contract:

    all = []

    def __init__(self,author,book,date,royalties):
        self.author,self.book,self.date,self.royalties = author,book,date,royalties

        self.all.append(self)

    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):
        if(isinstance(author,Author)):
            self._author = author
        else:
            raise Exception("You cant do that")

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self,book):
        if(isinstance(book,Book)):
            self._book = book
        else:
            raise Exception

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,date):
        if(type(date) == str):
            self._date = date
        else:
            raise Exception

    @property
    def royalties(self):
        return self._royalties
        
    @royalties.setter
    def royalties(self,royalties):
        if(type(royalties) == int):
            self._royalties = royalties
        else:
            raise Exception


