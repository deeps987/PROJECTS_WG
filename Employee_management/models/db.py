import sqlite3

class DbConnect:
    def __init__(self):
        pass

    def __enter__(self):
        self.connection = sqlite3.connect('Employee.db')
        cursor = self.connection.cursor()
        return cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        
    def cursor_auth(query, *self):
        with DbConnect() as cursor:
            cursor.execute(
                query,
                (self))
            result = cursor.fetchone()
            return result
        
    def cursor_employee(query, *self):
        with DbConnect() as cursor:
            cursor.execute(
                query,
                (self))
            result = cursor.fetchall()
            return result
        
    
