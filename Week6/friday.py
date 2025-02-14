print(" --- Friday, February 15th, 2025 | 0800 - 1000 ---")

# Working with CSV Files:

# NOTE: "CSV" stands for "Comma Seperated Values"
# NOTE: You can specify the format / type of output the data can be read as.

# Imported Modules and Files:
import csv
# import pandas

# Function to read CSV file and print data:
def read_csv_as_list():
    with open('folks.csv', 'r') as f:
        data = csv.reader(f, delimiter=',')
        print(type(data))
        
        next(data)
        
        for line in data:
            print(line)
            
# Function to read CSV file and print data as one list:
def read_csv_as_list_optimized():
    with open('folks.csv', 'r') as f:
        data = csv.reader(f, delimiter=',')
            
        return [line for line in data]
    
# Function to read CSV file and print data as a dictionary:
def read_csv_as_dict():
    with open('folks.csv', 'r') as f:
        data = csv.DictReader(f, delimiter=',')
            
        for line in data:
            print(line)
            
# Function to read CSV file and print data using Pandas:
'''def read_csv_pandas():
    df = pandas.read_csv('folks.csv')
    print(type(df))
    print(df)
'''

# Function to write data to a CSV file:
def write_csv():
    with open('folks_new.csv', 'w', newline='') as f:
        fieldnames = ['Name', 'Age', 'Id', 'Email']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        
        writer.writerow({'Name': 'John Doe', 'Age': 30, 'Id': 1, 'Email': 'johndoe@example.com'})
        writer.writerow({'Name': 'Jane Smith', 'Age': 28, 'Id': 2, 'Email': 'janesmith@example.com'})
        writer.writerow({'Name': 'Bob Johnson', 'Age': 32, 'Id': 3, 'Email': 'bobjohnson@example.com'})
        

if __name__ == "__main__":
    # read_csv_as_list()
    # read_csv_as_list_optimized()
    # read_csv_as_dict()
    # read_csv_pandas()
    write_csv()