cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }


def get_shop_list_by_dishes(dishes, person_count):
  grocery_list = {}
  for i in dishes:
    for z in cook_book.get(i):
      ingredient = z.get('ingredient_name')
      if ingredient not in grocery_list:
        grocery_list[ingredient] = {'measure': z.get('measure'), 'quantity': (z.get('quantity') * person_count)}
      else:
        ingredient_repeat = grocery_list[ingredient]['quantity']
        grocery_list[ingredient] = {'measure': z.get('measure'), 'quantity': ((z.get('quantity') * person_count) +
                                    ingredient_repeat)}
  for c, k in grocery_list.items():
    print(c, k)



get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
