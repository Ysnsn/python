sum=0
for num in range(2,101):
    for i in range(2,num):
        if num % i ==0:
            break
    else:
        sum+=num
print(sum)
