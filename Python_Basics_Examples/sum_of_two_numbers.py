#def sum_of_numbers(a, b):
   # print(f"enter first number: {a}")
   # print(f"enter second number: {b}")
   # sum=a+b
   # print(f"the sum of two numbers are: {sum}")

#sum_of_numbers(10,20)
def read_two_numbers():
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    return a, b

def substraction_of_two_numbers(a,b):
    sub=a-b
    return sub    

def addition_of_two_numbers(a,b):
    add=a+b
    return add


a, b=read_two_numbers()
sum = addition_of_two_numbers(a,b)
sub = substraction_of_two_numbers(a,b) 
print(f"the substraction of two numbers are: {sub}")
print(f"the addition of two numbers are: {sum}")
