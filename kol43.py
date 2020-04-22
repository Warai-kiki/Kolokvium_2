'''
Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(0,200) for i in range(10)]) # за допомогою генератора списків створюємо масив за умовами
while True: # цикл для перевірки та перехоплення помилок
    try:
        a,b = int(input('Введіть значення а: ')),int(input('Введіть значення d: ')) # користувач вводить число
        if 0<a<=200 and 0<b<=200: # перевіряємо чи взагалі може це число трапитись в масиві
            break
        else:
            print('Спробуйте ще раз')
    except ValueError or TypeError or KeyError:
        print('Щось пішло не так. Спробуйте ще раз')
w = False # вводимо нашу змінну зі значенням хиби
for i in range(len(x)): # перебираємо елементи масиву
    if x[i]%a==0 and x[i]%b!=0: # якщо хоча б один відповідатиме умові
        w = True # значення зміниться на істину
print(f'{x}\n{w}') #  виводимо результат