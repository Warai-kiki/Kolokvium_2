'''
Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
з початку і третього від кінця і т.д.
Котулич К.А. 122А
'''
x = ['Black','White','Green','Blum','Kent','Nilson','Funk','Cold'] # створюємо список прізвищ
count = -1 # додаємо лічильник, який допоможе визначати елемент з іншого кінця списку
for i in range(len(x)//2): # перебираємо половину списку
    x[i],x[count]=x[count],x[i] # і міняємо елементи місцями з відповідними
    count-=1 # значення індексу зменшується на 1
print(x) # виводимо список