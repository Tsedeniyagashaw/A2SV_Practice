k, n, w = map(int, input().split())
 
sum = k * w * (w+1)//2
 
 
if sum > n:
   print(sum - n)
else:
   print(0)
