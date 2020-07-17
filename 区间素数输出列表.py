def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True
ls=[]
n=int(input("请输入区间最小数"))
m=int(input("请输入区间最大数"))
for i in range(n,m+1):
    if isPrime(i):
        ls.append(i)
print(ls)
