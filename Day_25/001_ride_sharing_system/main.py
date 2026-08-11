from vehicles import Bike, Car
from decorators import ride_logger
from exceptions import RideHistoryError


@ride_logger
def book_ride():
    try:
        vehicle_type = input("Enter vehicle type (Car/Bike): ").strip().capitalize()
        driver_name = input("Enter driver's name: ").strip().title()

        rating = float(input("Enter driver's rating (1-5): "))
        distance = float(input("Enter distance (km): "))

        if vehicle_type == "Car":
            vehicle = Car(driver_name, rating)

        elif vehicle_type == "Bike":
            vehicle = Bike(driver_name, rating)

        else:
            print("Invalid vehicle type!")
            return

        fare = vehicle.calculate_fare(distance)

        print("\n========== Ride Details ==========")
        print(f"Driver Name : {vehicle.driver_name}")
        print(f"Vehicle     : {vehicle.__class__.__name__}")
        print(f"Rating      : {vehicle.rating}")
        print(f"Distance    : {distance} km")
        print(f"Fare        : Rs. {fare}")

        try:
            with open("ride_history.txt", "a") as file:
                file.write(f"Driver Name : {vehicle.driver_name}\n")
                file.write(f"Vehicle     : {vehicle.__class__.__name__}\n")
                file.write(f"Rating      : {vehicle.rating}\n")
                file.write(f"Distance    : {distance} km\n")
                file.write(f"Fare        : Rs. {fare}\n")
                file.write("-" * 20 + "\n")

            print("\nRide history saved successfully!")

        except Exception as e:
            raise RideHistoryError(f"Error while writing ride history: {e}")

    except ValueError as e:
        print("Input Error:", e)


def main():
    try:
        book_ride()

    except RideHistoryError as e:
        print(e)

    except Exception as e:
        print("Unexpected Error:", e)


main()