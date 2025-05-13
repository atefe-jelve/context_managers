"""
    here we use `contectlib` module that provide use context managers easily for small things
"""

import contextlib

@contextlib.contextmanager
def show(name):
    print("Starting Context MAnager...", name) # work as  __enter__
    yield {} # just use one time and empty yield
    print("Ending Context MAnager ...", name) # woek as __exit__

with show('Atefe') as s, show('sara') as a, show('john') as j:
    print("Hello")

"""
    out put for this code:

    Starting Context MAnager... Atefe
    Starting Context MAnager... sara
    Starting Context MAnager... john
    Hello
    Ending Context MAnager ... john
    Ending Context MAnager ... sara
    Ending Context MAnager ... Atefe

    - attention to order of output for __enter__ and __exit__
"""