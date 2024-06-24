#create a student class
class Student():

    #define a constructor
    #the constructor is a function that executes when an object is created
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
        #assign class property values
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = int(credit_hours)
        self.__gpa = float(gpa)
        self.__id_number = int(id_number)

    #create get and set methods for class properties
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_major(self):
        return self.__major
    
    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_gpa(self):
        return self.__gpa

    def get_id_number(self):
        return self.__id_number
    
    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}:")
        print(f"Major: {self.__major}, Credit Hours: {self.__credit_hours}")
        print(f"GPA: {self.__gpa}, ID Number: {self.__id_number}\n")