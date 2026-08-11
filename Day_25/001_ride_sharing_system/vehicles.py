from abc import ABC, abstractmethod


class Vehicles(ABC):
    def __init__(self, driver_name, rating=3):
        self.driver_name = driver_name
        self.rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5.")
        self._rating = value

    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bike(Vehicles):
    fare_per_km = 60

    def calculate_fare(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        return distance * self.fare_per_km


class Car(Vehicles):
    fare_per_km = 80

    def calculate_fare(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        return distance * self.fare_per_km