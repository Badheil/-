def lists_sum(*args, unique = False):
    ger = []
    for i in args:
        ger += i

    unique_list = []
    if unique:
        for i in ger:
            if i not in unique_list:
                unique_list.append(i)
                s = sum(unique_list)
        return s
    else:
       s = sum(ger) 
    return s
print(lists_sum([1, 2, 1, 2]))