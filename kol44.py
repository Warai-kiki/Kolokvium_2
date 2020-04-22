'''
Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(-50,100) for i in range(100)]) # за допомогою генератора списків створюємо масив за умовами
count = 0 # вводимо лічильник
for i in range(len(x)): # перебираємо всі елементи масиву
    if x[i]==i and x[i]%3==0: # якщо елемент відповідає умові
        count+=1 # додаємо до лічильника 1
print(f'Масив: {x}\nКількість елементів, які збігаються зі своїм номером і при цьому кратні 3: {count}') # виводимо значення