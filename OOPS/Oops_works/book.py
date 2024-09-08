class book():
    title:str
    author:str
    price:int
    language:str
# instance variable initialize
    def __init__(self,title,author,price,language):
        self.title=title
        self.author=author
        self.price=price
        self.language=language

    def display_book(self):
        print(self.title,self.author,self.price,self.language)

        # sring represenation
    def __str__(self):
        return self.title

            # create instance
book_instance=book("goat life","benyamin",678,"english")

book_instance.display_book()


print(book_instance)
