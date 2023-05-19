

# 1. Bu kodda baş verə biləcək errorları araşdırıb, onları handle edin
# 2. Təxmin edə bilməyəcəyiniz errorlar üçün bir şərt qoşun
# 3. Əgər istifadəçi 10-dan artıq və ya 3-dən az heyvan giribsə internetdən istədiyiniz bir erroru taparaq təyin edin.



# try:
#     animals = input('Heyvanlari girin: ').split(', ')
    
#     if not 3 < len(animals) < 10:
#         print('Umumi qiymet:', sum(map(lambda animal: prices[animal], animals)))
#         raise ValueError('Heyvanlar 3-ile 10 arasinda olmalidir')
#     prices = { 'inek': 500, 'toyuq': 50, 'qoyun': 120, 'at': 900, 'keci': 210 }

# except KeyError as error:
#     print('olmayan bir heyvan girdiniz.xeta sebebi: ',  {error})
# except Exception as error:
#     print('bilinmeyen bir xeta bas verdi .xeta kodu: ', {error})

# 1000-dən 0001-ə qədər sağında nöqtə ilə düzülmüş bir text faylı hazırlayın. Örnək:
# ...
# 0057.
# 0056.
# ...
# with open('sirala.txt',mode='w',encoding='UTF-8') as file:
#     for i in range(1000,0,-1):
#      file.write(f'{i:04}.\n')



# from math import factorial
# import math
# print(factorial(5))
# print(dir(math))


# import re
# numbers='12345'

# result = re.match('e121',numbers)

# print(result)


# import random
 
# prints a random value from the list
# list1 = [1, 2, 3, 4, 5, 6]
# print(random.choice(list1))


# from datetime import date


# today=date.today()

# limited_day=date(2023,5,15)

# result=limited_day-today


# print('Endirimli qiymete son',result.days,'gun')


# Timedelta function demonstration
 
# from datetime import datetime, timedelta
 
# creating datetime objects
# date1 = datetime(2020, 1, 3)
# date2 = datetime(2020, 2, 3)
 
# # difference between dates
# diff = date2 - date1
# print("Difference in dates:", diff)
 
# # Adding days to date1
# date1 += timedelta(days = 4)
# print("Date1 after 4 days:", date1)
 
# Subtracting days from date1
# date1 -= timedelta(7)
# print("Date1 before 15 days:", date1)