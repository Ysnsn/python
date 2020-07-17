money=eval(input("请用户输入存款金额:"))
n=eval(input("请用户输入年限:"))
if n<5:
    rate=0.03
elif 5<=n<=8:
    rate=0.05
else:
    rate=0.07
money*=(1+rate)**n
print(money)
