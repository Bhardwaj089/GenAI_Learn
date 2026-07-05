num = [10,20,45,9,15,25]

max= a[0]
min= a[0]

for i in a:
    if a[i] > max:
        max=a[i]
    if a[i] < min:
        min=a[i]        
        

print("largest number is:", max)
print("smallest number is:", min)


