from controller.employee import Employee
from utils.validation import Validation
import views.prompt 

class Menu:

    def employee_menu(details):
        while True:
            CHOICE = views.prompt.EMPLOYEE_MENU
            print(CHOICE)
            choice = input("\nEnter your choice:")
            print()

            if choice == '1':
                Employee.view_details(details)

            elif choice == '2':
                Menu.update_details(details)

            elif choice == '3':
                Employee.add_leave(details)

            elif choice == '4':
                Employee.add_attendance(details)

            elif choice == '5':
                print("Thankyou for logging in!")
                break

            else:
                print("Invalid option!")


    def manager_menu(details, role):
        while True:
            CHOICE = views.prompt.MANAGER_MENU
            print(CHOICE)
            choice = input("\nEnter your choice:")
            print()

            if choice == '1':
                Employee.view_details(details)

            elif choice == '2':
                Menu.update_details(details)

            elif choice == '3':
                Employee.add_leave(details)

            elif choice == '4':
                Employee.add_attendance(details)

            elif choice == '5':
                Employee.add_employee(details, role)

            elif choice == '6':
                Employee.remove_employee()

            elif choice == '7':
                Employee.view_attendance(details)

            elif choice == '8':
                Employee.view_leave(details)

            elif choice == '9':
                print("Thankyou for logging in!")
                break

            else:
                print("Enter valid choice!")
    
                
    def update_details(self):
        while True:
            CHOICE = views.prompt.UPDATE_MENU
            print(CHOICE)
            choice = input("\nEnter your choice: ")
            
            if choice == '1':
                new_number = Validation._check_phone_validity_()
                Employee.change_phone(self, new_number)
                
            elif choice == '2':
                new_password = Validation._check_password_validity_()
                Employee.change_password(self, new_password)

            elif choice == '3':
                print()
                break

            else:
                print("Invalid choice!")
