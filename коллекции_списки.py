a = []
b = []
for i in range(5):
    a.append(int(input()))
b = sorted(a, reverse= True)
for i in b:
    print(i)

# a = input().split()
# b = []
# for i in a:
#     b.append(int(i))
# c = sorted(b, reverse= True)
# print(" ".join(map(str, c)))