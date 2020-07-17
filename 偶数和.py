def func(n):
    s=0
    for i in range(2,n+1,2):
        s=s+i
    return s
n=int(eval(input("请输入一个整数:")))
print("1到{}的偶数和为{}".format(n,func(n)))
