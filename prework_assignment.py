# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")

hello_name('marianne')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.


def first_odds():
    for value in range(1, 100):
        if value % 2 == 1:
            print(value)
       

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 

def max_num_in_list(a_list):
    max = a_list[0]
    for x in a_list:
        if x > max:
            max = x
    return max

a_list = [1, 2, 3, 4, 5]
print(max_num_in_list(a_list))

# Question 4
# Write a function to return if the given year is a leap year. The return should be booelean Type.

def is_leap_year(a_year):

    if a_year % 4 == 0 and a_year % 100 !=0 or a_year % 400 == 0:
        print(bool(a_year))
    else:
        print("False")

is_leap_year(2050)

# 5 Question
# Write a function to check to see if all numbers in list are consecutive numbers. For example, 
# [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    a_list = sorted(a_list)
    if a_list:
        return a_list == list(range(a_list[0], a_list[-1] + 1))
    else:
        return True

a_list = [1, 2, 3, 4, 5, 7, 8]
print(is_consecutive(a_list))