def func(num1,num2):
    m=max(num1,num2)
    n=min(num1,num2)
    r=m%n
    while r!=0:
        m=n
        n=r
        r=m%n
    return n
m=eval(input("请输入第一个数:"))
n=eval(input("请输入第二个数:"))
print("{}和{}的最大公约数为{}".format(m,n,func(m,n)))
