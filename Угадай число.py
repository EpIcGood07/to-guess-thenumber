import random

number = random.randint(1, 10)

i = 0

print("Угадай число от 1 до 10:)")
print("Будь осторожен! У тебя 5 попыток!")

while True:

    p = input("Угадай число: ")

    if p == "Выйти":
        print("Вы вышли из игры")
        break

    if not p.isdigit():
        print("Правильно введи число")
        continue

    if int(p) > number:
        print("Загаданое число меньше")
        i += 1
        print("Осталось ", (5 - i), "попыток")
    elif int(p) < number:
        print("Загаданое число больше")
        i += 1
        print("Осталось ", (5 - i), "попыток")

    if i == 5:
        print("Попытки кончились")
        break

    if int(p) == number:
        print("Как ты угадал?!")
        o = input("Не хочешь сыграть еще раз? ")
        if o == "да":
            if i > 0:
                i = 0
                number = random.randint(1, 10)
                continue
        elif o == "нет":
            print("Пока")
            break
