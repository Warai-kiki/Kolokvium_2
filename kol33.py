'''
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
A = np.array([randint(-10,20) for i in range(20)]) # за допомогою генератора списків створюємо масив за умовами
y = list() # створюємо пустий список
for i in range(len(A)): # перебираємо кожен елемент масиву
    if A[i]!=0: # якщо елемент не дорівнює нулю
        y.append(A[i]) # додаємо його в список
z = np.array(y) # переводимо список в масив щоб скористатись вбудованим методом prod
print(f'Масив А:{A}\nДобуток всіх його ненульових елементів: {z.prod()}') # одразу виводимо добуток