def Func(num):
    s=1
    for i in range(1,num+1):
        s=s*i
    return s
n=int(eval(input("请输入一个整数:")))
print("n的阶乘为{}".format(Func(n)))
