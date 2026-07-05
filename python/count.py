#count occurrence of numbers in a list

a=[10,10,20,30,40,10,10,50,10,10,60,70,80,90,100] 
count=0  

for val in a:
    
    if val==10:
        count+=1
        
print("10 occurs",count,"times")
    
    