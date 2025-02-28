#Check If a String Is a Palindrome

def palindrome(value):
    normal_string=value
    reverse=list(reversed(normal_string))
    reversed_string="".join(reverse)

    if normal_string==reversed_string:
        print(f"the given number {value} is Palindrome")
    else:
        print(f"The given number {value} is not palindrome")
#value=input("Enter value:- ")
#palindrome(value)


'''Reversed
Here reversed function  create list but it show only memory location. 
we use list to show elements 
after that we use ".join(variable)'''


def reversed_function(values):
    normal_string=values
    reversed_string=normal_string[::-1]
    if normal_string==reversed_string:
        print(f'{values} is palindrome')
    else:
        print(f'{values} is not palindrome')
#values=input("enter value:-")

reversed_function(values)


