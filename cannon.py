from prettytable import PrettyTable
import os


def choise():
    global ch
    print("1 - таблица задержки и дальности (ось Y)")
    print("2 - расчет выстрела по координатам")
    print("выберите действие: (1, 2)")
    ch = input()
    if ch == "1":
        print(table1)
        print()
        print("нажмите ENTER что бы очистить консоль")
        print("нажмите '1' что бы записать таблицу в файл (программа перезапустится)")
        ch = input()
        if ch == "1":
            file = open("table.txt", "w", encoding = "utf-8")
            file.write(str(table1))
            file.close()
        else:
            os.system("cls")
            choise()
    elif ch == "2":
        print("введите координату пушки (y) без минуса")
        xcord1 = input()
        print("введите координату пушки (x) без минуса")
        ycord1 = input()
        print("введите координату выстрела (y) без минуса")
        xcord2 = input()
        print("введите координату выстрела (x) без минуса")
        ycord2 = input()
        print()
        print("данные обработаны")
        print(f"координаты пушки (y x): {xcord1, ycord1}")
        print(f"координаты выстрела (y x): {xcord2, ycord2}")
        print()
        print("______________________________")
        print()
        xraz = int(xcord2) - int(xcord1)
        yraz = int(ycord2) - int(ycord1)
        print(f"разница координат (y x) = {xraz, yraz}")
        try:
            tickx = xraz/50
            tickx = round(tickx)
            tickx = yraz/tickx
            tickx = round(tickx)
            tickx *= 2

            while xraz%5 != 0:
                xraz -=1

            for i in range(54):
                if xraz == listb[i]:
                    ticky = lists[i-1]

            print(f"задержка по координате Y: {ticky}")
            print(f"задержка по координате X: {tickx}")
            print("______________________________")
            print()
            print("нажмите ENTER что бы очистить консоль")
            print("нажмите '1' что бы записать чек выстрела в файл (программа перезапустится)")
            ch = input()
            if ch == "1":
                file = open("check.txt", "w", encoding = "utf-8")
                file.write(f'''______________________________

координаты пушки (y x): {xcord1, ycord1}
координаты выстрела (y x): {xcord2, ycord2}

задержка по координате Y: {ticky}
задержка по координате X: {tickx}
______________________________
\n
''')
                file.close()
            else:
                os.system("cls")
                choise()
        except:
            print()
            print("данные неправильные, перепроверьте значения координат!")
            print()
            print("нажмите ENTER что бы очистить консоль")
            input()
            os.system("cls")
            choise()

        

lists = []
listb = []

n = 0
b = 3
c = 0
blocks = 0
for i in range (9):

    for i in range (3):
        lists.append(n)
        n += 2
    n -= 1
    for i in range (3):
        lists.append(n) 
        n += 1
    n = len(lists)
    for i in range(8):
        listb.append(130 + c)
        c += 5
    n += b
    b += 3


table1 = PrettyTable()
table1.field_names = ["тикиY", "блокиY"]
for i in range(50):
    table1.add_row([lists[i], listb[i]])




choise()
