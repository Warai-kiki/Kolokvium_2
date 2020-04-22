'''
Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(100,200) for i in range(20)]) # за допомогою генератора списків створюємо масив за умовами
y = np.array(list(filter(lambda n: n%2==0 , x))) # створюємо ще один масив, в якому відсортовані за
# потрібною умовою елементи першого масиву
print(f'Масив: {x}\nСума всіх його парних елементів: {y.sum()}') # виводимо на екран суму останнього масиву за допомогою вбудованої ф-ї sum
