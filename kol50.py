'''
У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
Котулич К.А. 122А
'''
from random import choice # вводимо функцію для вибору рандомних значень зі списку
x = [i for i in range(1,101)] # за допомогою генератора створюємо список з квитками
y = [choice(x) for j in range(10)] # з них обирається 10 рандомних (виграшних)
while True: # цикл для перевірки та перехоплення помилок
    try:
        a = int(input('Введіть номер квитка: ')) # користувач вводить число
        if 0<a<=100: # перевіряємо чи підходить це
            break
        else:
            print('Немає такого квитка. Спробуйте ще раз')
    except ValueError or TypeError or KeyError:
        print('Щось пішло не так. Спробуйте ще раз') # перехоплення помилок
if a in y: # якщо задане число є в списку виграшних
    print('Вітаємо! Це виграшний квиток')
else: # якщо ні
    print('На жаль, це не виграшний квиток')