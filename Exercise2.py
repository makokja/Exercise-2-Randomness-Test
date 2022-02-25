import random

def get_numbers():
    #get the random 10 numbers between 1 and 50 and sort by ascending
    numbers = random.sample(range(1, 50), 10)   #are the numbers should be unique? I use random.sample for this
    numbers.sort()
    return numbers

#calling get_number function and print out the result
result = get_numbers() 
print(result)

#  unit tests I could implement
#  1. test to see if the output is between 1-50 and actually 10 numbers
#  2. test if the result is return in list format and in ascending order