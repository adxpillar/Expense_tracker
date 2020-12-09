from entry import Entry
from datetime import datetime 

def add_expense():
    """
    adds an expense record using Entry class

    args: none
    returns: none 
    """
    title = amount = tags = None
    # validate input type
    while not isinstance(title, str):
        title = input('Enter expense title: ')
    while not isinstance(amount, float):
        amount = float(input('Enter amount: '))
    while not isinstance(tags, str):
        tags = input("Tag this record. Separate tags by comma: ")

    created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    # make expense entry
    expense = Entry(title, amount, created_at, tags.split(','))

    # write record to txt file
    with open('expense.txt','a') as f:
        record = ','.join(map(str, [expense.title, expense.amount, expense.created_at, ' '.join(expense.tags)]))
        f.write(record + '\n')
        f.close()


# get entry that's already in txt file 

# def get_expense(search_term):
#     result = []
#     with open('expense_report.txt') as f:

#         if any (search_term in i for i in f.read()):
#             result.append(i)
#         else:
#             print('error')
#             raise ValueError("Try another search term")
    
#     print(result)

# search_term = input('Enter search term: ')
# search_op = get_expense(search_term)
# print(search_op)


#  List expenses 
# def list_expense():
#     # result = []
#     with open('expense_report.txt') as f:
#         result = f.read()
    
#     print(result)

# list_expense()

def update_expense():
    pass

def delete_expense():
    pass

# # delete entry 


if __name__ == "__main__":
    while True:
        print('Enter: "add" to add an expense \n enter "list" to list your expenses')
        print('Enter: "edit" to edit an expense \n enter "get" to get an expense by title')
        print('Enter: "delete" to delete an expense \n enter "exit" to close ledger')
        # select action to take on your expense record
        # CRUD flow 
        main = input('What would you like to do today?: ').lower()
        # exit 
        if main == "exit":
            break
        # Take other CRUD actions
        if main == "delete" or main == "edit" or main == "get":
            # enter a search term to be able to delete, update, or get a record 
            search_term = input("Enter search term: ").lower()
            #  check for non-existing record first
            if not get_expense(search_term): 
                print("We don't have that record")
                # move own to delete, update, or get a record  
            else:
                # delete
                if main == "delete":
                    delete_expense(search_term)
                    # update
                elif main == "edit":
                    update_expense(search_term)
                    # read 
                else:
                    print(get_expense(search_term))
        # read all records
        if main == "list":
            list_expense()
            # create new record 
        elif main == "add":
            add_expense()

    