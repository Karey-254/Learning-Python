#Local scope

#def my_func():
    #my_var = 10 # Locally scoped to my_func
    #print(my_var)

#my_func() # 10

#print(my_var) # NameError: name 'my_var' is not defined

#Enclosing scope
def outer_func():
    msg = 'Hello karey!'

    def inner_func():
        print(msg)

    inner_func()

outer_func() # Hello !Karey

#Enclosing Scope expounded

def outer_func():
    msg = 'Hello Karey-254!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you darling?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()

#Global Scope

my_var = 17

def show_var():
    print(my_var)

show_var() # 17
print(my_var) # 17