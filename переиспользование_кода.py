def get_balance(name=0, transactions=[]): # выводит int
    d ={}
    for i in range(len(transactions)):
        a= transactions[i].get("name") #Василий, Петя, Василий
        b= transactions[i].get("amount") #500, 100, -300
        if a in d.keys():
            d[a] += b
        else:
            d[a] = b
        print(d)
    s = 0
    for i in d.keys():
        if i == name:
            s = d[i]
    return s
    
def count_debts(names, amount, transactions):
    dict1 = {}
    # names = ["Василий", "Петя", "Вова"]
    for i in names: 
        if i not in dict1.keys():
            dict1[i] = get_balance(i, transactions)
    # dict1 = {'Василий': 200, 'Петя': 100, 'Вова': 0}
    money = 0
    for k, v in dict1.items():
        if v > amount:
            dict1[k] = 0
        else:
            dict1[k] = amount - v
    return dict1
    

transactions = [ 
{"name": "Василий", "amount": 500}, 
{"name": "Петя", "amount": -100}, 
{"name": "Василий", "amount": -300},
]

print(get_balance("Василий", transactions))

print(count_debts(["Василий", "Петя", "Вова"], 150, transactions))