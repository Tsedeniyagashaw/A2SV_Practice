n = int(input())
a =[]
for _ in range(n):  
    size = int(input())
    a = list(map(int,input().split()))
    a.sort()
    one_left = True
    for i in range(1, size):
            if abs(a[i] - a[i-1]) > 1:
                one_left = False
                break
    if one_left:
        print("YES")  
    else:
        print("NO")  
