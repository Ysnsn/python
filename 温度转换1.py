#符号值在前的温度转换
Tempstr=input("请输入温度值")
if Tempstr[0] in ['f','F']:
    c=(eval(Tempstr[1:])-32)/1.8
    print("转换后的温度是C{:.2f}".format(c))
elif Tempstr[0] in ['C','c']:
    f=1.8*eval(Tempstr[1:])+32
    print("转换后的温度为F{:.2f}".format(f))
else:
    print("输入格式错误，请重新输入。")
