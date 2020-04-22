'''
Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
чисел в ньому.
Котулич К.А. 122А
'''
import numpy as np # вводимо numpy
from random import randint # вводимо рандом
x = np.array([randint(-10,10) for i in range(10)]) # створюємо масив за допомогою генератора списків
print(x) # виводимо масив
count = 0 # вводимо лічильник
for i in range(len(x)): # перебираємо елементи списку
    flag = True # вводимо прапорець, за яким будемо визначати унікальний елемент чи ні
    for j in range(len(x)): # знову перебираємо масив
        if x[i]==x[j] and j!=i: # порівнюємо даний елемент з іншими, якщо знахожимо рівний йому елемент
            flag = False # і це не сам елемент, змінюємо значення прапорця
    if flag == True: # за допомогою перевірки прапорця
        count+=1 # рахуємо кількість унікальних елементів
print(f'Кількість різних чисел в масиві: {count}') # вивоодимо значення
