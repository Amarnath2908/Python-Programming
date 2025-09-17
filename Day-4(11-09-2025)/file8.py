from abc import ABC, abstractmethod

# -------------------------
# Task 1: Vehicle Classes
# -------------------------
class Vehicle:
    def _init_(self, vid, license_plate, owner):
        self.vid = vid
        self.__license_plate = license_plate   # private
        self.__owner = owner                   # private

    # Getters and setters for private attributes
    def get_license_plate(self):
        return self.__license_plate

    def set_license_plate(self, plate):
        self.__license_plate = plate

    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner

    def display(self):
        print(f"Vehicle ID: {self.vid}, Plate: {self._license_plate}, Owner: {self._owner}")

    def calculate_parking_fee(self, hours):
        raise NotImplementedError("Subclasses must override this method")


class Bike(Vehicle):
    def _init_(self, vid, license_plate, owner, helmet_required):
        super()._init_(vid, license_plate, owner)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike → ID: {self.vid}, Plate: {self.get_license_plate()}, Owner: {self.get_owner()}, Helmet Required: {self.helmet_required}")

    def calculate_parking_fee(self, hours):
        return 20 * hours


class Car(Vehicle):
    def _init_(self, vid, license_plate, owner, seats):
        super()._init_(vid, license_plate, owner)
        self.seats = seats

    def display(self):
        print(f"Car → ID: {self.vid}, Plate: {self.get_license_plate()}, Owner: {self.get_owner()}, Seats: {self.seats}")

    def calculate_parking_fee(self, hours):
        return 50 * hours


class SUV(Vehicle):
    def _init_(self, vid, license_plate, owner, four_wheel_drive):
        super()._init_(vid, license_plate, owner)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print(f"SUV → ID: {self.vid}, Plate: {self.get_license_plate()}, Owner: {self.get_owner()}, 4WD: {self.four_wheel_drive}")

    def calculate_parking_fee(self, hours):
        return 70 * hours


class Truck(Vehicle):
    def _init_(self, vid, license_plate, owner, max_load_capacity):
        super()._init_(vid, license_plate, owner)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"Truck → ID: {self.vid}, Plate: {self.get_license_plate()}, Owner: {self.get_owner()}, Max Load: {self.max_load_capacity} tons")

    def calculate_parking_fee(self, hours):
        return 100 * hours


# -------------------------
# Task 2: ParkingSpot Class
# -------------------------
class ParkingSpot:
    def _init_(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size  # S, M, L, XL
        self.__occupied = False
        self.__vehicle = None

    def assign_vehicle(self, vehicle):
        if not self.__occupied:
            self.__vehicle = vehicle
            self.__occupied = True
            return True
        return False

    def remove_vehicle(self):
        if self.__occupied:
            v = self.__vehicle
            self.__vehicle = None
            self.__occupied = False
            return v
        return None

    def is_occupied(self):
        return self.__occupied

    def get_vehicle(self):
        return self.__vehicle

    def display_status(self):
        if self.__occupied:
            print(f"Spot {self.spot_id} ({self.size}): Occupied → {type(self._vehicle).name} ({self._vehicle.get_license_plate()})")
        else:
            print(f"Spot {self.spot_id} ({self.size}): Empty")


# -------------------------
# Task 3: ParkingLot Class
# -------------------------
class ParkingLot:
    def _init_(self, name):
        self.name = name
        self.spots = []
        print(f"Parking Lot Created: {self.name}")

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        print("\nParking Status:")
        for spot in self.spots:
            spot.display_status()

    def _fits(self, vehicle, spot):
        # Spot size rules
        if isinstance(vehicle, Bike) and spot.size in ["S", "M", "L", "XL"]:
            return True
        elif isinstance(vehicle, Car) and spot.size in ["M", "L", "XL"]:
            return True
        elif isinstance(vehicle, SUV) and spot.size in ["L", "XL"]:
            return True
        elif isinstance(vehicle, Truck) and spot.size == "XL":
            return True
        return False

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot.is_occupied() and self._fits(vehicle, spot):
                spot.assign_vehicle(vehicle)
                print(f"{type(vehicle)._name_} ({vehicle.get_license_plate()}) parked at Spot {spot.spot_id}")
                return
        print(f"No suitable spot available for {type(vehicle)._name_} ({vehicle.get_license_plate()})")

    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            if spot.is_occupied() and spot.get_vehicle() == vehicle:
                spot.remove_vehicle()
                fee = vehicle.calculate_parking_fee(hours)
                print(f"{type(vehicle)._name_} ({vehicle.get_license_plate()}) removed from Spot {spot.spot_id}")
                print(f"Parking Fee = ₹{fee}")

                # Ask for payment
                print("Select Payment Method: 1. Cash  2. Card  3. UPI")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    payment = CashPayment()
                elif choice == 2:
                    payment = CardPayment()
                else:
                    payment = UPIPayment()
                payment.process_payment(fee)
                return
        print(f"Vehicle ({vehicle.get_license_plate()}) not found in lot.")


# -------------------------
# Task 4: Payment Abstraction
# -------------------------
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Cash")


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Card")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using UPI")


# -------------------------
# Task 5: Main Program
# -------------------------
if _name_ == "_main_":
    # Create Parking Lot
    lot = ParkingLot("CityMall Parking")
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "M"))
    lot.add_spot(ParkingSpot(4, "L"))
    lot.add_spot(ParkingSpot(5, "XL"))
    print("Total Spots Added:", len(lot.spots))

    # Create Vehicles
    bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
    car1 = Car("C201", "TS05CD5678", "Priya", 5)
    suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
    truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)

    print("\nVehicles Created:")
    bike1.display()
    car1.display()
    suv1.display()
    truck1.display()

    # Park Vehicles
    print("\n--- Parking Vehicles ---")
    lot.park_vehicle(bike1)
    lot.park_vehicle(car1)
    lot.park_vehicle(suv1)
    lot.park_vehicle(truck1)
    lot.show_spots()

    # Unpark a Car
    print("\n--- Unparking Car ---")
    lot.unpark_vehicle(car1, hours=3)

    # Final Status
    lot.show_spots()
