'''
Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Котулич К.А. 122А
'''
from random import randint # вводимо рандом
import numpy as np # вводимо бібліотеку для масивів
while True: # основний цикл програми
    x = np.array([randint(50,100) for i in range(20)]) # за допомогою генератора списків створюємо масив за умовами
    while True: # вводимо цикл 1 для перевірки
        while True: # вводимо цикл 2 для перехоплення помилок
            try: # перевіряємо код на помилки
                n = int(input('Введіть число (від 50 до 100): ')) # користувач вводить число
                break # якщо помилок не виникає цикл 2 обривається
            except ValueError or KeyError or TypeError: # якщо випливають вказані помилки
                print('Щось пішло не так. Спробуйте ще раз') # просимо користувача повторити введення і цикл повторюється
        if 50<=n<=100: # перевірка на входження в потрібний діапазон, тобто чи можуть бути такі значення в масиві
            break # якщо так, цикл 1 обривається
        else: # в іншому випадку
            print('Ваше число не входить в даний діапазон') # попередження і повторення циклу 1
    y = np.array(list(filter(lambda a: a>n , x))) # створюємо ще один масив, в якому відсортовані за
    # потрібною умовою елементи першого масиву
    print(f'Масив: {x}\nСума всіх його елементів, що більші за {n}: {y.sum()}')
    # виводимо на екран суму останнього масиву за допомогою вбудованої ф-ї sum

    print('Хочете спробувати ще раз? Напишіть так чи ні') # питаємо у користувача чи хоче він повторити
    l = input() # користувач вводить відповідь
    if l=='так': # якщо відповідь позитивна
      continue # повторно проходимо цикл
    else: # у будь-яких інших випадках
         break # обриваємо основний цикл