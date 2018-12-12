# Program Description:     Classes and Objects
# Author:                  Gerry Byrne
# Date of creation:        15/06/2015


# class Car(object):
#     """A car for sale by a Car Dealership.
#
#     Attributes:
#         wheels: An integer representing the number of wheels the car has.
#         miles: The integral number of miles driven on the car.
#         make: The make of the car as a string.
#         model: The model of the car as a string.
#         year: The integral year the car was built.
#         sold_on: The date the vehicle was sold.
#     """
#
#     def __init__(self, wheels, miles, make, model, year, sold_on):
#         """Return a new Car object."""
#         self.wheels = wheels
#         self.miles = miles
#         self.make = make
#         self.model = model
#         self.year = year
#         self.sold_on = sold_on
#
#     def sale_price(self):
#         """Return the sale price for this car as a float amount."""
#         if self.sold_on is not None:
#             return 0.0  # Already sold
#         return 5000.0 * self.wheels
#
#     def purchase_price(self):
#         """Return the price for which we would pay to purchase the car."""
#         if self.sold_on is None:
#             return 0.0  # Not yet sold
#         return 8000 - (.10 * self.miles)
#
#     class Truck(object):
#         """A truck for sale by a Car Dealership.
#
#         Attributes:
#             wheels: An integer representing the number of wheels the truck has.
#             miles: The integral number of miles driven on the truck.
#             make: The make of the truck as a string.
#             model: The model of the truck as a string.
#             year: The integral year the truck was built.
#             sold_on: The date the vehicle was sold.
#         """
#
#         def __init__(self, wheels, miles, make, model, year, sold_on):
#             """Return a new Truck object."""
#             self.wheels = wheels
#             self.miles = miles
#             self.make = make
#             self.model = model
#             self.year = year
#             self.sold_on = sold_on
#
#         def sale_price(self):
#             """Return the sale price for this truck as a float amount."""
#             if self.sold_on is not None:
#                 return 0.0  # Already sold
#             return 5000.0 * self.wheels
#
#         def purchase_price(self):
#             """Return the price for which we would pay to purchase the truck."""
#             if self.sold_on is None:
#                 return 0.0  # Not yet sold
#             return 10000 - (.10 * self.miles)

from abc import ABCMeta, abstractmethod


class Vehicle(object):
    """A vehicle for sale by a Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        """Return a new Vehicle object."""
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass


class Car(Vehicle):
    """A car for sale by a Car Dealership."""

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'


class Truck(Vehicle):
    """A truck for sale by Jeffco Car Dealership."""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'


class Motorcycle(Vehicle):
    """A motorcycle for sale by Jeffco Car Dealership."""

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'motorcycle'


myVehicle = Motorcycle(10000, 'Ford','Fiesta', 2017, '01/01/2017')
print(myVehicle.vehicle_type())
print(myVehicle.base_sale_price)
print(myVehicle.wheels)
print(myVehicle.year)
