def InputNumbers(inputText):
    good = False
    while not good:
        try:
            number = float(input(f"{inputText}"))
            good = True
        except ValueError:
            print("не")
    return number

def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")