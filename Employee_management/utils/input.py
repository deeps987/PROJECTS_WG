import maskpass
import settings.config

class AuthDetails:
    
    def auth_login(self):
        #print("Enter your credentials to login!\n ")
        print(settings.config.CREDENTIALS_STATEMENT)
        #self.user_id = input("Enter your user id: ")
        self.user_id = input(settings.config.CREDENTIALS_USERID)
        # self.password = 
        self.password = maskpass.advpass()
        return self

class Employee:
        
    def new_phone():
        # phone = input("\nEnter your new phone number: ")
        phone = input(settings.config.NEW_PHONE)
        return phone
    
    def new_password():
        password = maskpass.advpass()
        return password
    
    def add_leave():
        #start_date = input("Enter start date in yyyy-mm-dd format: ")
        start_date = input(settings.config.LEAVE_START_DATE)
        #end_date = input("Enter end date in yyyy-mm-dd format: ")
        end_date = input(settings.config.LEAVE_END_DATE)
        return [start_date, end_date]
    
    def add_employee():
        #user_id = input("Enter the user_id: ")
        user_id = input(settings.config.EMPLOYEE_USERID)
        #name = input("Enter name: ")
        name = input(settings.config.EMPLOYEE_NAME)
        #username = input("Enter user name: ")
        username = input(settings.config.EMPLOYEE_USERNAME)
        leave = settings.config.TOTAL_LEAVES
        detail = {'user_id': user_id, 'Name': name, 'Username': username, 'leaves': leave}
        return detail
    
    def remove_employee():
        user_id = input("Enter the user_id: ")
        return user_id
    