class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)

obj = Rectangle(10,5)
print('Area:',obj.area())
print('Perimter:',obj.perimeter())

# This code return calculated area and perimeter

#        Length = 10m
#   ┌──────────────────┐
#   │                  │
#   │                  │ Width = 5m
#   │                  │
#   └──────────────────┘