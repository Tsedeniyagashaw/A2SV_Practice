n,k = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
res = []
i =0
j =0
smaller = []
count = 0

while i < len(arr1) and j < len(arr2):    
    if arr2[j] > arr1[i]:
        count += 1
        i += 1
    else:        
        smaller.append(count)             
        j += 1 
while j < len(arr2):
    smaller.append(count)
    j += 1                  
print(*smaller)         
