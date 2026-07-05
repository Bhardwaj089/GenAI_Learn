#largest and smallest number in list
a=[10,20,30,40,50,60]

largest = a[0]
smallest = a[0]

for i in range(1,len(a)):
    if a[i] > largest:
        largest = a[i]
    if a[i] < smallest:
        smallest = a[i]

print("largest number is:", largest)
print("smallest number is:", smallest)
        
        
    