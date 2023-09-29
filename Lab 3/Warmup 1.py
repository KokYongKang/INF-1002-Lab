# Question 1
# def division(x, y):
#   z = x/y
#  return z


# print(division(10,10))


# Question 2
# x = []

# for i in range(5):
#    z = input("Element: ")
#    x += [z]

# print(f"elements: {x}")

# Question 3 ( Else if change to elif )
# def printMax(a, b):
#    if a > b:
#        print(a, "is maximum")
#    elif a == b:
#        print(a, 'is equal to', b)
#    else:
#        print(b, 'is maximum')


# printMax('charlie', 'hello')


# Question 4 (message x 2 for hello while world x 5 )

# def say(message, times=2):
#    print(message*times)

# say('hello')
# say('world', 5)

# Question 5
# a is  3 and b is 7 and c is 10
# a is  25 and b is 5 and c is 24
# a is  100 and b is 5 and c is 50)
# def func(a, b=5, c=10):
#    print('a is ', a, 'and b is', b, 'and c is', c)


# func(3, 7) a is  3 and b is 7 and c is 10
# func(25, c=24) a is  25 and b is 5 and c is 24
# func(c=50, a=100) a is 100 and b is 5 and c is 50)

# Question 6
# def func(a, b, names):
#    a = a+10
#    b = b+20
#    names[0] = 12
#    names[1] = 18
#    return a, b


# x, y = 10, 30
# fruits = ["apple", "orange", "banana"]
# num1, num2 = func(x, y, fruits)
# print(num1, num2) # this will give u 20 50 as it only return a and b
# for fruit in fruits:
#    print(fruit) # this will give u 12 18 banana as fruits[0] and [1] have been modified

# question 8

def func(x):
    return x+5


print(func(20))

sorted(abs, ['00', '-800', '400', '200', '50'])

print(sorted)
