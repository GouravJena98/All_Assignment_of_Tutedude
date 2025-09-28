#Q1 --

n=int(input("Enter a number : "))
if n%2==0 : 
    print(f"{n} is Even number")
else:
    print(f"{n} is Odd number")
    
#Q2 --
sum=0
for i in range(1,51):
    sum+=i
print(f"The sum of number from 1 to 50 is : {sum}")