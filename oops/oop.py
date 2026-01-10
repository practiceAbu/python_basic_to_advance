class Car :

    def __init__(self,make,model,year):
        self.make = make 
        self.model = model
        self.year = year

    def display_info(self):
        print(f'{self.make} {self.model} {self.year}')

car1 = Car("Toyata" , "V5" , 2004)
car2 = Car("BMW","M3",2012)

# car1.display_info()
# car2.display_info()


class ElectricCar(Car):
    def __init__(self,make,model,year,batteryCappacity):
        super().__init__(make,model,year)
        self.batteryCappacity = batteryCappacity

    def display_info(self):
        super().display_info()
        print(f'Battery Capacity {self.batteryCappacity} Kwh')

electricCar = ElectricCar('Tesla','s3',2021,5000)
electricCar.display_info()