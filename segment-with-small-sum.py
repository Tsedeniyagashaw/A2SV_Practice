n,s = map(int,input().split())
arr = list(map(int,input().split()))
l = 0
r = 0
segment = 0
summ = 0
for r in range(n):
    summ += arr[r]
    while summ > s:
        summ  -= arr[l]
        l += 1
    segment =  max(segment, r - l + 1)
print(segment)            
