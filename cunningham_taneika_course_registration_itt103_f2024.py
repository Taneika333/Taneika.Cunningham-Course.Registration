# -*- coding: utf-8 -*-
"""Cunningham.Taneika-Course_Registration-ITT103-F2024

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/167InzLibaDUgqpOMPpYBPdARYr3leaC3
"""

class Course: #This line defines class named course.
    def __init__(self, course_id, name, fee):#This line is called upon when a new course object is created and initializes the attributes of the object.
        self.course_id = course_id #unique identifier for each course.
        self.name = name # name of the course
        self.fee = fee #cost of the course
    def __str__(self): #This line is used to create a string representation of the object.
        return (f"{self.name} (ID: {self.course_id}, Fee: ${self.fee})") #This line is prints the information stored in the attributes.


class Student: #This line defines a student class.
    def __init__(self, student_id, name, email): #This line is called upon when a new course object is created and initializes the attributes of the object.
        self.student_id = student_id #unique identifier for each student.
        self.name = name #student name
        self.email = email #student email
        self.courses = [] # a list of courses the students are enrolled in
        self.balance = 0 #outstanding balance for all enrolled courses.

    def enroll(self, course): #This is a method that defines enroll so that it can be called upon when a students want to be enrolled to a course.
        if course in self.courses:#This if statement checks if the student is already enrolled in the course.
            print("***********************************************************************************************") #this is for design purposes.
            print(f"You are already enrolled in {course.name}. {self.name} has a balance of: ${self.balance}. ") #if the student is already enrolled this line will be printed as a string.
            print("***********************************************************************************************")
        else: #if the first block is not executed then this else block will be executed.
            self.courses.append(course) #This line adds the course object to the list that holds all the courses that are enrolled to.
            print("***********************************************************************************************")
            print(f"You are enrolled in {course.name}.") #this line print a string when you have successfully enrolled.
            print("***********************************************************************************************")
            self.balance += course.fee #this line update the balance by adding the fee to the enrolled course.

    def get_total_fee(self): #this line defines a method which is to calculate the total fees for all courses that a user is enrolled in.
        return self.balance #This line calculates and print the balance of the courses that the user is in.


class RegistrationSystem: #this line defines a registration system class.
    def __init__(self): #This line is called upon when a new course is course object is created and initializes the attributes of the object.
        self.courses = [] #list that will store all the courses that are added to the registration system.
        self.students = {} #dictionary that will store students by their ID numbers.

    def add_course(self, course_id, name, fee): #This is a method that defines add course so that it can be called upon when a new course is added to the registration system.
        course = Course(course_id, name, fee) #this line is an instance of the class and will use the variables inside as arguments.
        self.courses.append(course) #this line adds a newly created course to the list.
        print("***********************************************************************************************")
        print(f"The course '{name}' with the id {course_id} has been successfully added. ") #this line prints the specific course that has been added.
        print("***********************************************************************************************")

    def register_student(self, student_id, name, email): #This is a method that defines register student so that it can be called upon when a new student is added to the registration system.
        if student_id in self.students: #this line check if a student's ID number already exists.
            print("***********************************************************************************************")
            print(f"Student with ID {student_id} already exists.") #if the ID number already exists this line will be printed.
            print("***********************************************************************************************")
        else:# if the first block is not executed then this else block will be executed.
            student = Student(student_id, name, email) #this line is an instance of the class and will use the variables inside as arguments.
            self.students[student_id] = student #this line adds new students to the dictionary by their student ID.
            print("***********************************************************************************************")
            print(f"The student {name} with id {student_id}, has been successfully registered. ") #this line prints a specific student is successfully registered.
            print("***********************************************************************************************")

    def enroll_in_course(self, student_id, course_id):#This is a method that defines add course so that it can be called upon when a student wants to enroll to a course in the registration system.
        if student_id not in self.students:#this line checks if the student id is not in the student dictionary
            print("***********************************************************************************************")
            print("This student is not registered.")#this line will print if the student is not in the dictionary.
            print("***********************************************************************************************")
            return #this line stops any other execution if the student is not registered.

        student= self.students[student_id] #this line holds the information of the registered students.
        course = next((c for c in self.courses if c.course_id == course_id), None) #this line is using a next function to find a course from the list based on th course id. c is just a variable that represent each course and the if condition searches through the list until c matches the course id.

        if not course: #this line checks if the course variable matches or not.
             print("***********************************************************************************************")
             print("The course entered is not found.") #this line will be printed if the course is not found.
             print("***********************************************************************************************")
             return#this line stops any other execution if the course is not added, therefore a student wont be able to get registered.

        student.enroll(course)#this line adds the new course to the list of courses that the students are enrolled in.

    def calculate_payment(self, student_id):#This is a method that defines calculate payment so that it can be called upon to calculate payment of a student in the registration system.
        try: #this block allows the program to accept exceptions throughout the code.
            if student_id not in self.students:#this line checks if the student id is not in the student dictionary
                print("***********************************************************************************************")
                raise ValueError("This student is not registered.")#if the student id is not in the student dictionary then this line will be printed.
                print("***********************************************************************************************")

            student = self.students[student_id]#this line holds the student information if the student id is valid.
            total_fee = student.get_total_fee() #this line calculate and store the total fee owed by students.
            print("***********************************************************************************************")
            print(f"The total for {student.name} is: ${total_fee:.2f}")#this line print the student name and their total.
            print("***********************************************************************************************")

            payment_min = 0.4 * total_fee #this line calculate and store the minimum payment accepted.
            print("***********************************************************************************************")
            print(f"The minimum payment available to register is: ${payment_min:.2f}") #this line prints if the user makes a payment less than the minimum accepted to register.
            print("***********************************************************************************************")

            payment = float(input("Please enter the amount paid: $")) #this prompt the user to enter the amount they wish to pay.
            if payment >= payment_min:#this line checks if the payment entered is greater than or equal to the minimum payment accepted.
                student.balance -= payment#this line subtract the payment amount made from the student balance if if the payment is sufficient.
                print("***********************************************************************************************")
                print("Successful payment")#this line will be print for confirmation.
                print(f"Your outstanding balance: ${student.balance:.2f}")#this line prints the updated balance
                print("***********************************************************************************************")
            else:#if the first block is not executed then this else block will be executed.
                print("***********************************************************************************************")
                print("This is insufficient payment. Payment has to be at least 40% of the total fee.")#this line will be print if the pament made is less than 40% of the total.
                print("***********************************************************************************************")
        except ValueError as e:#this line will catch any errors in the try block.
            print(f"Error: {e}")#if a valueerror was raised then this line will print the error message from the exception.
        except Exception as e:#this line cathes unexpected errors that may occur other than valueerrors.
            print(f"An unexpected error occurred: {e}")#this line will print the error.

    def check_student_balance(self, student_id):#this is a method that defines the check student balance so that it can be called upon ckeck a student balance based on their id number in the registration system.
        try: #this block allows the program to accept exceptions throughout the code.
            if student_id not in self.students:#this line checks if the student id is not in the student dictionary
                print("***********************************************************************************************")
                raise ValueError("This student is not registered.")# if the student id is not in the student dictionary then this line will be printed.
                print("***********************************************************************************************")
            student = self.students[student_id]#this line holds the student information if the student id is valid.
            print("***********************************************************************************************")
            print(f"The balance for {student.name} (ID: {student.student_id}) is ${student.balance:.2f}")#this line prints the student information along their balance.
            print("***********************************************************************************************")
        except ValueError as e:#this line will catch any errors in the try block.
            print(f"Error: {e}")# if a valueerror was raised then this line will print the error message from the exception.

    def show_courses(self): #This is a method that defines show courses so that it can be called upon with the list of courses in the registration system.
        if self.courses: #this line checks if there are any available courses.
            print("***********************************************************************************************")
            print("Available courses:") #this line serves as a header to show the available courses that will follow.
            for course in self.courses: #this line begins a for loop that iterates over every course in the list.
                print(course) #this line prints all the available courses
                print("***********************************************************************************************")
        else: #if the first block is not executed then this else block will be executed.
            print("***********************************************************************************************")
            print("No courses available.") #This line will be printed if there are no available courses.
            print("***********************************************************************************************")

    def show_registered_students(self): #This is a method that defines show registered students so that it can be called upon in the dictionary of registered students.
        if self.students: #this line checks if there are any available students.
            print("***********************************************************************************************")
            print("Registered Students:") #this line serves as a header to show the available registered students that will follow.
            for student in self.students.values(): #this line begins a for loop that iterates over every student in the dictionary.
                print(f"ID: {student.student_id}, Name: {student.name}, Email: {student.email}") #this line prints the information of each student.
                print("***********************************************************************************************")
        else: #if the first block is not executed then this else block will be executed.
            print("***********************************************************************************************")
            print("No student/s registered.") #this line will be printed if there are no registered students.
            print("***********************************************************************************************")

    def show_students_in_course(self, course_id): #This is a method that defines show the students in a course so that it can be called upon in the dictionary of registered students.
        try: #this block allows the program to accept exceptions throughout the code.
           course =next((c for c in self.courses if c.course_id ==course_id), None)#this line is using a next function to find a course from the list based on th course id. c is just a variable that represent each course and the if condition searches through the list until c matches the course id.
           if not course:#this line checks if the course variable matches or not.
                print("***********************************************************************************************")
                raise ValueError("This course is not found.") #If no course was found, this line raises a ValueError with a message indicating that the specified course does not exist.
           else:#if the first block is not executed then this else block will be executed.
                print("***********************************************************************************************")
                print(f"Students enrolled in {course.name}:") #this line will be printed if the student has successfully enrolled to a course.


                enrolled_students = [student for student in self.students.values() if course in student.courses] #This line creates a list comprehension that iterates over all registered students in self.students.values()
                if enrolled_students: #This line checks if there are any students in the enrolled_students list
                 for student in enrolled_students: #If there are enrolled students, this line begins a loop that iterates over each student in the list.

                    print(f"ID: {student.student_id}, Name: {student.name}, Email: {student.email}") #this line prints the details of each student.
                    print("***********************************************************************************************")
                else: #if the first block is not executed then this else block will be executed.
                 print("***********************************************************************************************")
                 print("No student is enrolled in this course.") #This message will print if there are no students are currently enrolled in the specified course
                 print("***********************************************************************************************")
        except ValueError as e: #This line begins an except block that catches any ValueError exceptions raised within the try block
                 print(f"Error: {e}") # this line prints an error message that includes details from the caught exception (e)


# This is the main section of the program
system = RegistrationSystem() #this line creates an instance of the class and assigns it to a variable that will manage students registration information.
is_running = True #this line controls the functionality of the program until the user chooses to exit.

while is_running: #this while loop will continue printing its information until the user exits.
    print("Welcome to UCC dashboard. ") #this will be printed to greet the user on the registration dashboard.
    print("1. Add a course") #option for the user to add a course
    print("2. Register students") #option for the user to register a student
    print("3. Enroll in a course") #option for the user to enroll a student to a course.
    print("4. Calculate payment") #option for the user to calculate payment
    print("5. Check student balance") #option for the user check a student balance
    print("6. Show available courses") #option for the user to show all available courses
    print("7. Show registered students") #option for the user to show all registered students
    print("8. Show students in a course") #option for the user to show all the students in a specific course.
    print("9. Exit") #if the user choose this option the program will stop.

    try: #this block allows the program to accept exceptions throughout the code.
        choice = input("Enter your choice of action (1-9): ") #this prompts the user to select an option.

        if choice == '1': #this line checks is the variable the user selected is 1.
            course_id = input("Please enter the course ID: ") #this line prompts the user to enter the course id number.
            name = input("Please enter the course name: ") #this line prompts the user to enter the name of the course.
            fee = float(input("Please enter the course fee: $")) #this line prompts the user to enter the cost of the course
            system.add_course(course_id, name, fee) #this line will update the registration sysytem with the user inputs.

        elif choice == '2': #this line checks is the variable the user selected is 2
            student_id = input("Please enter your student ID: ")#this line prompts the user to enter their student id number
            name = input("Please enter the student name: ") #this line prompts the user to enter their name.
            email = input("Please enter your school email: ")#this line prompts the user to enter their email address.
            system.register_student(student_id, name, email)#this line will update the registration sysytem with the user inputs.

        elif choice == '3': #this line checks is the variable the user selected is 3
            student_id = input("Please enter your student ID: ")#this line prompts the user to enter their student id number.
            course_id = input("Please enter your course ID to enroll: ")#this line prompts the user to enter the course id number to enroll in a course.
            system.enroll_in_course(student_id, course_id)#this line will update the registration sysytem with the user inputs.

        elif choice == '4': #this line checks is the variable the user selected is 4
            student_id = input("Please enter your student ID: ")#this line prompts the user to enter their student id number.
            system.calculate_payment(student_id) #this line calculates the payment amount that a specific student owes for all their enrolled courses and updates the system.

        elif choice == '5': #this line checks is the variable the user selected is 5
            student_id = input("Enter your student ID: ")#this line prompts the user to enter their student id number.
            system.check_student_balance(student_id) #this line prints the current balance of a specific student by their id number.

        elif choice == '6': #this line checks is the variable the user selected is 6
            system.show_courses()#this line print a list of all the available courses.

        elif choice == '7': #this line checks is the variable the user selected is 7
            system.show_registered_students() #this line print a dictionary of all the registered students in the system.

        elif choice == '8': #this line checks is the variable the user selected is 8
            course_id = input("Please enter the course ID to see enrolled students: ")#this line prompts the user to enter the course id number so that they can see enrolled students.
            system.show_students_in_course(course_id)#this line prints all the student in a specific course based on the course id.

        elif choice == '9': #this line checks is the variable the user selected is 9
            is_running = False  # if the program is no longer True it will Exit the loop

        else: #if the pervious blocks did not execute then this else block will be executed.
            print("This is an invalid choice, try again.") #this line will be printed if there was an invalid entry.
    except ValueError: #this line will catch any exception that may occur in the try block.
        print("Please enter a valid input (1-9).") #this line will be printed so the user knows that the program only accept inputs from 1-9.