import math
n=input("Enter a number: ")
if n<=1:
    print("Not Prime")
else:
    is_prime=True
    for i in range(2,n+1):
        if n%i==0:
            break
    print(is_prime)
    
    