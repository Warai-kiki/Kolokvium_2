'''
Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
числами від 500 до 1000.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(500,1000) for i in range(30)]) # за допомогою генератора списків створюємо масив за умовами
y = np.array(list(filter(lambda n: n%5==0 and n%8==0, x))) # створюємо ще один масив, в якому відсортовані за
# потрібною умовою елементи першого масиву
print(f'Масив: {x}\nСума всіх його елементів, що діляться на 5 і на 8 одночасно: {y.sum()}')
# виводимо на екран суму останнього масиву за допомогою вбудованої ф-ї sum