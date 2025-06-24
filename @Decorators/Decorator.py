#Decorator = A function that extends the behavior of another function w/o modifying the base function
#Pass the base function as an argument to the decorator

def add_more(fun):
    def wrapper(*args, **kwargs):
        print(f"Add more Cream!")
        fun(*args,**kwargs)
    return wrapper

def add_nuts(func):
    def wrapper(*args, **kwargs):
        print("Add More nuts to Cake!")
        func(*args, **kwargs)
        #print("Add More nuts to Cake!")
    return wrapper

@add_nuts
@add_more
def get_cake(flavor):
    print(f"Take your {flavor} cake!")

if __name__ == "__main__":
    get_cake("Chocolate")
    #get_cake("Vanilla")
    ##get_cake("Butterscotch")