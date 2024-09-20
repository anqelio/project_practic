from datetime import datetime, timedelta
import re
try:
    print('Доступные пиццы: ')
    print('1. Маргарита')
    print('2. Пепперони')
    print('3. Грибная')
    print('4. Четыре сыра')
    print('5. Капричоза')
    date_today = datetime.now()
    result = date_today + timedelta(hours = 1)
    what_pizza = int(input('Какую пиццу вы хотите заказать? (Введите номер): '))
    sum_pizza = int(input('Сколько пицц вы хотите заказать? (Введите количество): '))
    while True:
        if what_pizza == 1:
            name_pizza = "Маргарита"
        elif what_pizza == 2:
            name_pizza = 'Пепперони'
        elif what_pizza == 3:
            name_pizza = 'Грибная'
        elif what_pizza == 4:
            name_pizza = 'Четыре сыра'
        elif what_pizza == 5:
            name_pizza = 'Капричоза'
        else:
            print('Номер пиццы отсутствует. Пожалуйста, выберите номер из списка.')
        print(f'Вы заказали {sum_pizza} пицц {name_pizza}')
        review = input('Готовы ли вы оставить отзыв? (да/нет): ')
        if review == ('да'):
            review_one = input('Введите ваш отзыв: ')
            regex = r'вкусно'
            if regex.search(review_one):
                print('Спасибо за положительный отзыв! Получите пиццу в подарок')
            print('Спасибо, что воспользовались нашим сервисом!')
            print(f'Заказ от {date_today} принят. Наш курьер подъедет к вам в течение часа (до {result})')
        break
except ValueError as e:
    print('Ввод должен быть числом')