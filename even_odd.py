
number=int(input())
def validate_even_not(number):
    if number%2==0:
        print(f"Successful - {number} is even number")
    else:
        print(f"failure - {number} is odd number")

validate_even_not(number)