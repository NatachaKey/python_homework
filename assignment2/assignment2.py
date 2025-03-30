import csv
import os
import custom_module 
from datetime import datetime
#task2
def read_employees():
    dict={}
    rows=[]
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index==0:
                    dict['fields']=row
                else:
                    rows.append(row)
        dict["rows"]=rows
        return dict
    except TypeError:
            return "You can't multiply those values!"

employees=read_employees()

#task3
def column_index(string):
    try:
        return employees["fields"].index(string)
    except TypeError:
        return 'Error found'

employee_id_column=column_index("employee_id")

#task4

def first_name(row_number):
    employee_first_name_column_index=column_index("first_name") #returns 1
    try:
        return employees['rows'][row_number][employee_first_name_column_index] #This line retrieves a specific value from the employees dictionary.This retrieves the list of employee rows.
    #Here, row_number is an integer that specifies which row to access; employee_id_column is an integer that specifies which column to access.
    except TypeError:
        return 'You can´t use this values'
#print('this is employees')    #it´s a dictionary {}, object in js
#print(employees)
#print()
#print('this is fields')
#print(employees['fields']) #it´s a list , array in js
#print()
#print('this is rows')
#print(employees['rows'])  #it´s a list of lists [], array of arrays in js
#print()
#print('this is the output')
print(first_name(1))

#task5

def employee_find(emp_id):
    try:
        def employee_match(row):
            return int(row[employee_id_column]) == emp_id
        matches=list(filter(employee_match, employees["rows"]))
        return matches
    except ValueError:
        return "Value is not correct"
    
employee_find(3)

#task6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

employee_find_2(4)

#task7
def sort_by_last_name():
    employee_last_name_column_index=column_index("last_name")
    try:
        employees["rows"].sort(key= lambda row: row[employee_last_name_column_index] )
        return employees["rows"]
        
    except ValueError:
        return "Value is not correct"
    
sort_by_last_name()

#task8
def employee_dict(row):
    try:
        keys=employees['fields'][1:]
        
        values=row[1:]
        
        employee=dict(zip(keys, values))
        return employee
    except KeyError as e:
        return e
print(employee_dict(employees['rows'][0]))

#task9
def all_employees_dict():

    all_employees = {}
    for employee in employees["rows"]:
        print(employee)
        emp_id = employee[0]  # Get employee_id
        print(emp_id)
        all_employees[emp_id] = employee_dict(employee)  # Store employee data
    return all_employees
all_employees_dict()

#task10

def get_this_value():
    return os.getenv('THISVALUE')
get_this_value()

#task11
def set_that_secret(newest_secret):
    try:
        return custom_module.set_secret(newest_secret)
    
    except Exception as e:
        return e
set_that_secret('open sesame')
print(custom_module.secret)

#task12
minutes1={}
minutes2={}
def read_minutes():
    try:
        def reader(read_file, minutes):
            minutes={}
            rows=[]
            with open(read_file, 'r') as file:
                reader = csv.reader(file)
                for index, row in enumerate(reader):
                    if index==0:
                        minutes['fields']=row
                    else:
                        rows.append(tuple(row))
            minutes["rows"]=rows
            return minutes
        global minutes1, minutes2
        minutes1=reader('../csv/minutes1.csv', minutes1)
        minutes2=reader('../csv/minutes2.csv', minutes2)
        return minutes1, minutes2
    except TypeError:
            return "You can't use those values!"
read_minutes()

#Task 13
minutes_set=set()
def create_minutes_set():
    try:
        set1 = set(tuple(row) for row in minutes1.get("rows"))
        set2 = set(tuple(row) for row in minutes2.get("rows"))
        unionSet=set1.union(set2)
        global minutes_set
        minutes_set=unionSet
        return minutes_set
    except Exception as e:
        return e
create_minutes_set()
#IMPORTANT.TO PASS ALL THE TESTS IN TERMINAL TYPE:  export THISVALUE=ABC ; PYTEST

#Task 14
minutes_list=[]
def create_minutes_list():
    try:
        return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    except Exception as e:
        return e
minutes_list=create_minutes_list()

#Task 15
def write_sorted_list():
    try:
        global minutes_list
        sortedList=sorted(minutes_list, key=lambda x: x[1])
        newList=list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),sortedList))
        
        with open('./minutes.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1['fields'])
            for row in newList:
                writer.writerow(row)

        return newList
    except Exception as e:
        return e
write_sorted_list()