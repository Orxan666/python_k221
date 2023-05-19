# MODULE HOMEWORK
# 1-ci sual
# import math


# def get_coni_area(r,h):
#     result=(1/3)*math.pi*(r**2)*h
#     return result

# print(get_coni_area(2,5))
# --------
# def get_glob_value(r):
#     result=(4/3)*math.pi*(r**3)
#     return result
# print(get_glob_value(5))

# ------------------2-ci sual
# import math

# def get_combination(n,r):
#     if n<r:
#         raise ValueError('n>r sertine uygun olmalidir')
#     a=math.factorial(n)
#     diff =math.factorial(r)*math.factorial(n-r)
#     result=a/diff
#     return result
# print(get_combination(7,4))

# 3-cu sual

# from random import shuffle
# names = input('adlar; daxil edin: ').split(', ')
# shuffle(names)
# for n in names:
#     input(n)

# 4-cu sual-----------------------

# import random
# start:int=int(input('baslangic deyeri daxil edin : '))
# end:int=int(input('sonuncu deyeri daxil edin : '))
# number:int=random.randint(start,end)

# print(number)

# attempt:int=0
# attempt+=1
# while True:
  
#     prediction:int=int(input('ededi deyin: '))
#     if prediction > number:
#         print('asagi eded teyin edin')
#     elif prediction < number:
#         print('yuxari eded yazin')
#     else:
#         if attempt>3:
#             print(f'uduzduz cunki siz {attempt} qeder bextinizi sinadiniz vallah mumkun deyil')
#             break

#         else:
#             print('qalib oldunuz')
#         break
# eded_araliq=random.randint(1,50)
# texmin_haqqi=10
# saygac=0
# while True:
#     eded=int(input('1-50 arasi eded daxil edin'))
#     texmin_haqqi-=1
#     saygac+=1
#     if 
# import random

# start = int(input("Baslangic ededi qeyd edin: "))
# finish = int(input("Hansi edede qeder olacagin qeyd edin: "))

# gizlireqem = random.randint(start, finish)

# cehd = 0
# texmin = None

# while texmin != gizlireqem:
#     if cehd > 9:
#         print("Meglub oldunuz!")
#         break 
#     else:
#         texmin = int(input("Verdiyiniz araliqdaki ededi texmin edin: "))

#         if texmin < gizlireqem:
#             print("Yuxari")
#             cehd += 1
#         elif texmin > gizlireqem:   
#             print("Asagi")
#             cehd += 1
#         else:
#             print("Tebrikler! Qalibsiniz!")
#             break
# ++++++++++++++++++++++++++++++++++++++++++++++
#==== TIMEIT LESSON====

# from timeit import timeit,repeat

# duration1=timeit('[i**3 for i in (1,2,3,4,5,6,7,8)]',number=7)
# duration2=timeit('map(lambda x: x**3, (1,2,3,4,5,6,7,8))',number=7)

# print(duration1,duration2)


# a=(1,2,3,4,5,6,7,8)

# duration1=timeit('[i**3 for i in a]','from __main__ import a',number=100_000)
# duration2=timeit('map(lambda x: x**3,a)','from __main__ import a',number=100_000)

# print(duration1,duration2)










# print(sys.version)
# print(sys.version_info)


# argv: list[str]=sys.argv

# filename:str =argv[1]
# count:int=int(argv[2])

# with open('rufet.txt','w') as file:
#     for i in range(1,1+1):
#         file.write(f'{i}. \n')
# print('COMPLETED!')


# import sys


# for line in sys.stdin:
#     if 'q'==line.rstrip():
#         break
#     print(f'Input {line}')

# print('Exit')

# from math import pi,comb,perm
# import random

# form=input('ad daxil edin').split(', ')
# adlar=len(form)
# while True:
#     input('yeniden daxil edin')
#     secilen_ad=random.choice(form)
#     form.remove(secilen_ad)
#     adlar-=1
#     print(secilen_ad)

#     if adlar==0:
#         print('adlar bitdi')
#         break

from datetime import datetime,timedelta
mesafe=588000000
suret= 90
vaxt=mesafe/suret
zaman= datetime.now()+timedelta(hours=vaxt)
a= zaman.strftime('%d.%m.%Y')
print(f"niva ile {a} tarixde catacaqsiz ")
# print(zaman)

'“Saat 17:00, 04.06.2022 tarixində dərsə gəlin” cümləsindən istifadə edərək tarixi datetime formatına çevirin. '
cumle='Saat 17:00, 04.06.2022 tarixində dərsə gəlin'
cumle_format='Saat %H:%M , %d.%m.%Y tarixində dərsə gəlin'
