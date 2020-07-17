count={"Upper":0,"Lower":0,"Num":0,"Others":0}
s=input("请输入一个字符串")
for p in s:
    if p.isupper():
        count["Upper"]+=1
    elif p.islower():
        count["Lower"]+=1
    elif p.isnumeric():
        count["Num"]+=1
    else:
        count["Others"]+=1
print(count)
