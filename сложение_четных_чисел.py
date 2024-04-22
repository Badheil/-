summ = 0
input_number = "1"
while input_number != "":
    input_number = input()
    # if input_number != "":
    a = int(input_number)
    if a % 2 == 0:
        summ += a
    print(summ)