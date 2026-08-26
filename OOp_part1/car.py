class car:

    def __init__(self,brand,model,feul,feul_cons):
        self.brand = brand
        self.model = model
        self.feul = feul
        self.feul_cons = feul_cons

    def drive(self,distance):
        fuel_used =  distance/self.feul_cons

        if fuel_used <= self.feul:
            self.feul -= fuel_used
            return f'Car drove {distance} km'
        else:
            return 'Not enough fuel '

    def refuel(self,amount):
        self.feul+=amount
        return f'Fuel added: {amount}'

    def display(self):
        return self.feul

obj = car('BMW','M4',100,10)
print(obj.drive(distance=100))
print(obj.refuel(10))
print(obj.display())
