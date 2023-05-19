# animal = input(
#     'Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')
# farm = ('inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at', 'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'qoyun', 'keci', 'keci',
#         'qoyun', 'at', 'qoyun', 'inek', 'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', 'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

# text = '''Axtarilan Heyvan: {}
# {}
# Fermadaki {} sayi:  {}
# Diger heyvanlara olan faizi: {}%
# {} umumi qiymeti: {} AZN
# '''.format(
#     animal,
#     "-"*20,
#       animal,
#       farm.count(animal),
#       farm.count(animal)/len(farm)*100,
#       animal,
#       farm.count(animal)*qiymetler[animal])


# print(text)


# sentence="Salam {} necesen senin {} yasin var".format("Rufet",26)
# print(sentence)

# ededler = [1, 53, 22, 5, 6, 1, 3, 4, 76]
# ['tek', 'tek', 'cut', 'tek', 'cut', 'tek', 'tek', 'cut', 'tek']

# result = [('tekdir' if eded % 2 != 0 else 'cutdur') for eded in ededler[:4] ]
# result = {eded:('tekdir' if eded % 2 != 0 else 'cutdur') for eded in ededler[:5]if eded<10}

# print(result)
# print('armud','heyva','nar', sep=' , ', end='\n yemek isteyirem')
# print('bitdi!')


# def human_years_cat_years_dog_years(human_years):
#     cat_years = 0
#     dog_years = 0

#     if human_years > 0:
#         cat_years += 15
#         dog_years += 15

#     if human_years > 1:
#         cat_years += 9
#         dog_years += 9

#     if human_years > 2:
#         cat_years += (human_years-2)*4
#         dog_years += (human_years-2)*5

#     return [human_years, cat_years, dog_years]


# print(
#     human_years_cat_years_dog_years(10)

# )
 
