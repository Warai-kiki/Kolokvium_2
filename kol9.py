'''
З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
що протягом цього часу температура знижувалася. Визначте, о котрій годині було
вперше зафіксовано від'ємну температуру.
Котулич К.А. 122А
'''
x,y = [i for i in range(8,21)],[j for j in range(18,-10,-2)] # створюємо два списки зі значеннями годин і температури
# за допомогою генератора списків; для годин беремо стандартний крок і визначаємо потрібний початок і кінець
# а для температури беремо від'ємний крок і з більшим значенням
z = {c: d for (c,d) in zip(x,y)} # створюємо словник,поєднуючи наші списки
v = list() # створюємо пустий список для подальшого заповнення
for i in z.keys(): # перебираемо в і ключі словника
    if z[i]<0: # знаходимо від'ємні значення
        v.append(z[i]) # заносимо їх в пустий список в порядку їх знаходження циклом
for i in z.keys(): # знову перебираємо всі ключі
    if z[i]==v[0]: # знаходимо ключ, який відповідає першому значенню зі списку
        print(f'О {i} годині вперше зафіксовано від`ємну температуру ({z[i]})') # виводимо відповідну годину