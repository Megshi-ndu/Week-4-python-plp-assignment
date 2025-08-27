# This is an example of how a program file is opened.
# The file is opened in read mode and then in write mode to add content.

import os
os.makedirs("./WEEK_4/", exist_ok=True)

# Open the file in write mode and write content to it
with open("./WEEK_4/student_register.txt", "w", encoding='utf-8') as file:
    file.write("student_name, student_id, student_grade")

# Open the file in read mode
with open("./WEEK_4/student_register.txt", "r", encoding='utf-8') as file:
    content = file.read()
    print("Initial content:")
    print(content)
    

# Append new content to the file
with open("./WEEK_4/student_register.txt", "a", encoding='utf-8') as file:
    file.write("\nJohn Mwangi, 12345, A")
    file.write("\nRose Wanja, 67890, B")
    file.write("\nPeter Kamau, 11223, A-")

# Read and print the updated content of the file
with open("./WEEK_4/student_register.txt", "r", encoding='utf-8') as file:
    updated_content = file.read()
    print("Updated content:")
    print(updated_content)
# The file is automatically closed after the with block


