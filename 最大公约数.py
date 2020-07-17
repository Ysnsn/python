num1=eval(input("请输入第一个数:"))
num2=eval(input("请输入第二个数:"))
m=max(num1,num2)
n=min(num1,num2)
r=m%n
while r!=0:
    m=n
    n=r
    r=m%n
print(n)
