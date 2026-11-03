import random
a = sorted(random.sample(range(0, 333), 101))#список для поиска
b=int(input("Введите число "))#что ищем
c = len(a)
d = 0#счётчик сравнений
e = -1
print("начальный список: ", a)
print("ЛИНЕЙНЫЙ ПОИСК:")
for i in range(c):#идём по списку
    d += 1
    if b == a[i]:
        e = i#нашли — запомнили
        break
if b == a[e]:
    print("индекс элемента: ", e)
    print("количество сравнений: ", d)
else:
    print("число не найдено")

print("БИНАРНЫЙ ПОИСК: ")
f = 0#нижняя граница
g = len(a)-1#верхняя граница
h = 0#счётчик сравнений
j = -1
while f <= g:#сужаем диапазон
    h += 1
    k = (f + g)//2#середина
    if a[k] == b:
        j = k#нашли
        break
    elif a[k] < b:
        f = k + 1
    else:
        g = k - 1
if j == -1:
    print("число не найдено")
else:
    print("индекс элемента: ", j)
    print("количество сравнений: ", h)