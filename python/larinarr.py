a=[1,2,3,45,50,60,70]
#find the largest in array
max=a[0]
for i in range(1,len(a)):
    if a[i]>max:
        max=a[i]
print(max)
