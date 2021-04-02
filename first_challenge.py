from random import randint
import math

list_of_all = []

n = int(input('Введите количество точек (только целое число)'))

#создаем наши точки

for i in range(n):
    x = randint(-100,100)
    y = randint(-100,100)
    new_list = [x, y]

    list_of_all.append(new_list)
#сортировать будем по углу от оси х, тут тригонометрия, считаем арктангенс, переводим радианы в угол

def sort_key(some_list):
    if some_list[0] > 0 and some_list[1] > 0:
        angle = 360 + math.degrees(math.atan2(some_list[1], some_list[0]))
    elif some_list[1] <= 0:
        angle = 360 + math.degrees(math.atan2(some_list[1],some_list[0]))
    else:
        angle = math.degrees(math.atan2(some_list[1],some_list[0]))
    return angle

list_of_all = sorted(list_of_all, key = sort_key)

#самая последняя точка в конце списка,если она из первой четверти, будет самой ближайщей к оси игрек, если она есть, перекину ее в начала списка
if list_of_all[-1][1] > 0:
    new_new_list = []
    last_position = list_of_all[-1]

    new_new_list.append(last_position)
    new_new_list = new_new_list + list_of_all
    list_of_all.clear()
    list_of_all = new_new_list
    del list_of_all[-1]

#считаю расстояние от нуля до точки

list_of_gipotenusa = []
all_gipotenusas = 0
for elem in list_of_all:
    gipotenusa = math.sqrt(elem[0]**2 + elem[1]**2)
    list_of_gipotenusa.append(gipotenusa)
    all_gipotenusas += gipotenusa

#ввывожу мин и макс, среднюю длину
print("MIN ", min(list_of_gipotenusa))
print("MAX ", max(list_of_gipotenusa))
print("Arithmetic mean ", all_gipotenusas / n)


