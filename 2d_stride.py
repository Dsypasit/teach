n = int(input())
a = [i for i in range(1,n+1)]
for i in range(n):
    for i in range(n):
        print(a[i],end=' ')
    c = a.pop()
    a.insert(0,c)
    print('')
