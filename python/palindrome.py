s=input("Enter a string: ")
l=0
h=len(s)-1
while l < h:
    if s[l] != s[h]:
        print("Not a palindrome")
        break
    l=l+1
    h=h-1
else:
    print("Yes, it is a palindrome")
    
    