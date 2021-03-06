'''
Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(-15,30) for i in range(15)]) # за допомогою генератора списків створюємо масив
index = 0 # створюемо нулььову змінну
for i in range(len(x)): # перебираємо кожен елемент масиву
    if x[i]==x.max(): # визначаемо на якій позиції стоїть максимальне значення з масиву
        index = i # і присвоюємо змінній індекс
print(f'Масив: {x}\nНайбільше значення: {x.max()}, його індекс: {index}') # виводимо всі значення