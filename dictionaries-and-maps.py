n = int(input())
dict = {}

for i in range(n):
    a, b = input().split()
    dict[a] = b

for i in range(n):
    name = input()
    if name in dict:
        print(name + "=" + dict[name])
    else:
        print("Not found")
