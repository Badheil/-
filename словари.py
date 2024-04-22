a = input().split(", ")
a = sorted(a)
d = {}
sorted_dict = {}
for el in a:
    d[el] = d.get(el, 0) + 1
sorted_values = sorted(d.values(), reverse= True)
print(sorted_values)
for i in sorted_values:
    for k in d.keys():
        if d[k] == i:
            sorted_dict[k] = d[k]
            break
p = 0
for k, v in sorted_dict.items():
    print("{}: {}".format(k, v))
    p +=1
    if p==3:
        break
