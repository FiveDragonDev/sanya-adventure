from random import randint
from time import sleep

defult_actions: str = ['Порыться в мусоре — 1', 'Сдать бутылки — 2', 'Посмотреть содержимое инвентаря — 3',
					   'Посмотреть информацию — 4', 'Съесть что-нибудь — 5', 'Вылечить раны чем-то — 6',
					   'Остановить игру — 0']
items = {
	'food': {
		'trash': ['Кусок хлеба', 'Заплесневелый кусок хлеба', 'Яблочный огрызок']
	},
	'clothes': {
		'trash': ['Рваная рубашка', 'Грязные джинсы']
	},
	'consumables': {
		'trash': ['Бутылка', 'Грязный бинт'],
		'defult': ['Стерильный бинт']
	}
}
item_categories = ['food', 'clothes', 'consumables']
items_in_inventory = {
	'food': [],
	'clothes': [],
	'consumables': []
}
monies: int = 0
bottles = []
health = 100
hungry_time = 0
health_statuses = ['Голоден', 'Ранен', f'Голодный и раненый', 'Всё хорошо']
wounded = False
hungry = False
health_status = (health_statuses[1] if wounded
				 else health_statuses[3]) if not hungry \
	else (health_statuses[2] if wounded else health_statuses[0])

print(f'Добро пожаловать в приключения бомжа Сани!')
print(f'Ваша цель одна: ВЫЖИТЬ.')
print(f'Удачи!)\n')

actions_list: str = '; '.join(defult_actions)
print(f'Доступные действия: {actions_list}.')
while True:
	action = input('Ваше действие: ')

	if not action:
		print(f'Доступные действия: {actions_list}.')
	else:
		if '1' in action:
			# получение рандомной категории предметов
			random_category = str(item_categories[randint(0, len(item_categories)) - 1])
			# получение рандомного массива предметов
			items_in_trash = items[random_category]['trash']
			# получение рандомного значения из массива предметов (получение предмета)
			item_from_trash = str(items_in_trash[randint(0, len(items_in_trash) - 1)])
			print(f'Вы порылись в мусоре и нашли: {item_from_trash.lower()}.')
			items_in_inventory[random_category].append(item_from_trash)
			if 'Бутылка' == item_from_trash:
				bottles.append(item_from_trash)
				if randint(0, 100) <= 10:
					wounded = True
					print(f'Вы порезались о разбитую бутылку!')
			else:
				if randint(0, 100) <= 2:
					wounded = True
					print(f'Вы поранились пока рылись в мусоре!')
		elif '2' in action:
			monies += 1 * len(bottles)
			print(f'Вы получили {1 * len(bottles)} рублей продав {len(bottles)} бутылок')
			bottles.clear()
			try:
				for i in range(len(items_in_inventory['consumables'])):
					items_in_inventory['consumables'].remove('Бутылка')
			except:
				pass
		elif '3' in action:
			items_in_inventory.update()
			inventory = ''
			for i in item_categories:
				if not items_in_inventory[str(i)]:
					continue
				inventory += ', '.join(items_in_inventory[str(i)])
				if i != item_categories[len(item_categories) - 1]:
					inventory += ', '
			print(f'Содержимое инвентаря: {inventory.lower()}')
		elif '4' in action:
			health_status = (health_statuses[1] if wounded
				 else health_statuses[3]) if not hungry \
				else (health_statuses[2] if wounded else health_statuses[0])
			print('')
			print(f'Имя: Саня\n'
				  f'{monies} рублёв в кармане\n'
				  f'{health_status}, здоровье: {health if not wounded and not hungry else health - 1}%\n')
		elif '5' in action:
			if not hungry:
				print('Вы не голодны и решаете не тратить еду в пустую.')
				continue
			elif len(items_in_inventory['food']) <= 0:
				print('У вас нет еды.')
				continue
			eat = items_in_inventory['food'][randint(0, len(items_in_inventory['food']) - 1)]
			hungry = False
			hungry_time = 0
			items_in_inventory['food'].remove(eat)
			print(f'Вы съели {eat}, теперь вы не голодны.')
		elif '6' in action:
			if not wounded:
				print('Вы не ранены и решаете не тратить расходники в пустую.')
				continue
			elif len(items_in_inventory['consumables']) <= 0:
				print('У вас нет расходников.')
				continue
			consumables = items_in_inventory['consumables']
			consumables[:] = (value for value in consumables if value != 'Бутылка')
			consumable = consumables[randint(0, len(consumables) - 1)]
			wounded = False
			items_in_inventory['consumables'].remove(consumable)
			print(f'Вы использовали {consumable}, теперь вы не истекаете кровью.')
		elif '0' in action:
			break
		else:
			print('Некорректный выбор.')
	hungry_time += 1
	if hungry_time > 14:
		hungry = True
	if wounded or hungry:
		health -= 1
	if health <= 0:
		print('Мёртв...')
		break

print(f'Игра окончена...')
sleep(3.5)
