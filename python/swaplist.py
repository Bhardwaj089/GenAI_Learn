#interchange first and last elements in a list

num = [1,2,3,4,5,6]

#num[0],num[-1] = num[-1], num[0]

#print("After swapping first and last elements:", num)

#using temp variable
def swaplist(num):
    n=len(num)
    temp=num[0]
    num[0]=num[n-1]
    num[n-1]=temp
    return num
print(swaplist(num))