def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True
lower=int(input("请输入区间最小数:"))
upper=int(input("请输入区间最大数:"))
s=0
if lower<=1 or upper<lower:
    print("输入有误:")
else:
    for n in range(lower,upper+1):
        if isPrime(n):
            s=s+n
    print(s)
         

