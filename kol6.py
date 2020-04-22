'''
Створіть масив А [1..8] за допомогою генератора випадкових чисел з
елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних
елементів масиву.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(-10,10) for i in range(8)]) # за допомогою генератора списків створюємо масив
a = list() # створюємо пустий список
for i in range(len(x)): # перебираємо кожен елемент масиву
    if x[i]<0: # умова для визначення елементів що менше нуля
        a.append(x[i]) # додаємо потрібні елементи в пустий список
print(f'Масив: {x}\nКількість від’ємних елементів: {len(a)}') # виводимо довжину заповненного спискуєєє