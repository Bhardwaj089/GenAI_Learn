num = [10,20,45,9,15,25]

maximum= num[0]
minimum= num[0]
for value in num:
    if value > maximum:
        maximum=value
    if value < minimum:
        minimum=value       
        

print("largest number is:", maximum)
print("smallest number is:", minimum)


