#生成杨辉三角
def yanghui(max):
    L=[1]
    n=0
    while n<max:
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(len(L)-1) ]+[1]
        n=n+1
a = yanghui(10)
for i in a:
    print(i)
