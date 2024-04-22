# Напишите функцию mean_age(json_string), которая принимает json строку,
# считает средний возраст людей из входных данных и возвращает новую
# json-строку в том формате, который указан ниже.
# {"mean_age": 23.5}
import json
def mean_age(json_string):
    f = json.loads(json_string)
    age_list = []
    d = {}
    for i in f:
        age_list.append(i["age"])
    mid_age = sum(age_list)/len(age_list)
    d["mean_age"] = mid_age
    json_dict = json.dumps(d)
    return json_dict
print(mean_age(('[ \
    {"name": "Петр", "surname": "Петров", "patronymic": "Васильевич", "age": 23, "occupation": "ойтишнек"}, \
    {"name": "Василий", "surname": "Васильев", "patronymic": "Петрович", "age": 24, "occupation": "дворник"} \
]')))
