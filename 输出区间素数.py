def isPrime(num):#判断素数的方法
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True

    
lower=int(input("请输入区间最小数:"))
upper=int(input("请输入区间最大数:"))
if lower<=1 or upper<lower:
    print("输入有误!")
else:
    print("范围内的素数为:",end="")
    for n in range(lower,upper+1):
        if isPrime(n):
            print("{}".format(n))#print("{:5}".format(n),end="")不换行

                                                

