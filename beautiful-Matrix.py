arr = []
 
for i in range(5):
    arr.append(list(map(int, input().split())))
 
ones_position = []
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            ones_position = [i,j]
 
 
output = abs(ones_position[0] - 2) + abs(ones_position[1] - 2)
 
print(output)
