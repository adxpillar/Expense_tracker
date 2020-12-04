import math 
from datetime import datetime 

total_expense = []

def expense_entry(amount: float, title: str, tags:[]):

    """
    add, list, get, edit, delete
    args: amount, title, date, tags
    returns: total expense 
    """

    entry = []
    expense = {}

    # add pair of amount and title
    if amount > 0:
        expense[title] = amount
        # add date created
        created_at = datetime.today().strftime('%Y-%m-%d')
        # add tags 
        tags = tags

        entry.append(created_at)
        entry.append(tags)
        entry.append(expense)

    else:
        print("Invalid amount")

    return entry 

amount = float(input('amount: '))
title = input('what did you buy? ')
tags = input('tag this: ')


print(expense_entry(amount,title,tags))

# get entry that's already in txt file 
# def get_entry()

# delete entry that's already 

