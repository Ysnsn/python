def mean(ls):
    s=0.0
    for i in ls:
        s=s+i
    return s/len(ls)
score={"Mary":87,"Tom":42,"Amy":98,"Gavin":100,"Pual":77}
m="Mary"
for dd in score.keys():
    if score[m]<score[dd]:
        m=dd
print(m,score[m])
print("平均值为{:.2f}".format(mean(score.values())))
