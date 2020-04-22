'''
Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
повторюється найчастіше число.
Котулич К.А. 122А
'''
import numpy as np # вводимо numpy
from random import randint # вводимо рандом
x = np.array([randint(1,5) for i in range(10)]) # створюємо масив за допомогою генератора списків
print(x)
count = 1 # вводимо лічильник для основного значення
for i in range(len(x)-1): # пербираємо елементи масиву крім останнього
    count1 = 1 # вводимо лічильник на випадок якщо не одразу натрапимо на найбільш частий елемент
    for j in range(i+1,len(x)): # перебираємо кожен елемент з наступного
        if x[i]==x[j]: # порівнюємо з даним
            count1+=1 # рахуємо їх
    if count1>count: # якщо знайшовся елемент якого більше ніж 1
        count = count1 # робимо його кількість основним значенням
if count>1: # якщо є елемент якого більше ніж 1
    print(f'{count} разів в масиві повторюється найчастіше число') # виводимо кількість
else:  # якщо ні
    print('Кожен елемент в цьому масиві унікальний')