s=input("输入一个字符串")
count1=0
count2=0
count3=0
count4=0
for c in s:
    if 65<=ord(c)<=90 or 97<=ord(c)<=122:#大写 小写
        count1+=1
    elif 48<=ord(c)<=57:#数字
        count2+=1
    elif ord(c)==32:#空格
        count3+=1
    else:
        count4+=1
print("字符串中有{}个字母,{}个数字,{}个空格,{}个其它字符".format(count1,count2,count3,count4))
