'''
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
x = np.array([randint(-10,10) for i in range(30)]) # за допомогою генератора списків створюємо масив за умовами
count = 0 # вводимо лічильник
value = list() # створюємо пустий список
n = 0 # ще один лічильник
while True: # цикл для уникнення зайвих дій
    for i in range(len(x)): # проходимо по елементам масиву
        if x[i] != x.min():  # обраховуємо кількіть елементів перед першим мінімальним числом
            n+=1
        else: # якщо натикаємось на мінімальне число
            break # обриваєм цикл
    break
while True: # вводимо цикл щоб не робити зайві перевірки
    for j in range(len(x)-n-2,-1,-1): # проходимо по елементам масиву зліва направо до елемента
        count+=1 # додаємо до лічильника 1
        value.append(x[j]) # додаємо в список елемент
    v = np.array(value) # переводимо список в масив щоб потім скористатись вбудованим методом sum
    if count==0: # вводимо перевірку щоб не виникла помилка у випадку коли перше мінімальне значення в кінці масиву
        print(f'Масив: {x}\nПісля першого мінімального елемента немає більше значень')
        break
    else: # у інших випадках
        y = v.sum()/count # знаходимо середнє арифметичне

        print('Масив: {}\nСереднє арифметичне значення тих елементів, які розташовані за першим по порядку мінімальним елементом {:.2f}'.format(x,y))
        # виводимо масив і середнє арифметичне
        break