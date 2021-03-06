'''
Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(-10,10) for i in range(30)]) # за допомогою генератора списків створюємо масив за умовами
count = 0 # вводимо лічильник
while True: # цикл для перевірки та перехоплення помилок
    try:
        a = int(input('Введіть число: ')) # користувач вводить число
        if -10<=a<=10: # перевіряємо чи взагалі може це число трапитись в масиві
            if a in x: # додатково перевіряємо чи є дане число в масиві
                break
            else:
                print('Дане число не випало в масиві. Спробуйте ще раз')
        else:
            print('Дане число не може випасти в масиві. Спробуйте ще раз')
    except ValueError or TypeError or KeyError:
        print('Щось пішло не так. Спробуйте ще раз')
while True: # вводимо цикл щоб не робити зайві перевірки
    for i in range(len(x)): # проходимо по елементам масиву
        if x[i]!=a: # якщо елемент не дорівнює заданому числу
            if x[i]%2==0: # якщо остача від ділення на 2 дорівнює 0
                count+=1 # додаємо до лічильника 1
        else: # якщо натикаємось на дане число
            break # обриваємо цикл

    print(f'Масив: {x}\nВ ньому {count} парних елементів перд заданим числом') # виводимо масив і кількість парних елементів
    break