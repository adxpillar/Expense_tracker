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
        CREATE TABLE Expenses (
        Title CHAR(20) NOT NULL,
        Amount FLOAT NOT NULL,
        Created_at CHAR(20) NOT NULL,
        Tags TEXT)
        '''

        try:
            self.cur.execute(''' DROP TABLE IF EXISTS Expenses''')
        except IndexError:
            print("Table not dropped or no such tables")
        finally:
            self.cur.execute(query)
        self.connection.commit()
        self.connection.close()
        return None 
    
    def save(self,expense):
        query = 
        '''
        INSERT INTO TABLE Expense (Title, Amount, Created_at, Tags) VALUES (?,?,?,?)
        ''',(expense.title,expense.amount,expense.created_at,expense.tags)
        try:
            self.cur.execute(query)
        except:
            print("Unable to save record")
        self.connection.close()

        

    def get_by_id(self,id):
        query = """
                SELECT * FROM Expenses
                WHERE "id" = ?
                """
        self.cur.execute(query,(id,))
        row = self.cursor.fetchall()
        self.connection.close()
        return row 

    def list_all_expense(self):
        query = """
                SELECT * FROM Expenses
                """
        self.cur.execute(query)
        rows = self.cur.fetchall()
        self.connection.close()
        return rows

    def delete_expense(self,id):
        query = """
                DELETE FROM Expenses
                WHERE "id" = ?
                """
        self.cur.execute(query,(id,))
        self.connection.close()
        return None 

if __name__ == "__main__":
    exp = Expense("Wholefoods", 45, "12/06/20", ["shopping", "bills","food"])
    exp2 = Expense("Tennis", 43.78, "12/07/20", ["sports", "leisure", "fitness"])
    print(exp)
    print(exp.__str__())
    print(exp.__repr__())

    print("Title:", exp.title)
    print("Amount:", exp.amount)
    print("Created_On:", exp.created_at)
    print("Tags:", exp.tags)


    print("Title:", exp.title)
    print("Amount:", exp.amount)
    print("Created_On:", exp.created_at)
    print("Tags:", exp.tags)

    er = ExpenseRepository
    er.AddExpense(exp)
    er.AddExpense(exp)
    er.EditExpense(exp2, 10)
    print(er.GetById(10))
    print(er.ListAll())
    er.Delete(11)
    er.Delete(10)