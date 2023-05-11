

# Write a Python program that takes a list of strings as input 
# and outputs the number of times each string appears in 
# the list, using a dictionary and conditional statements.


def count_strings(lst):
    form_dict = {}
    for string in lst:
        if string in form_dict:
            form_dict[string] += 1
        else:
            form_dict[string] = 1
    return form_dict
my_list = ["pineapple", "banana", "apple", "mellon", "banana", "apple"]
print(count_strings(my_list))  

# Write a Python program that takes a list of numbers as input and outputs the median of the numbers 

def find_median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        median = (lst[n//2-1] + lst[n//2]) / 2
    else:
        median = lst[n//2]
    return median

my_list = [1, 3, 5, 8, 9]
print(find_median(my_list)) 

# Write a Python program that takes a list of numbers as input 
# and outputs the second largest number in the list using conditional statements and a for loop.


def find_second_largest(lst):
    largest = second_largest = lst[0]
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest


my_list = [10, 5, 15, 20, 7, 3, 8]
print(find_second_largest(my_list)) 

# Write a Python program that takes a year as input and determines if it is a leap year.

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2000))