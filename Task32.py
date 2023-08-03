# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3

N = int(input("Введите количество элементов: "))

arr = []
for i in range(N):
    arr.append(int(input("arr[{}] = ".format(i))))

print(arr)

mini = int(input('Min: '))
maxi = int(input('Max: '))
print(*[i for i in range(len(arr)) if mini <= arr[i] <= maxi],sep=', ')