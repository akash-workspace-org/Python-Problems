class library:

    def __init__(self,title,auther,avalaible):
        self.title = title
        self.auther = auther
        self.avalaible = avalaible


    def diplay_book(self):
        print('Book:',self.title)
        print('Auther: ',self.auther)
        print('Status: ',self.avalaible)

    def borrow_book(self):
        if self.avalaible == True:
            self.avalaible = False
            return 'Book is avalaible: '
        elif self.avalaible == False:
            return 'Not avalaible: '

    def return_book(self):
        if self.avalaible == False:
            self.avalaible = True
            return 'Book retured: '
        elif self.avalaible == True:
            return 'Book already avalaible: '

obj = library('rich dad','maxan',True)
obj.diplay_book()
print(obj.borrow_book())
print(obj.return_book())