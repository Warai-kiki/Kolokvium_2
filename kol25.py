'''
Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(10,100) for i in range(10)]) # за допомогою генератора списків створюємо масив за умовами
y = np.array(list(filter(lambda n: n%5==0 , x))) # створюємо ще один масив, в якому відсортовані за
# потрібною умовою елементи першого масиву
print(f'Масив: {x}\nДобуток всіх його елементів, що кратні 5: {y.prod()}')
# виводимо на екран добуток елементів останнього масиву за допомогою вбудованої ф-ї prod