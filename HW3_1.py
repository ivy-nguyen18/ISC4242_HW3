'''
Design a program that asks the user to enter the file name for processing, and processes the file
according to the following scenario:
Assumptions:
The file is in .CSV format containing the comma-separated values for the following table:
account_id total_debt contact_email
12345 209.10 john@companyname.com
10215 0.00 someuser@aol.com
18215 32.15
… … …
Some rows may have no contact email address, which is OK.
The very first row in the file must be:
account_id,total_debt,contact_email
Actions:
If the file is not found, the program must say this and terminate.
If the first line is different from the above, your program should tell “Invalid file format!” and terminate
Your program has to ignore empty lines (except the very first one – see above) and check that in every
non-empty row, the first element is an integer, the second one – float, and the third column is a string,
which might be empty. You might want to use conversion and exceptions mechanism.
If the conditions are satisfied, we will call such file well-formatted.
If the file is not well-formatted, the program must specify this saying in which line there is a problem.
If everything is OK, the program should print out the total debt on the list.
Note 1: In real life, you will often receive data saved as various files. It is important to work carefully
with them assuming there could be broken records, incorrect file structure, etc. The main purpose of
this problem is to teach you how to work with file input correctly.
Note 2: When your algorithm is done with working on the file, it must not forget to close it.
'''

def getHeading(file):
    heading = file.readline().strip()
    if heading != "account_id,total_debt,contact_email":
        print("Invalid file format!")
        return 0

def getThreeElements(line):
    elem = line.split(",")
    if len(elem) == 2:
        return elem[0], elem[1], ""
    return elem

def checkInt(test):
    if test.isdigit():
        return int(test)
    else:
        return -1

def checkFloat(test):
    try:
        return float(test)
    except ValueError:
        return -1

def getFile(file_name):
    i = 1
    try: 
        with open(file_name, "r") as file:
            if getHeading(file) == 0:
                return 0
            sum = 0
            for line in file:
                i += 1
                line = line.strip()
                if len(line) > 0:
                    integer, floats, string = getThreeElements(line)
                    account_id = checkInt(integer)
                    total_debt = checkFloat(floats)
                    if account_id == -1:
                        print(f"Error in line {i}: Invalid input for account_id")
                        return 0
                    if total_debt == -1:
                        print(f"Error in line {i}: Invalid input for total_debt")
                        return 0
                    sum += total_debt
            print(f"The total debt is {sum}")    

    except FileNotFoundError as e:
        print("File Not Found!")
        return 0
    except ValueError as e:
        print(f"Error in line {i}: {e}")
        return 0

file_name = input("Please Enter A File: ")
if getFile(file_name) == 0:
    print("Exiting Program")