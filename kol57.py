'''
Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна.
Котулич К.А. 122А
'''
x = ['Black','White','Green','Blum','Kent','Nilson','Funk','Cold'] # створюємо список прізвищ
y = [9847,4557,7658,7987,5644,5474,8976,6865] # створюємо список
s = sum(y)/len(y) # визнааємо середнє значення
low_in = 0 # вводимо змінну для зручності
max1 = [] # створюємо пустий список
a = [] # і ще один
for i in range(len(y)): # перебираємо елементи списку зарплат
    lowi = abs(s-y[i]) # визначаємо різницю між середнім значенням і даним елелментом
    a.append(lowi) # додаємо це значення в список
for i in range(len(a)): # перебираєм елементи списку, який ми заповнили в попередньому циклі
    if a[i]==min(a): # знаходимо мінімальне значення
        low_in = x[i] #  зберігаємо фамілію з відповідним індексом
for i in range(len(y)): # перебираємо елементи списку зарплат
    if y[i]==min(y): # знаходимо мінімальне значення
        x.remove(x[i]) # видаляємо прізвище під таким самим індексом
        y.remove(y[i]) # видаляємо сам елемент
        break # перериваємо процес
for i in range(len(y)): # знову перебираємо елементи списку зарплат
    if len(max1)<=2: # поки у другому нашому списку 2 або менше елементів
        if y[i]==max(y): # додаєм до нього елемент зі списку прізвищ, індекс якого збігається
            max1.append(x[i]) # з індексом максимального елемента у списку зарплат
            y[i]=0 # міняємо значення максимального елемента на 0
    else: # коли в списку набирається два елемента
        break # перериваємо процес
print(f'Прізвище працівника, зарплата якого найменш відхиляється від середньої зарплати: {low_in}\n'
      f'Прізвища двох працівників з найбільшою заробітною платою: {max1}\n'
      f'Список працівників без прізвища того, чия зарплата найменша: {x}') # виводимо всі значення