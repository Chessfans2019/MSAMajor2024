#create an automobile class
import datetime
class Automobile():
    
    #define a constructor
    #the constructor is a function that executes when an object is created
    def __init__(self, make, model, vin, engine_size, owner, year):
        #assign class property values
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
        self.year = year

    #create get and set methods for class properties
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_vin(self):
        return self.vin
    
    def get_engine_size(self):
        return self.engine_size
    
    def set_engine_size(self, new_size):
        try:
            self.engine_size = float(new_size)
        except:
            print("Error: Engine size must be a number\n")

    def get_owner(self):
        return self.owner
    
    def set_owner(self, new_owner):
        #check that the new owner is not an empty string
        if new_owner == "":
            print("Error: Must enter new owner's name")
            return
        self.owner = new_owner

    def get_year(self):
        return self.year
    
    #create a method to get the automobile age
    def get_age(self):
        #get the current year
        current_date = datetime.datetime.now()
        this_year = current_date.year

        #return the difference between current year and auto year
        return this_year - self.year

    def print_info(self):
        print(f"{self.year} {self.make} {self.model}")
        print(f"VIN: {self.vin}, Engine Size: {self.engine_size}")
        print(f"Owner: {self.owner}\n")