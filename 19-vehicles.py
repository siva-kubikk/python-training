class Vehicle:
    def __init__(self,make,model,year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def display_vehicle_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, door_count) -> None:
        super().__init__(make, model, year)
        self.door_count = door_count

    def display_vehicle_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Doors: {self.door_count}"


class Truck(Vehicle):
    def __init__(self, make, model, year, bed_length) -> None:
        super().__init__(make, model, year)
        self.bed_length = bed_length

    # def display_vehicle_info(self):
    #     print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Bed length: {self.bed_length}")
    def display_vehicle_info(self):
        return f"{super().display_vehicle_info()}, bedlength: {self.bed_length}"
        # super().display_vehicle_info()
        # print(f"{super().display_vehicle_info()}, Bed length: {self.bed_length}")
        # print(f"Bed length: {self.bed_length}")
class VehicleManager:
    def __init__(self) -> None:
        self.vehicles=[]

    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def display_all_vehicles(self):
        for vehicle in self.vehicles:
            vehicle.display_vehicle_info()

v=Vehicle("Honda", "Civic", 2022)
c=Car("Nissan", "Rogue", 2023,4)
t=Truck("Ford", "F150", 2023,40)

vm = VehicleManager()
vm.add_vehicle(v)
vm.add_vehicle(c)
vm.add_vehicle(t)

print(t.display_vehicle_info())
print("-------")
vm.display_all_vehicles()
