ls=[7,4,5,2,3,5,6]
print("列表为",end="")
print(ls)

print("列表长度为{}".format(len(ls)))
print("列表中有{}个5".format(ls.count(5)))

print(ls[1:5:2])

new=eval(input("请输入一个新的元素:"))
ls.append(new)

ls[3:5]=[11,12,13]

print("列表为",end="")
print(ls)

print("列表中的最大值为:{}".format(max(ls)))
print("列表中的最小值为:{}".format(min(ls)))

n=eval(input("请输入要删除的元素符号:"))
del ls[n]

print("列表为",end="")
print(ls)
ls=sorted(ls,reverse=True)
print(ls)
ls=sorted(ls,reverse=False)
print(ls)
