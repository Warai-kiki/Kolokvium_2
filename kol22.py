'''
Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(5,500) for i in range(20)]) # за допомогою генератора списків створюємо масив за умовами
y = np.array(list(filter(lambda n: n%3==0 or n%9==0, x))) # створюємо ще один масив, в якому відсортовані за
# потрібною умовою елементи першого масиву
print(f'Масив: {x}\nДобуток всіх його елементів, кратних 3 і 9: {y.prod()}')
# виводимо на екран добуток елементів останнього масиву за допомогою вбудованої ф-ї prod