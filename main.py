from random import randint, randrange
from time import sleep

defult_actions: str = ['Порыться в мусоре — 1', 'Сдать бутылки — 2', 'Посмотреть содержимое инвентаря — 3',
					   'Посмотреть информацию — 4', 'Съесть что-нибудь — 5', 'Вылечить раны чем-то — 6',
					   'Сходить в магаз — 7', 'Украсть какую-то вещь — 8', 'Остановить игру — 0']
passport_actions: str = ['Сменить имя — 1', 'Продолжить игру — 0']
items = {
	'food': {
		'trash': ['Кусок хлеба', 'Заплесневелый кусок хлеба', 'Яблочный огрызок'],
		'defult': ['Яблоко;2', 'Доширак;15', 'Ролтон;5']
	},
	'clothes': {
		'trash': ['Рваная рубашка', 'Грязные джинсы'],
		'defult': ['Рубашка;7']
	},
	'consumables': {
		'trash': ['Бутылка', 'Грязный бинт', 'Кусок белого халата'],
		'defult': ['Стерильный бинт;3', 'Пачка сигарет;5']
	}
}
NPCs_names = ['Саня', 'Лёха', 'Аркаша', 'Димон', 'Константин']
item_categories = ['food', 'clothes', 'consumables']
items_in_inventory = {
	'food': [],
	'clothes': [],
	'consumables': []
}
events = ['На вас напал гопник', 'Вы отравились', 'Вы нашли кошелёк на земле']
monies = 0
bottles = []
health = 100
hungry_time = 0
health_statuses = ['Голоден', 'Ранен', 'Голодный и раненый', 'Всё хорошо']
wounded = False
hungry = False
player_name: str = 'Саня'
days_without_events: int = 0
debug = False
health_status = (health_statuses[1] if wounded
				 else health_statuses[3]) if not hungry \
	else (health_statuses[2] if wounded else health_statuses[0])
social_statuses = ['Бомж', 'Главный бомж', 'Кассир', 'Менеджер', 'Главный менеджер', 'Начальник', 'Босс',
				   'Главный босс', 'Бизнесмен']
social_status = social_statuses[0]
social_rating = 0
null_social_rating = 0

print(f'Добро пожаловать в приключения бомжа Сани!')
print(f'Ваша цель одна: ВЫЖИТЬ.')
print(f'Удачи!)\n')

print(f'Так же, хочу сказать, что код этой игры есть в свободном доступе.'
	  f' ВЫ можете его скачать и менять правила игры или добавлять, что вашей душе угодно!')
print(f'https://github.com/FiveDragonYT/sanya-adventure\n\n')

defult_actions_list: str = '; '.join(defult_actions)
print(f'Доступные действия: {defult_actions_list}.')
while True:
	if debug:
		print('ВКЛЮЧЁН ДЕБАГ РЕЖИМ... ')
	action = input('Ваше действие: ').lower().strip()

	if not action:
		print(f'Доступные действия: {defult_actions_list}.')
	elif action.startswith('/'):
		action = action.replace('/', '', 1)

		if 'debug' == action:
			if debug:
				debug = False
				print('Режим ДЕБАГ выключен!')
				continue
			debug = True
			print('Режим ДЕБАГ включён!')
		elif debug:
			if 'heal' == action:
				health = 100
				wounded = False
				hungry = False
				hungry_time = -15
				if monies <= 0:
					monies = 1000
				print(f'Вы полностью здоровы!')
			elif 'monies;' in action:
				try:
					h = action.split(';')
					monies = int(h[1].strip().lower())
					print(f'Новое кол-во денег: {monies}')
				except:
					pass
			elif 'social;' in action:
				h = action.split(';')
				null_social_rating = int(h[1].strip().lower())
				social_rating = null_social_rating
				for i in range(round(social_rating / 100)):
					if null_social_rating >= 100:
						null_social_rating -= 100
						i: int = social_statuses.index(social_status)
						i += 1
						social_status = social_statuses[i]
				print(f'Новый соц. статус: {social_status}\n'
					  f'Новое кол-во соц. рейтинга: {social_rating}')
			elif 'health;' in action:
				h = action.split(';')
				try:
					health = int(h[1])
				except:
					pass
				print(f'Новое кол-во здоровья: {health}')
			elif 'suicide' == action:
				health = 0
				if debug:
					print('Мёртв...')
					break
			else:
				print('Команда не существует.')
		else:
			print('Команда не существует.')
	else:
		if '1' == action:
			# получение рандомной категории предметов
			random_category = str(item_categories[randrange(len(item_categories))])
			# получение рандомного массива предметов
			items_in_trash = items[random_category]['trash']
			# получение рандомного значения из массива предметов (получение предмета)
			item_from_trash = str(items_in_trash[randrange(len(items_in_trash))])
			print(f'Вы порылись в мусоре и нашли: {item_from_trash.lower()}.')
			items_in_inventory[random_category].append(item_from_trash)
			if not debug:
				if 'Бутылка' == item_from_trash:
					bottles.append(item_from_trash)
					if randint(0, 100) <= 10:
						wounded = True
						print(f'Вы порезались о разбитую бутылку!')
				else:
					if randint(0, 100) <= 2:
						wounded = True
						print(f'Вы поранились пока рылись в мусоре!')
			else:
				if 'Бутылка' == item_from_trash:
					bottles.append(item_from_trash)
					wounded = True
					print(f'Вы порезались о разбитую бутылку!')
				else:
					wounded = True
					print(f'Вы поранились пока рылись в мусоре!')
		elif '2' == action:
			give_monies = 2 * len(bottles)
			print(f'Вы получили {give_monies} рублей продав {len(bottles)} бутылок')
			monies += give_monies
			items_in_inventory['consumables'] = list(set(items_in_inventory['consumables']) - set(bottles))
			if len(bottles) >= 2:
				if randint(0, 100) <= 50:
					getting_social_rating = randint(5, 20)
					print(f'Люди подумали, что вы волонтёр и убираетесь на улице. '
						  f'Социальный рейтинг +{getting_social_rating}')
					null_social_rating += getting_social_rating
					social_rating += getting_social_rating
					for i in range(round(social_rating / 100)):
						if null_social_rating >= 100:
							null_social_rating -= 100
							i: int = social_statuses.index(social_status)
							i += 1
							social_status = social_statuses[i]
					print(f'Ваш социальный статус: {social_status}\n'
						  f'Ваше кол-во социального рейтинга: {social_rating}')
			bottles.clear()
		elif '3' == action:
			items_in_inventory.update()
			inventory = ''
			for i in item_categories:
				if not items_in_inventory[str(i)]:
					continue
				inventory += ', '.join(items_in_inventory[str(i)])
				if i != item_categories[len(item_categories) - 1]:
					inventory += ', '
			print(f'Содержимое инвентаря: {inventory.lower()}')
		elif '4' == action:
			health_status = (health_statuses[1] if wounded
							 else health_statuses[3]) if not hungry \
				else (health_statuses[2] if wounded else health_statuses[0])
			print('')
			print(f'Имя: {player_name}\n'
				  f'{monies} рублёв в кармане\n'
				  f'{health_status}, здоровье: {health if not wounded and not hungry else health - 1}%\n'
				  f'Ваш социальный статус: {social_status}\n')
			passport_actions_list: str = '; '.join(passport_actions)
			print(f'Доступные действия: {passport_actions_list}.')
			while True:
				passport_action = input('Ваше действие: ')

				if not passport_action:
					print(f'Доступные действия: {passport_actions_list}.')
				else:
					if '1' == passport_action:
						if not debug:
							if monies < 10:
								print('Не достаточно денег')
								continue
						player_name = input('Введите ваше НОВОЕ имя: ')
						print(f'Ваше новое имя: {player_name}')
					elif '0' == passport_action:
						print('')
						break
					else:
						print('Некорректный выбор.')
		elif '5' == action:
			if not debug:
				if not hungry:
					print('Вы не голодны и решаете не тратить еду в пустую.')
					continue
				elif len(items_in_inventory['food']) <= 0:
					print('У вас нет еды.')
					continue
				eat = items_in_inventory['food'].pop()
				hungry = False
				hungry_time = 0
				print(f'Вы съели {eat.lower()}, теперь вы не голодны.')
			else:
				hungry = False
				hungry_time = 0
		elif '6' == action:
			if not debug:
				if not wounded and health > 90:
					print('Вы не ранены и решаете не тратить расходники в пустую.')
					continue
				elif len(items_in_inventory['consumables']) <= 0:
					print('У вас нет расходников.')
					continue
				consumables = items_in_inventory['consumables']
				try:
					consumables[:] = (value for value in consumables if value != ('Бутылка' or 'Пачка сигарет'))
				except:
					print('Произошла некоторая ошибка, пожалуйста напишите отзыв и приложите к нему скриншот ошибки')
					continue
				if len(consumables) <= 0:
					print('У вас нет расходников.')
					continue
				consumable = consumables.pop()
				wounded = False
				health += 5
				if health > 100:
					health = 100
				print(f'Вы использовали {consumable.lower()}, теперь вы не истекаете кровью.')
			else:
				wounded = False
				health += 5
				if health > 100:
					health = 100
		elif '7' == action:
			item_categories_list = ''
			for i in range(len(item_categories)):
				item_categories_list += item_categories[i] + f' — {i + 1}; '
			print(f'Доступные категории предметов для покупки: {item_categories_list}')
			category_index = input('Выберите номер категории предметов: ').lower().strip()
			if len(item_categories) >= int(category_index) >= 1:
				selected_category = item_categories[int(category_index) - 1]
				print(f'Выбрана категория: {selected_category}')
				items_in_category_str = ''
				items_in_category = items[selected_category]['defult']
				try:
					for i in range(len(items[selected_category]['defult'])):
						items_in_category_str += items[selected_category]['defult'][i] + f' — {i + 1}'
						if i != len(items[selected_category]['defult'][i]):
							items_in_category_str += ', '
				except:
					print('Произошла некоторая ошибка, пожалуйста напишите отзыв и приложите к нему скриншот ошибки')
					continue
				print(print(f'Доступные предметы: {items_in_category_str}'))
				item_index = input('Введите номер предмета, который хотите купить: ').lower().strip()
				try:
					item_index = int(item_index)
				except TypeError:
					continue
				if item_index > len(items_in_category):
					print('Предмет не найден')
				else:
					selected_item = str(items_in_category[item_index - 1])
					h = selected_item.split(';')
					item_price = int(h[1])
					selected_item = h[0]
					print(f'Вы выбрали {selected_item}, его цена {item_price} рублей')
					if monies >= item_price:
						while True:
							print(f'Купить — 1; Не покупать — 2; ')
							buy_or_not = input('Ваше действие: ').lower().strip()
							if '1' == buy_or_not:
								monies -= item_price
								items_in_inventory[selected_category].append(selected_item)
								print(f'Вы успешно купили {selected_item.lower()}! Ваше новое кол-во денег: {monies}')
								break
							elif '2' == buy_or_not:
								print(f'Вы отказались от покупки {selected_item.lower()}')
								break
							else:
								print('Некорректный выбор.')
					else:
						print(f'К сожалению у вас не хватает денег, '
							  f'{selected_item.lower()} стоит {item_price} рублей')
			else:
				print('Номера такой категории не существует')
		elif '8' == action:
			random_item = items['consumables']['defult'][randrange(len(items['consumables']['defult']))]
			random_npc = NPCs_names[randrange(len(NPCs_names))]
			if randint(0, 100) <= 65:
				h = random_item.split(';')
				random_item = h[0]
				items_in_inventory['consumables'].append(random_item)
				print(f'Вы попытались украсть какую-нибудь вещь у {random_npc} и... У Вас получилось!\n'
					  f'Вы украли {random_item.lower()} у {random_npc}, '
					  f'{random_item.lower()} добавлено в ваш инвентарь')
				if randint(0, 100) <= 60:
					getting_social_rating = randint(10, 30)
					print(f'К сожалению, кто-то увидел, как Вы воруете. Социальный рейтинг -{getting_social_rating}')
					null_social_rating -= getting_social_rating
					social_rating -= getting_social_rating
					for i in range(round(social_rating / 100)):
						if null_social_rating >= 100:
							null_social_rating -= 100
							i: int = social_statuses.index(social_status)
							i += 1
							social_status = social_statuses[i]
					print(f'Ваш социальный статус: {social_status}\n'
							f'Ваше кол-во социального рейтинга: {social_rating}')
			else:
				print(f'Вы попытались украсть какую-нибудь вещь у {random_npc} и... У Вас не получилось...\n'
					  f'{random_npc} вызвал полицию, Вы арестованы...')
				break
		elif '0' == action:
			sure = input('Введите 0 еще раз, если хотите выйти из игры (весь прогресс будет утерян!)\n').lower().strip()
			if sure == '0':
				break
			else:
				print('Вы решили не выходить из игры, молодцы!\n'
					  'Это действие не будет считаться.')
				continue
		else:
			print('Некорректный выбор.')

		hungry_time += 1
		days_without_events += 1
		if hungry_time > 14:
			hungry = True
		if wounded or hungry:
			health -= 1
		# Рандомные события
		if days_without_events >= 7:
			if randint(0, 100) <= 75:
				event = events[randint(0, len(events) - 1)]
				print(event)
				if event == 'На вас напал гопник':
					health -= 15
					wounded = True
				elif event == 'Вы отравились':
					health -= 5
				elif event == 'Вы нашли кошелёк на земле':
					monies += 15
			days_without_events = 0

		# Проверка на здоровье, уберите, чтобы стать бессмертным
		if not debug:
			if health <= 0:
				print('Мёртв...')
				break

print(f'Игра окончена...')
sleep(3.5)
end_not_end = True
while end_not_end:
	action = input('Нажмите Enter для выхода...\n').lower().strip()
	if action.startswith('/'):
		action = action.replace('/', '')
		if 'stat' in action:
			health_status = (health_statuses[1] if wounded
							 else health_statuses[3]) if not hungry \
				else (health_statuses[2] if wounded else health_statuses[0])
			print('')
			print(f'Имя: {player_name}\n'
				  f'{monies} рублёв в кармане\n'
				  f'{health_status}, здоровье: {health if not wounded and not hungry else health - 1}%\n'
				  f'Ваш социальный статус: {social_status}\n')
	else:
		exit()
