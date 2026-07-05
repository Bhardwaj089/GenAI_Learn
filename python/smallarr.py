a=[10,30,40,50,60]
#print smallest in array
min=a[0]
for i in range(1,len(a)):
    if a[i]<min:
        min=a[i]
    
print(min)