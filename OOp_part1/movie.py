class movie:

    def __init__(self,title,category,rating):
        self.title = title
        self.category = category
        self.rating = rating

    def add_rating(self):
        rat = int(input('Enter rating: '))
        self.rating.append(rat)

    def cal_avg(self):
        total = 0
        count = 0
        avg = 0
        for i in self.rating:
            total+=i
            count+=1
        avg = (total)/count
        return float(avg)

    def display(self):
        print('Movie: ',self.title)
        print('Category: ',self.category)
        print('Rating: ',self.rating)

    def highest_rating(self,obj1,obj2):
        if obj1.cal_avg() > obj2.cal_avg():
            print(obj1.title,'have highest rating')
        else:
            print(obj2.title,'have highest rating')
obj1 = movie('Reacher','action',[1,4,7,3,9,6])
obj2 = movie('Jurassic world','adventure',[3,5,6,7])
obj1.display()
print()
obj1.add_rating()
obj2.add_rating()
print()
print(obj1.title,':',obj1.cal_avg())
print(obj2.title,':',obj2.cal_avg())
print()
obj1.highest_rating(obj1,obj2)