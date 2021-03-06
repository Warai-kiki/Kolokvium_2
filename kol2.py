'''
Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення коріння і квадратів кожного з елементів масиву.
Котулич К.А. 122А
'''
import numpy as np # вводимо бібліотеку для масивів
x = np.array([int(input('Ведіть число: ')) for i in range(5)]) # за допомогою генератора списків заповнюємо масив
y = list(x**2) # створюємо список з елементів піднесених до степеня 2
z = list(x**(1/2)) # щоб отримати корінь з елементів підносимо до степеня 1/2
print(f'Корінь з кожного елемента: {z}\nКожен елемент в квадраті: {y}') # виводимо результати