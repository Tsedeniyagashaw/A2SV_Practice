n = int(input())
arr = list(map(int,input().split()))

all_same_parity = True

first_parity = arr[0] % 2

for i in range(n):
    if arr[i] % 2 != first_parity:
        all_same_parity = False
        break
if not all_same_parity:
    arr.sort()

print(*arr)
