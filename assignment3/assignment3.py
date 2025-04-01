import pandas as pd
import numpy as np
# Task 1: Create DataFrame from dictionary with correct capitalization
dataDict = {
    'Name': ['Alice', 'Bob', 'charlie'],  
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(dataDict)

# Add a new column (Salary)
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]

# Modify an existing column (Increment Age)
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1

# Save the DataFrame as a CSV file
csv_filename = 'employees.csv'
task1_older.to_csv(csv_filename, index=False)

# Task 2
#Read data from a CSV file
task2_employees= pd.read_csv('./employees.csv')
print(task2_employees)

#Read data from a JSON file
json_employees=pd.read_json('additional_employees.json')
print(json_employees)

#Combine DataFrames
more_employees=pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

# Task 3
#the head() method
first_three=more_employees.head(3)
print(first_three)
#the tail() method
last_two=more_employees.tail(2)
print(last_two)
#Get the shape of a DataFrame
employee_shape=more_employees.shape
print(employee_shape)
#the info() method
more_employees.info()

#task 4
dirty_data= pd.read_csv('dirty_data.csv')
clean_data=dirty_data.copy()
clean_data.drop_duplicates(inplace=True)

# errors="coerce" will turn invalid dates into NaN or NaT (Not a Time) 
clean_data['Age']=pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"].replace(["unknown"], pd.NA), errors="coerce")
print(clean_data)

mean_age=clean_data['Age'].mean()
clean_data['Age']=clean_data['Age'].fillna(mean_age)
mean_salary=clean_data['Salary'].mean()
clean_data['Salary']=clean_data['Age'].fillna(mean_salary)
clean_data['Hire Date']= pd.to_datetime(clean_data['Hire Date'], errors='coerce')

clean_data['Department']=clean_data['Department'].str.strip()
clean_data['Name']=clean_data['Name'].str.strip()

clean_data['Department']=clean_data['Department'].str.upper()
clean_data['Name']=clean_data['Name'].str.upper()
print(clean_data)