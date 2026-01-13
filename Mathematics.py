my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1
print('modular integers:',  mod_ints ) # divides two numbers from the left to right
print('modular float:', mod_floats)
print('answer:', mod_ints * mod_floats)
print('Exponential:',mod_ints ** mod_floats ) 
print('floor:', mod_floats // mod_ints) # gives an integer equal to or less than the highest integrer

# Problem 2
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2
print('exponential integer:',exp_ints)
print('exponential float:',exp_floats)
print('floor int:',my_int_1 //my_int_2) #floor it
print('Modulo int:', my_int_1 % my_int_2) #Modulo it

# Problem 3 augemented
my_var = 10
my_var += 5
print(my_var)
print(my_var + 10)
print(my_var / 5)

# Problem 4 augemented
my_var = 113
my_var_1 = 10
print(my_var)
print(my_var + 10)
print(my_var / 5)
print(my_var // my_var_1) #flooring


#agumented addition
my_var = 10
my_var += 5 #put the operation before the = sign to avoid repetition
print(my_var)


#agumented substration
count = 14
count -= 3  # Right from the left
print(count)


#agumented multiplication
product = 65
product *= 7 #left variable with the rigt
print(product)


#agumented division
price = 100
price /= 4 #divides the left variable by the right
print(price)


#agumented modulo
bits = 35
bits %= 2 # computes the reminder of the left variable divided by the right
print(bits)


#agumented floor
total_pages = 23
total_pages //= 5 # divides the left variable by the right and puts the answer to the left
print(total_pages)


#agumented exponential
power = 2
print(power)

#agumented strings
greet = 'Hello'
greet += 'world'
print(greet)

#Boolean
print(17 > 22) # False
print(17 < 22) # True
print(17 == 22) # False
print(22 == 22) # True
print(17 != 22) # True
print(17 >= 22) # False
print(17 <= 22) 

#agumented division review

price = 15000000
price /= 100 #divides the left variable by the right
print(price)

price = 10000000000
price /= 1000

print(price)

purpose = 14000
purpose *= 100
print(purpose)