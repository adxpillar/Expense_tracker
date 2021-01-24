class Expense():
    """
    Each record entry should have following attributes:
    * title (string)
    * amount (float)
    * created_at (date)
    * tags (list of strings)
    """
    def __init__(self,title,amount,created_at,tags):
        self.title = str(title)
        self.amount = float(amount)
        self.created_at = created_at
        self.tags = tags
    
    def __repr__(self):
        return "{self.__class__.__name__}({self.title},{self.amount},{self.created_at},{self.tags})".format(self=self)
    def __str___(self):
        return "Title: {self.title}, Amount:{self.amount}, Created_at:{self.created_at},Tags:{self.tags}".format(self=self)
