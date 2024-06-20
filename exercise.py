#CREATE A CLASS CALLED CARS WITH THE FOLLOWING ATTRIBUTES
#MODEL, YEAR OF MANUFACTURE, TYPE, COLOR

#CRETE A METHOD TO PRINT
#"MY DREAM CAR IS... MANUFACTURED IN... BEING A...TYPE... IN COLOR"

#INITIALIZE WITH AT LEAST 5 OBJECT

class Cars:
    def __init__(self, model, year_of_manufacture, types, color):
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.types = types
        self.color = color

    def display(self):
        print(f"My dream car is {self.model}, manufactured in {self.year_of_manufacture}, being a {self.types}, in color {self.color}")


car = Cars('Audi', 2023, 'RTTS', 'Black')
car.display()
car2 = Cars('Mercedez', 2018, 'GLE', 'Black')
car2.display()
car3 = Cars('BMW', 2020, 'M5', 'Black')
car3.display()
car4 = Cars('Porsche', 2015, 911, 'Black')
car4.display()
car5 = Cars('Bugatti', 2022, 'Chiron', 'Blue')
car5.display()