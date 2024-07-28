import datetime
import mysql.connector

# Connection to mysql database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="amal",
  database="project"
)

mycursor = mydb.cursor()

# Function to display employee details
def display_employee():
    print("\nDisplaying Employee Details...")
    # Code to retrieve and display employee details from the database[AMAL]
    mycursor.execute("select * from employees")
    myresult = mycursor.fetchall()
    print("(empid, empname, empdept, empcity, empsalary")
    for x in myresult:
        print(x)

# Function to add employee
def add_employee():
    print("\nAdding Employee...")
    # Code to get new employee details from the user and add to the database[AMAL]
    a = input("Enter empid: ")
    b = input("Enter empname: ")
    c = input("Enter empdept: ")
    d = input("Enter empsalary: ")
    e = input("Enter empcity: ")
    sql = "insert into employees values("+a+",'"+b+"'"+",'"+c+"','"+e+"',"+d+");"
    mycursor.execute(sql)
    mydb.commit()

# Function to remove employee
def remove_employee():
    print("\nRemoving Employee...")
    # Code to get employee details to remove from the user and remove from the database[AMAL]
    a = input("Enter empid: ")
    sql = "delete from employees where empid = "+a+";"
    mycursor.execute(sql)

# Function to update employee details
def update_employee():
    print("\nUpdating Employee Details...")
    # Code to get employee details to update from the user and update in the database[AMAL]
    a = input("Enter empid: ")
    b = input("Enter empname: ")
    c = input("Enter empdept: ")
    d = input("Enter empcity: ")
    sql = "update employees set empname = '"+b+"', empdept = '"+c+"', empcity ='"+d+"' where empid = "+a+";"
    mycursor.execute(sql)
    mydb.commit()


# Function to display employee salary details
def display_employee_salary():
    print("\nDisplaying Employee Salary Details...")
    # Code to retrieve and display employee salary details from the database[AMAL]
    sql = "select empid, empname, empdept, empsalary from employees;"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print("(empid, empname, empdept, empsalary)")
    for x in result:
        print(x)

# Function to update employee salary details
def update_employee_salary():
    print("\nUpdating Employee Salary Details...")
    # Code to get employee salary details to update from the user and update in the database[AMAL]
    a = input("Enter empid: ")
    b = input("Enter empsalary: ")
    sql = "update employees set empsalary = "+b+" where empid = "+a+";"
    mycursor.execute(sql)
    mydb.commit()

# Function to handle HR login process and menu options
def hr_login():
    # Prompt for HR login credentials
    hr_username = input("\nEnter HR username: ")
    hr_password = input("Enter HR password: ")

    # Check if the credentials are correct
    if hr_username == "hruser" and hr_password == "hrpassword":
        print("\nLogin successful! Welcome, HR.")

        # Database connection code here...[AMAL]

        # Display HR menu options
        while True:
            print("\nHR Menu:")
            print("1. Display Employee Details")
            print("2. Add Employee")
            print("3. Remove Employee")
            print("4. Update Employee Details")
            print("5. Salary Management")
            print("6. Logout")
            hr_choice = input("\nEnter your choice (1-6): ")
            if hr_choice == '1':
                display_employee()
            elif hr_choice == '2':
                add_employee()
            elif hr_choice == '3':
                remove_employee()
            elif hr_choice == '4':
                update_employee()
            elif hr_choice == '5':
                salary_management()
            elif hr_choice == '6':
                print("\nLogging out of HR account.")
                break
            else:
                print("\nInvalid choice. Please try again.")
    else:
        print("\nInvalid HR username or password. Please try again.")
        
        
def emp_login():
    # Prompt for HR login credentials
    emp_username = input("\nEnter Emp username: ")
    emp_password = input("Enter Emp password: ")

    # Check if the credentials are correct
    if emp_username == "empuser" and emp_password == "emppassword":
        print("\nLogin successful! Welcome, Emp.")

        # Database connection code here...[AMAL]

        # Display HR menu options
        while True:
            print("\nEmp Menu:")
            print("1. Display Employee Details")
            print("2. Apply Leave")
            print("3. Salary Upraisal")
            print("4. Logout")
            emp_choice = input("\nEnter your choice (1-4): ")
            if emp_choice == '1':
                display_employee()
            elif emp_choice == '2':
                apply_leave()
            elif emp_choice == '3':
                salary_appraisal()
            elif emp_choice == '4':
                print("\nLogging out of Emp account.")
                break
            else:
                print("\nInvalid choice. Please try again.")
    else:
        print("\nInvalid Emp username or password. Please try again.")

# Function to apply leave       
def apply_leave():
    print("Leave Management System")
    a = input("Enter your empid: ")
    b = input("Enter your Name: ")
    c = input("Enter your start date: ")
    d = input("Enter your end date: ")
    e = input("Enter timeperiod of leave: ")
    sql = "insert into empleave values("+a+",'"+b+"'"+",'"+c+"','"+d+"','"+e+"');"
    mycursor.execute(sql)
    mydb.commit()
    
    
# Function for salary appraisal
def salary_appraisal():
    print("Salary Appraisal System")
    a = input("Enter your empid: ")
    b = input("Enter your Name: ")
    c = input("Would you like to Apply for your next Salary Appraisal Interview[yes//no]: ")
    sql = "insert into empsalary values("+a+",'"+b+"'"+",'"+c+"');"
    mycursor.execute(sql)
    mydb.commit()
    

# Function to handle salary management options
def salary_management():
    while True:
        print("\nSalary Management Menu:")
        print("1. Display Employee Salary Details")
        print("2. Update Employee Salary Details")
        print("3. Return to HR Menu")
        salary_choice = input("\nEnter your choice (1-3): ")
        if salary_choice == '1':
            display_employee_salary()
        elif salary_choice == '2':
            update_employee_salary()
        elif salary_choice == '3':
            print("\nReturning to HR Menu.")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Function to track login time for HR users
def track_login_time(username):
    now = datetime.datetime.now()
    login_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{username} logged in at: {login_time}")

# Main function to run the HRMS program
def main():
    while True:
        print("\nWelcome to HRMS!")
        print("1. HR Login")
        print("2. Employee Login")
        print("3. Exit")
        choice = input("\nEnter your choice (1-3): ")
        if choice == '1':
            hr_username = input("\nEnter HR username: ")
            hr_password = input("Enter HR password: ")
            if hr_username == "hruser" and hr_password == "hrpassword":
                track_login_time(hr_username)
                hr_login()
            else:
                print("\nInvalid HR username or password. Please try again.")
        elif choice == '2':
            emp_username = input("\nEnter Emp username: ")
            emp_password = input("Enter Emp password: ")
            if emp_username == "empuser" and emp_password == "emppassword":
                track_login_time(emp_username)
                emp_login()
            else:
                print("\nInvalid HR username or password. Please try again.")
        elif choice == '3':
            print("\nExiting HRMS. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
