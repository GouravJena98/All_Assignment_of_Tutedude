import math 
#Q1 --

n=int(input("Enter a number : "))
#By Recursion method : 
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(f"The factorial of {n} by Recursion is : {fact(n)}")

#OR 

#By Looping Method : 
fact=1
for i in range(1,n+1):
    fact*=i
print(f"The factorial of {n} by Looping method is : {fact}")


#Q2 --

m=int(input("Enter a number : "))
print("The square root of is : {}".format(math.sqrt(m)))
print("The natural logarithm (log base e) of the number is ",math.log(m))
print("The logarithm of the number to base 10 is ",math.log10(m))
print("The logarithm of the number to base 2 is ",math.log2(m))
print("The sine of the number is ",math.sin(m))
