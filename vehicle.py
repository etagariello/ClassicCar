

class Vehicle:
    number_of_vehicles = 0

    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

        Vehicle.number_of_vehicles += 1
    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight}kg")

    def honk(self):
        print("Beep Beep!")

    @staticmethod
    def is_motorcycle(weight):
        if weight < 500:
            return True
        else:
            return False

# Test driver code
if __name__ == "__main__":
    # Create instances of Vehicle
    car = Vehicle("Toyota", "Corolla", 2021, 1275.0)
    motorcycle = Vehicle("Harley-Davidson", "Street 750", 2019, 220.0)

    # Display information of the car
    print("Car Info:")
    car.display_info()
    car.honk()
    print("Is the car a motorcycle?", Vehicle.is_motorcycle(car.weight))
    print()

    # Display information of the motorcycle
    print("Motorcycle Info:")
    motorcycle.display_info()
    motorcycle.honk()
    print("Is the motorcycle actually a motorcycle?", Vehicle.is_motorcycle(motorcycle.weight))
    # Show total number of vehicles created, if you are going for the Bonus
    print(f"Total number of vehicles: {Vehicle.number_of_vehicles}")
