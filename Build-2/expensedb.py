import os 
import sqlite3
from expense import Expense

expense = Expense()

class ExpenseRepository():

    def __init____(self):
        self.connection = sqlite3.connect('./db.sqlite3')
        self.cur = self.connection.cursor()
    
    def createTable(self):
        query = 
        '''
        CREATE TABLE Expense (
        Title CHAR(20) NOT NULL,
        Amount FLOAT NOT NULL,
        Created_at CHAR(20) NOT NULL,
        Tags TEXT)
        '''

        try:
            self.cur.execute(''' DROP TABLE IF EXISTS Expense''')
        except IndexError:
            print("Table not dropped or no such tables")
        finally:
            self.cur.execute(query)
    
    def save(self):
        query = 
        '''
        INSERT INTO TABLE Expense (Title, Amount, Created_at, Tags) VALUES (?,?,?,?)
        ''',(expense.title,expense.amount,expense.created_at,expense.tags)
        try:
            self.cur.execute(query)
        except:
            print("Unable to save record")
        

    def get_by_id():
        pass

    def list_expense():
        pass

    def delete_expense(sefl):
        pass