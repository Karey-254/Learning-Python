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