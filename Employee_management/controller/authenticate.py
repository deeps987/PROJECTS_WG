from utils.input import AuthDetails
from models.db import DbConnect
from views.menu import Menu
import utils.queries 

class Authentication:
    
    def login(self):
        while True:
            credentials = AuthDetails()
            details = credentials.auth_login()
            if Authentication.check_credentials(details):
                print("Login successfull. Welcome to your page!\n")
                role = Authentication.check_role(details)
                flag = True
                break
            else:
                print("\nIncorrect credentials! Please Try again.\n")
        
        if flag == True:
            if role == 'Employee':
                Menu.employee_menu(details)
            elif role == 'Manager':
                Menu.manager_menu(details, role)
            else:
                Menu.manager_menu(details, role)

    
    def check_credentials(credentials):
        return DbConnect.cursor_auth(utils.queries.CHECK_CREDENTIALS, credentials.user_id, credentials.password)   

    
    def check_role(self):
        result = DbConnect.cursor_auth(utils.queries.CHECK_ROLE, self.user_id)
        return result[0]
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            

    
    
    
    

    
        