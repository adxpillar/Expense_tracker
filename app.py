from entry import Entry
from datetime import datetime 

def add_expense():
    """
    # adds an expense record using Entry class

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
        # write each record horizontally
        record = ','.join(map(str, [expense.title, expense.amount, expense.created_at, ' '.join(expense.tags)]))
        f.write(record + '\n')
        f.close()

def get_expense(search_term):
    """
    # search expense record through title
    args: title of expense
    returns: record

    """
    with open('expense.txt', 'r') as f:
        # read through each line in txt file to find search == result
        lines = f.readlines()
        found = None
        for line in lines:
            line = line.rstrip('\n').split(',')
            if line[0].lower() == search_term:
                found = line
        return found

def list_expense():
    """
    # list all expenses
    args: none
    return: none
    """
    with open('expense.txt', 'r') as f:
        list_all_expenses = f.readlines()
        for expense in list_all_expenses:
            print(expense)

def update_expense(search_term):
    """
    # update an expense
    args: search_term
    return: none 
    """
    # get title of record to edit
    record_to_edit = get_expense(search_term)
    # delete the record 
    delete_expense(search_term)
    # instruct 
    instruction = input('Enter "title" to edit title, "amount" to edit amount, and "tags" to edit tags: ').lower()
    new_title = new_amount = new_tags = None 
    if instruction == 'title':
        while not isinstance(new_title, str):
            new_title = input('Enter new title: ')
            record_to_edit[0] = new_title
    elif instruction == 'amount':
        while not isinstance(amount, float):
            new_amount = input('Update title: ')
            record_to_edit[1] = new_amount
    else:
        while not isinstance(tags, str):
            new_tags = input('Update tags: ').split()
            record_to_edit[3] = new_tags
    
    with open('expense.txt','a') as f:
        f.write(','.join(record_to_edit) + '\n')

def delete_expense(search_term):
    """
    # open the file and get all lines. Then reopen the file in write mode 
    # and write lines back, except for the line you want to delete:
    args: title of record
    return: none
    """
    result = []
    # read all records except 'column' title
    with open('expense.txt','r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.rstrip('\n').split(',')
            # check if first record == target
            if line[0].lower() == search_term:
                continue
            # else append all record to list 
            result.append(line)
    # write list into new txt file with 'columns'
    with open('expense.txt', 'w') as f:
        f.write('Title, Amount, Created_at,   Tags' + '\n')
        for line in result:
            f.write(','.join(line) + '\n')

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

    