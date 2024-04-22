import datetime
def gift_count(budget= 0, month= 1, birthdays= {}):
    d = {}
    sorted_dict= {}
    mas = []
    for i in birthdays.values():
        mas.append(i.day)

    mas = sorted(mas)
    for key, val in birthdays.items():
        if val.month == month:
            d[key] = val
    p = 0     
    for i in mas:
        for k in d.keys():
            if d[k].day == i:
                p = 1
                sorted_dict[k] = d[k]
    mas = sorted_dict.values()
    if p !=0:
        s = ", ".join('{} ({:02}.{:02}.{})' \
        .format(key, val.day, val.month, val.year)
        for key, val in sorted_dict.items())

        y = budget//len(mas)
        print("Именинники в месяце {}: {}. При бюджете {} они получат по {} рублей."\
        .format(month, s, budget, y))
                
    else:
        print("В этом месяце нет именинников.")

birthdays = {
    "Катя": datetime.date(1989, 1, 1), 
    "Ваня": datetime.date(1971, 1, 6),
    "Рахимджон": datetime.date(1965, 5, 6),
    "Орхузон": datetime.date(1999, 5, 30),
    "Галя": datetime.date(1971, 5, 25),
}

gift_count(3000, 5, birthdays)

birthdays = {
    "Иванов Иван Иванович": datetime.date(1989, 5, 1),
    "Петров Петр Петрович": datetime.date(1998, 5, 6)
}

gift_count(20000, 5, birthdays)

gift_count(budget=26300, month=5, birthdays=birthdays)

# print(f"Именинники в месяце {month}: {s}.
# При бюджете {budget} они получат по {budget//(len(mas))} рублей.")