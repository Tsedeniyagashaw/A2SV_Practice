n, t = map(int,input().split())
arr = list(map(int,input().split()))

sum = 0
count = 0
i = j = 0
while i < n and j < n:
    sum = sum + arr[i]
    if sum <= t:
        count += 1
    else:
        sum = sum - arr[j]
        j += 1
    i += 1
print(count)            
