def isNum(str):
    try:
        if type(eval(str)) in [type(3),type(3.0),type(1+2j)]:
            return True
        else:
            return False
    except:
        return False
s=input("请输入一个字符串:")
print("这个字符串是数值型的吗？",end="")
print(isNum(s))
