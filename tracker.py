import math 
from datetime import datetime 


def expense_entry(amount: float, title: str, tags:[]):

    """
    add, list, get, edit, delete
    args: amount, title, date, tags
    returns: total expense 
    """

    entry = []

    # add pair of amount and title
    if amount > 0:

        # add date created

        created_at = datetime.today().strftime('%Y-%m-%d')
        amount = amount
        title = title
        # add tags 
        tags = tags

        entry.append(created_at)
        entry.append(amount)
        entry.append(title)
        entry.append(tags)


    else:
        print("Invalid amount")

    return entry

amount = float(input('amount: '))
title = input('what did you buy? ')
tags = input('tag this: ')

entry = expense_entry(amount,title,tags)


f = open('expense_report.txt', 'a')
f.write(str(entry))
f.close()

# get entry that's already in txt file 

def get_expense(search_term):
    result = []
    with open('expense_report.txt') as f:

        if any (search_term in i for i in f.read()):
            result.append(i)
        else:
            print('error')
            raise ValueError("Try another search term")
    
    print(result)

search_term = input('Enter search term: ')
search_op = get_expense(search_term)
print(search_op)


#  List expenses 
def list_expense():
    # result = []
    with open('expense_report.txt') as f:
        result = f.read()
    
    print(result)

list_expense()

# # delete entry 


