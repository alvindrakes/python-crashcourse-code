class Car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes to describe the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """return the reading of the car's odometer"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        update the reading of the car odometer to given value
        reject if want to reset back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Youc can't roll back the odometer!")


    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

class Battery():
    """model a battery for na electric car"""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

    message = "This car can go approximately " + str(range)
    message += " miles on a full charge."
    print(message)


class Electric_car(Car):
    """Models aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
        