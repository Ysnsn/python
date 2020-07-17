def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True
def  mean(ls):
    s = 0.0
    for i in ls:
        s+=i
    return s/len(ls)
vls=[]
lower=eval(input("请输入一个大于二的整数:"))
upper=eval(input("请输入一个整数:"))
for i in range(lower,upper):
    if isPrime(i):
        vls.append(i)
print(vls)
print("平均值为{}".format(mean(vls)))
