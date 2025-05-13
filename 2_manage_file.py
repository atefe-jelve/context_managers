""" 
    in this part we impelement a file manager for open and close our file
    in __exit__ the reason for return True is that for instance is , 
    we call a method that we dosent that the error python dosent show and we can handle it.

"""
class ManagerFile:
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None  # keep our conecction here for file

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()
        print(exc_type)
        print(exc_value)
        print(exc_tb)
        return True  # diactive errors in __exit__


with ManagerFile('file.txt', 'r') as f:
    for i in f:
        print(i)



