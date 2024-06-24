import student
import random
from datetime import datetime
"""
function to write error log file
input: error message
output: none
"""
def write_to_error_log(error_message):
    try:
        #open log file
        log_file = open("error_log.txt", "a")

        #write error message to log file
        log_file.write(f"{datetime.now(): {error_message}}\n")

        #close log file
        log_file.close()
    except Exception as err:
        print(err)

    return

#function to load student data from file
#input: path to the file
#output: list of student data
def load_students(file_name):
    #create an empty list to store student data
    student_list = []
    
    #open the file
    student_file = open(file_name, "r")
    
    #ignore the header data row in the file
    next(student_file)
    
    #read each line of the file in for a for loop
    line_number = 1
    for line_of_data in student_file:
        
        #increment line number by 1
        line_number += 1
        
        #split each line at the comma to get the values
        student_data = line_of_data.split(",")

        #check that vehicle_data contains 6 items
        #if not, raise error and skip that line of data
        try:
            if len(student_data) != 6:
                raise Exception(f"There is an error in your data file on line {line_number}")
        except Exception as err:
            write_to_error_log(str(err))
            continue

        #get individual values from the resulting list
        try:
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit_hours = int(student_data[3])
            gpa = float(student_data[4])
            id_number = int(student_data[5])
        except Exception as err:
            write_to_error_log(f"Error: {err} on line {line_number}")
            continue

        #create automobile objects with the data
        new_student = student.Student(first_name, last_name, major, credit_hours, gpa, id_number)

        #append each automobile to the list of automobiles
        student_list.append(new_student)

    #close file and return list of automobiles
    student_file.close()
    return student_list

def main():
    #load a list of automobiles from data in a file
    student_list = load_students("student.csv")
    rand_student = random.randint(0,200)
    student1 = student_list[rand_student]
    student1.print_student_data()
    rand_student = random.randint(0,200)
    student2 = student_list[rand_student]
    student2.print_student_data()
    
    #print info for each automobile in a for loop
    #for student in student_list:
        #student.print_student_data()

main()