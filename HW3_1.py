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