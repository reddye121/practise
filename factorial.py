def factorial(number):
    factorial_number=1
    for i in range(1, number+1):
        factorial_number*=i
    print(factorial_number)
number=int(input("Entervalue:-"))
factorial(number)

