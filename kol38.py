'''
Дані про направлення вітру (північний, південний, східний, західний) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
південний вітер з силою, що перевищує 8 м / с.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array(['Північний','Південний','Північний','Східний','Західний','Південний','Східний','Східний','Західний','Південний'])
# створюємо масив з напрямками вітру
y = np.array([randint(0,20) for i in range(10)]) # створюємо масив зі швидкостями вітру
count = 0 # вводимо лічильник
for i in range(len(x)): # перебираємо елементи першого масиву
    if x[i]=='Південний': # в пошуках потрібного напрямку
        if y[i]>8: # якщо швидкість під цим же індексом з другого списку відповідає умові
            count+=1 # додаємо до лічильника 1
print(f'{count} дні(день) дув південний вітер з силою, що перевищує 8 м / с') # виводимо значення лічильника
