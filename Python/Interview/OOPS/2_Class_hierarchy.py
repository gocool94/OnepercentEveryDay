"""
   - Create a class hierarchy for different types of vehicles (car, bike, truck)
   with shared and specific attributes/methods.

"""

class vehicle:
    def __init__(self,make_year,model,company):
        self.make_year = make_year
        self.model = model
        self.company = company

    def display_vehicle_info(self):
        print(f"Make Year : {self.make_year} Model : {self.model} company : {self.company}")


class Car:
    def __init__(self,make_year,model,company,IsElectric,NumberofDoors):
        self.vehicle = vehicle(make_year,model,company)
        self.electric = IsElectric
        self.numberofDoors = NumberofDoors

    def display_vehicle_info(self):
        self.vehicle.display_vehicle_info()
        if(self.electric == True):
            print(f"This is a electric vehicle and you need charging port")
        else:
            print(f"{self.vehicle.model} is non electric")


class Truck:
    def __init__(self,make_year,model,company,NumberofTyres):
        self.vehicle = vehicle(make_year,model,company)
        self.TyreNumbers = NumberofTyres

    def display_info(self):
        self.vehicle.display_vehicle_info()


MyCar = Car(2022,"Contassa","Apple",True,4)
MyCar.display_vehicle_info()
MyTruck = Truck(2021,"Borosil","Xyram",6)
MyTruck.display_info()