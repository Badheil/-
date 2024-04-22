    # Считывает файл, в котором в каждой строке
    # записаны имена и фамилии через пробел
    # нужно вернуть строку - самое популярное имя в файле
    # Если их несколько то перечислить
    # через запятую в алфавитном порядке 

    # f = open(filename, encoding="utf8")

def get_popular_name_from_file(filename):

    with open(filename, encoding="utf8") as f:
        a = []
        d = {}
        sorted_dict = {}
        name_list = (f.read().split("\n"))
        ind = 0

        for i in name_list:
            for j in i:
                if j == " ":
                    ind = i.index(j)
                    a.append(i[0:ind])

        for el in a:
            d[el] = d.get(el, 0) + 1
        max_num = max(d.values())
        yt = sorted(d.keys())

        for i in yt:
            for k in d.keys():
                if k == i:
                    sorted_dict[k] = d[k]
        d.clear()

        for key in sorted_dict.keys():
            if sorted_dict[key] == max_num:
                d[key] = max_num

        str_names = sorted(d.keys())
        s = ", ".join(str_names)
    return s

print(get_popular_name_from_file("names.txt"))