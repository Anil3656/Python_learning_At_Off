'''
In Python, a Context Manager is a construct that allows you to properly manage resources 
such as files, network connections, or database connections, ensuring that they are acquired and released cleanly, even if errors occur during their usage.'''

#A Context Manager is typically used with the `with` statement.
#The 'with' statement automatically handles setup and cleanup process.

#Context managers implement two magic methods

def __enter__():  #Sets up the context
    pass

def __exit__():   #Cleans up the context
    pass

#Examples:
'''with open('text.txt','w') as file:
    data = file.write("Hello every one!")
    
with open('text.txt','r') as file:
    data = file.read()
    print(data)'''
    
#In the above example:
    #->open() is the context manager.
    #->It opens the file (enter).
    #->Then closes it automatically when the block is exited (even if an error occurs).

# Built-in Context Managers in Python
'''
| Context Manager                                             | Description                                                          |
| ----------------------------------------------------------- | -------------------------------------------------------------------- |
| `open()`                                                    | Opens files and ensures they're closed properly                      |
| `threading.Lock()`                                          | Acquires and releases thread locks                                   |
| `decimal.localcontext()`                                    | Manages a local decimal context                                      |
| `suppress()` from `contextlib`                              | Suppresses specified exceptions                                      |
| `redirect_stdout()` / `redirect_stderr()` from `contextlib` | Redirects output to file or another stream                           |
| `tempfile.TemporaryFile()`                                  | Creates temporary files and deletes them when done                   |
| `fileinput.input()`                                         | Iterates over lines from multiple input streams                      |
| `os.scandir()`                                              | Used to iterate directory entries and ensures the iterator is closed |
| `contextlib.closing()`                                      | Closes anything with a `.close()` method                             |
| `contextlib.ExitStack()`                                    | Allows dynamic management of multiple context managers               |
'''

#Custom context manager
class MyContext:
    def __enter__(self):
        print("Entering")
        return self
    def __exit__(self,exc_type, exc_val, exc_tb):
        print("existing")

with MyContext():
    print("Inside")
    
#use @contextmanager from contextlib:
from contextlib import contextmanager

@contextmanager
def simple_cum():
    print("Enter")
    yield
    print("Exit")

with simple_cum():
    print("Inside")
    

#Temporary Suppression of Warnings or Errors
from contextlib import suppress

with suppress(Exception):
    z = 10 // 2
    print(z)
    print("Still Running!").__class__