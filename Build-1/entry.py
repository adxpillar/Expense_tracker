class Entry():
    """
    Each record entry should have following attributes:
    * title (string)
    * amount (float)
    * created_at (date)
    * tags (list of strings)
    """
    def __init__(self,title,amount,created_at,tags):
        self.title = title
        self.amount = amount
        self.created_at = created_at
        self.tags = tags
