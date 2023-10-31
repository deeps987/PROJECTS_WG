import random
from datetime import date
from models.db import DbConnect
from utils.log import Log
from utils.validation import Validation
from utils.input import Employee
from datetime import date,datetime
import utils.queries 
from prettytable import PrettyTable

class Employee:
    def __init__(self):
        self.userid = None
        self.name = None
        self.username = None
        self.leave = 0
        self.role = None
        
            
    def view_details(self):
        details = Employee._view_detail_(self)
        details = details[0]
        if details:
            table = PrettyTable()
            table.field_names = ["Name", "Designation", "Phone", "Number of leaves"]
            table.add_row([details["Name"], details["Designation"], details["Phone"], details["Total Leaves"]])
            table.align = "l"
            table.max_width["Type"] = 15
            table.max_width["Date/Time"] = 19    
            print("The details are : ")
            print(table)

    
    def _view_detail_(self):
        result = DbConnect.cursor_employee(utils.queries.VIEW_DETAIL, self.user_id)
        result = [{
                'Name': row[1],
                'Designation': row[2],
                'Phone': row[3],
                'Total Leaves': row[4]
            } for row in result]
        return result
    
    
    def change_phone(self, new_number):
        Employee._change_phone(self, new_number)
        print("\nPhone number changed successfully!\n")
        Log.change_phone(self)
    
    def _change_phone(self, new_number):
        DbConnect.cursor_employee(utils.queries.CHANGE_PHONE, new_number, self.user_id)
    
    
    def change_password(self, new_password):
        Employee._change_password(self, new_password)
        print("\nPassword changed successfully!\n")
        Log.change_password(self)
        
    def _change_password(self, new_password):
        DbConnect.cursor_employee(utils.queries.CHANGE_PASSWORD, new_password, self.user_id)
    
    
    def add_leave(self):
        date = Validation.check_date_format()
        Employee._add_leave(self, date)
        print("\nLeave added successfully!\n")
        Log.add_leave(self)
        
    def _add_leave(self, date):
        leave_id = random.randint(0, 10**9)
        DbConnect.cursor_employee(utils.queries.ADD_LEAVE, leave_id, self.user_id, date[0], date[1], "Pending")

    
    def add_attendance(self):
        Employee._add_attendance(self)
        print("\nAttendance added successfully!\n")
        
    def _add_attendance(self):
        attendance_id = random.randint(0, 10**9)
        marked_at = date.today()
        DbConnect.cursor_employee(utils.queries.ADD_ATTENDANCE, attendance_id, self.user_id, marked_at)
        
        
    def add_employee(self, role):
        details = Validation.check_input_details()
        if role == 'Manager':
            details['Designation'] = 'Employee'
        else:
            details['Designation'] = 'Manager'
        details['Role'] = role
        Employee._add_employee(details)
        print("Employee added successfully!\n")
        Log.add_employee(details)
    
    def _add_employee(self):
        unique_id = random.randint(0, 10**9)
        DbConnect.cursor_employee(utils.queries.INSERT_AUTHENTICATION,
                self['user_id'], self['Username'], self['Password'])
        DbConnect.cursor_employee(utils.queries.INSERT_EMPLOYEE,
                self['user_id'], self['Name'], self['Designation'], self['Phone'], self['leaves'])
        DbConnect.cursor_employee(utils.queries.INSERT_RELATIONSHIP,
                unique_id, self['user_id'], self['Role'])
        

    def remove_employee():
        user_id = Validation.check_input_id()
        Employee._remove_employee(user_id)
        print("\nUser removed successfully!\n")
        Log.remove_employee(user_id)
            
    def _remove_employee(user_id):
        DbConnect.cursor_employee(utils.queries.DELETE_AUTHENTICATION,
                user_id, )
        DbConnect.cursor_employee(utils.queries.DELETE_EMPLOYEE,
                user_id, )
        DbConnect.cursor_employee(utils.queries.DELETE_RELATIONSHIP,
                user_id, )    
        return
    
    
    def view_attendance(self):
        details = Employee._view_attendance(self)
        if details:
            table = PrettyTable()
            table.field_names = ["User id", "Name"]
            for detail in details:
                table.add_row([detail[0], detail[1]])
            table.align = "l"
            table.max_width["Type"] = 15
            table.max_width["Date/Time"] = 19    
            print(table)
        print('\n')
    
    def _view_attendance(self):
        return(DbConnect.cursor_employee(utils.queries.VIEW_ATTENDANCE,
                self.user_id,))

    
    def view_leave(self):
        leave = Employee._get_leave_details(self)
        if leave:
            table = PrettyTable()
            table.field_names = ["User id", "Start Date", "End Date"]
            for li in leave:
                table.add_row([li[0], li[1], li[2]])
            table.align = "l"
            table.max_width["Type"] = 15
            table.max_width["Date/Time"] = 19    
            print(table)
        print('\n')
    
        # for date_tuple in leave:
        #     print(date_tuple)
            
        for item in leave:
            user_id, start_date, end_date = item
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            delta = end_date - start_date
            number_of_days = delta.days
            
            total_leaves_remaining = Employee._get_leaves_remaining(user_id)
            
            status = Employee._get_status_(number_of_days, total_leaves_remaining)
            
            Employee._enter_leave_status(user_id, status)
            
            if status == 'Approved':
                Employee._update_leave(user_id, total_leaves_remaining - number_of_days)
        
        print('Status updated!\n')
    
    def _get_leave_details(self):
        return(DbConnect.cursor_employee(utils.queries.GET_LEAVE_DETAILS,
                self.user_id,))    

    def _get_leaves_remaining(user_id):
        return(DbConnect.cursor_employee(utils.queries.GET_LEAVES_REMAINING,
                user_id,))[0][0] 
    
    def _enter_leave_status(user_id, status):
        return(DbConnect.cursor_employee(utils.queries.ENTER_LEAVE_STATUS,
                status, user_id))    
    
    def _update_leave(user_id, days):
        return(DbConnect.cursor_employee(utils.queries.UPDATE_LEAVE,
                days, user_id))
    
    def _get_status_(number_of_days, total_leaves_remaining):
        if(number_of_days < total_leaves_remaining):
            return 'Approved'
        return 'Rejected'
