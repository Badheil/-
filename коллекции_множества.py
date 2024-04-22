a = input().lower().split(", ")
a = sorted(a)
b = []
for word in a:
    if word not in b:
        b.append(word)        
string = ", ".join(b)
print(string)