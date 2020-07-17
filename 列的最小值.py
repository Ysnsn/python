def imin(ls):
    n=ls[0]
    for m in ls:
        if n>m:
            n=m
    return n
ilist=[34,25,45,64,485,545,65]
print(imin(ilist))
