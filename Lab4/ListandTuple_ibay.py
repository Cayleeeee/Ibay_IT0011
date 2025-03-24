import json

# Function to load student records from a file
def open_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return [tuple(record) for record in data]  
    except FileNotFoundError:
        print("File not found. Starting with an empty record list.")
        return []
    except json.JSONDecodeError:
        print("Error reading file. Data might be corrupted.")
        return []

# Function to save student records to a file
def save_file(filename, records):
    with open(filename, "w") as file:
        json.dump(records, file)
    print("Records saved successfully.")

# Function to display all student records
def show_all_records(records):
    if not records:
        print("No records available.")
        return
    for record in records:
        print(record)

# Function to sort by last name
def order_by_lastname(records):
    return sorted(records, key=lambda x: x[1][1])

# Function to sort by computed grade
def order_by_grade(records):
    return sorted(records, key=lambda x: (x[2] * 0.6 + x[3] * 0.4), reverse=True)

# Function to search for a student record
def show_student_record(records, student_id):
    for record in records:
        if record[0] == student_id:
            return record
    return None

# Function to add a new record
def add_record(records):
    try:
        student_id = int(input("Enter Student ID (6-digit number): "))
        if len(str(student_id)) != 6:
            print("Invalid ID. Must be a 6-digit number.")
            return records
        
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Major Exam Grade: "))

        records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully.")
        return records
    except ValueError:
        print("Invalid input. Please enter the correct data type.")
        return records

# Function to edit a record
def edit_record(records, student_id):
    for i, record in enumerate(records):
        if record[0] == student_id:
            try:
                first_name = input(f"Enter New First Name (Current: {record[1][0]}): ")
                last_name = input(f"Enter New Last Name (Current: {record[1][1]}): ")
                class_standing = float(input(f"Enter New Class Standing (Current: {record[2]}): "))
                major_exam = float(input(f"Enter New Major Exam Grade (Current: {record[3]}): "))

                records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
                print("Record updated successfully.")
                return records
            except ValueError:
                print("Invalid input. Please enter the correct data type.")
                return records
    print("Student ID not found.")
    return records

# Function to delete a record
def delete_record(records, student_id):
    for i, record in enumerate(records):
        if record[0] == student_id:
            del records[i]
            print("Record deleted successfully.")
            return records
    print("Student ID not found.")
    return records

# Main program loop
filename = "students.json"
students = open_file(filename)

while True:
    print("\nStudent Record Management")
    print("1. Show All Students")
    print("2. Order by Last Name")
    print("3. Order by Grade")
    print("4. Show Student Record")
    print("5. Add Record")
    print("6. Edit Record")
    print("7. Delete Record")
    print("8. Save File")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_all_records(students)
    elif choice == "2":
        students = order_by_lastname(students)
        show_all_records(students)
    elif choice == "3":
        students = order_by_grade(students)
        show_all_records(students)
    elif choice == "4":
        student_id = int(input("Enter Student ID: "))
        record = show_student_record(students, student_id)
        if record:
            print(record)
        else:
            print("Student not found.")
    elif choice == "5":
        students = add_record(students)
    elif choice == "6":
        student_id = int(input("Enter Student ID to edit: "))
        students = edit_record(students, student_id)
    elif choice == "7":
        student_id = int(input("Enter Student ID to delete: "))
        students = delete_record(students, student_id)
    elif choice == "8":
        save_file(filename, students)
    elif choice == "9":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number from 1-9.")
