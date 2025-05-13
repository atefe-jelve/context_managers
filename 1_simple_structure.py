"""
    context managers use when we need do sothing befor and after a main process
    this is utilize manage sorces automaticaly, open and close file, connect and disconnect to database,
    in tests and manage lock in multithreading....
"""

class A:

    def __enter__(self):
        print("Do Befor ........")
        return(" extra things")

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Do After .........")


def show():
    print(" main task")

with A() as a:
    print(a)
    show()

"""
    in terminal we have this output:

    Do Befor ........
        extra things
        main task
    Do After .........

"""