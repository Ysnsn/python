print("这是一个三人规模的《逢\'7\'拍腿》的小游戏(即遇到7的倍数或个位为7的数就拍腿一次)，接下来开始游戏。")
counta=1
while counta>0:
    ref=input("确认次数范围。请输入数值范围的最后一个整数，已默认由1开始：")
    ref=int(ref)
    if ref>0:
        counta=0
        countb=1
        while countb>0:
                num = input("确认结束时拍数。请输入你刚才设置区域内的一个整数，以其作为游戏结束时的数值：")
                num = int(num)
                if num in range(1, ref+1):
                    countb=0
                    countc=1
                    while countc>0:
                        role = input("请选择一个角色。第1位开始的a，第二位开始的b，第三位开始的c：")
                        if role in ("a","b","c"):
                            countc=0
                            sum=0
                            if role=="a":
                               numa=1
                               while numa<=num:
                                       if numa % 7 == 0 or numa % 10 == 7:
                                           sum += 1
                                       numa+=3
                            if role=="b":
                                numb=1
                                while numb<=num:
                                    if numb % 7 == 0 or numb % 10 == 7:
                                        sum+=1
                                    numb+=3
                            if role == "c":
                                numc = 1
                                while numc <= num:
                                    if numc % 7 == 0 or numc % 10 == 7:
                                        sum += 1
                                    numc += 3
                        else:
                            countc+=1
                else:
                    countb+=1
 
    else:
        counta+=1
print("你选择的角色%s最终拍腿次数为%d，游戏结束！" % (role, sum))