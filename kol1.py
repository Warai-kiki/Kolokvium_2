'''
Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне.
Котулич К.А. 122А
'''
import numpy as np # вводимо бібліотеку для масивів
y = np.array([int(input('Ведіть число: ')) for i in range(5)]) # за допомогою генератора списків заповнюємо масив
x = y.sum()/5 # за допомогою вбудованої функції знаходимо суму елементів масиву та ділимо на їх кількість яку ми вказали в генераторі списку
g = str(list(y)) # переводимо масив в список а потім в строку
print(f'{g[1:-1]}\nСереднє арифметичне: {x}') # щоб вивести строку без квадратних дужок використовуємо зрізи