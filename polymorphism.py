# Base class representing a general Vehicle
class Vehicle:
    def __init__(self, brand, model):
        # Protected attributes using underscore to indicate encapsulation
        self._brand = brand
        self._model = model

    def display_info(self):
        """Display basic vehicle information."""
        print(f"Brand: {self._brand}, Model: {self._model}")

    def move(self):
        """Generic move method to be overridden in child classes."""
        print("The vehicle is moving.")

# Derived class representing a Car
class Car(Vehicle):
    def __init__(self, brand, model, number_of_doors):
        # Call the constructor of the base class
        super().__init__(brand, model)
        # Add an attribute specific to Car
        self._number_of_doors = number_of_doors

    def display_info(self):
        """Override display_info to include doors."""
        super().display_info()
        print(f"Number of doors: {self._number_of_doors}")

    def move(self):
        """Override the move method for Car."""
        print("The car is driving on the road.")

    def honk(self):
        """Unique method for Car."""
        print("Beep beep!")

# Derived class representing a Plane
class Plane(Vehicle):
    def __init__(self, brand, model, wingspan):
        # Call the constructor of the base class
        super().__init__(brand, model)
        # Add an attribute specific to Plane
        self._wingspan = wingspan

    def display_info(self):
        """Override display_info to include wingspan."""
        super().display_info()
        print(f"Wingspan: {self._wingspan} meters")

    def move(self):
        """Override the move method for Plane."""
        print("The plane is flying in the sky.")

    def take_off(self):
        """Unique method for Plane."""
        print("Plane is taking off!")

# Testing and Demonstration
def main():
    # Instantiate a Car object
    my_car = Car("Toyota", "Corolla", 4)
    print("Car Info:")
    my_car.display_info()
    my_car.move()       # Demonstrates polymorphism
    my_car.honk()
    print()

    # Instantiate a Plane object
    my_plane = Plane("Boeing", "747", 68.5)
    print("Plane Info:")
    my_plane.display_info()
    my_plane.move()     # Demonstrates polymorphism
    my_plane.take_off()

# Entry point of the script
if __name__ == "__main__":
    main()
