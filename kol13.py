'''
Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(-40,40) for i in range(15)]) # за допомогою генератора списків створюємо масив з 15-ти елементів
print(f'Масив: {x}\nМаксимальне значення: {x.max()}') # виводимо максимальне значення максиву за допомогою вбудованої ф-ї max