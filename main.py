'''

Exercise 9b

Write a function that takes a list or tuple of numbers. Return the result of alter-
nately adding and subtracting numbers from each other. So calling the func-
tion as plus_minus([10, 20, 30, 40, 50, 60]) , you’ll get back the result of
10+20-30+40-50+60 , or 50 .

'''
def plus_minus(numbers):
    index = 0
    sum = 0
    for number in numbers:
        if index > 1 and index % 2 == 0:
            sum -= number
        else:
            sum += number
        index += 1
    return sum

print(plus_minus((1, 2, 3, 4, 5, 6)))