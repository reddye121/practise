a=int(input("first number: "))
b=int(input("second number: "))
c=int(input("final number: "))
def largest(a,b,c):
    if a>b and a>c:
        print(f"a: {a} is largest number")
    elif b>a and b>c:
        print(f"b: {b} is largest number")
    else:
        print(f"c: {c} is largest number")
largest(a,b,c)