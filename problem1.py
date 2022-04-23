#                 PROBLEM!
#menu = {'lagman':120, 
#	'plov': '120', 
#	'borsh':100}
#print(menu)
#drinks = {'drinks':['Coca-Cola', 'Sprite','Fanta']}
#print(drinks)
#menu.update(drinks)
#print(menu)





#                  PROBLEM2
#a = {}
#l = input('Введите логин: ')
#p = input('Введите пароль: ')
#a[l] = p
#l = input('Введите логин: ')
#p = input('Введите пароль: ')
#a[l] = p
#l = input('Введите логин: ')
#p = input('Введите пароль: ')
#a[l] = p
#print(a)





#                  PROBLEM3
#a = {'Sanzhar':'Ecomomic',
#    'Ruslan':'Voditel',
#    'Almaz':'Mehanik',
#    'Dastan':'Programmer',
#    'Kairat':'Mentor'
#}



#				PROBLEM4

#menu = {'lagman':120, 
#       'plov': '120', 
#       'borsh':100}

#print('Меню: ',menu)
#menu.update({'besh_barmak':130})
#print(menu)
#print('Лагман слишком дешёвый')
#menu.update({'besh_barmak':135})
#print(menu)
#print('Вашповар отвратительно готовит, удалите лагман из меню!')
#menu.pop('lagman')
#print(menu)



south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
a = set(south_american_countries)
b = set(range(1,13))
a = dict(zip(b,a))
print(a)

