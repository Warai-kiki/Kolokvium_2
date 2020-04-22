'''
Знайти суму всіх елементів масиву цілих чисел що задовольняють умові:
остача від ділення на 2 дорівнює 3. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 200 до 300.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(200,300) for i in range(20)]) # за допомогою генератора списків створюємо масив за умовами
y = np.array(list(filter(lambda n: n%2==3 , x))) # створюємо ще один масив, в якому відсортовані за
# потрібною умовою елементи першого масиву
print(f'Масив: {x}\nСума всіх його елементів, що задовольняють умову: {y.sum()}')
# виводимо на екран суму останнього масиву за допомогою вбудованої ф-ї sum