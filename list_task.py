

# ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']

# print(ferma.index('keci'))

# ferma.sort()
# print(ferma)

# print(dir(list))
# ferma.remove('at')
# ferma.append('toyuq')
# print(ferma)
# ferma.insert(0, 'keci')
# print(ferma)

# ferma.pop(4)
# del ferma([4])
# del ferma[2:5]
# del ferma[:len(ferma//2)]

# print(ferma)


# elave = ['at', 'qoyun', 'inek', 'inek', 'qoyun']
# ferma.extend(elave)

# ferma = ferma*3

# ferma.reverse()


# print(ferma.count('inek')/len(ferma)*100)

# another = ferma.copy()
# print(another)

# ferma.clear()

# =================
# 2-ci sual
# result = [0, 0]
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]

# for i in numbers:
#     if i < 0:
#         result[0] +=i
#     else:
#         result[1]+=i
# print(result)
# ==============

# 3-cu sual

# code = input("reqem daxil et: ")
# myList = []
# for i in code:
#     if not int(i) % 2 == 0:
#         myList.append(int(i))
# myList.reverse()
# print(myList)


# =============
# 5cu sual
# r=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]
# student_count=len(r)
# print(student_count)
# toplam_bal=0
# for i in r:
#     successfull_student=0
#     if i < 51:
#         kesilen_telebe+=1

# single = input("Tek reqemli bir eded girin: ")
# double = [int(i) for i in (single)][::-1]

# print(double)


# number=[10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62,77,22]
# number.sort()
# print(number)
# maxNumber=number
# print('minEded: ',minNumber)
# print('maxEded: ',maxNumber)

# print(number.pop())
# print(number.index(77))

# saxtaAd=number[-1]
# print(saxtaAd)


r = [31, 38, 69, 83, 83, 56, 38, 41, 96, 48,
     43, 60, 49, 47, 73, 60, 69, 96, 50, 74]

# totalCount = len(r)
# print(totalCount)

# defaultCount = 0
# yuksekAlanlar = 0

# for i in r:
#     if i < 51:
#         defaultCount += 1
#     elif i > 80:
#         yuksekAlanlar += 1
#     else:
#         pass
# kesilenler = defaultCount/len(r)*100
# print(yuksekAlanlar/len(r)*100)
# print(kesilenler)


# a="asd"
# b="asd"

# a=[4,5]
# b=[2,a,3]
# b[1].append(7)
# print(a)


# a=[1,2,3]
# b=[1,2,3]

# print(a is b)

# developer = {
#     "name": "Rufet",
#     "lastName": "Resulov",
#     "age": 26,
#     "hobby":["football","voleyball","basketball"]


# }

# print(developer["hobby"][0])

# keys for the dictionary
# alphabets = {'a', 'b', 'c'}

# numbers = [1,3,5]
# dictionary = dict.fromkeys(alphabets, numbers)
# print(dictionary)

users = [
    {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
    {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
    {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
]
username=input("Istifadeci adini daxil edin: ")
current_user=None
for info in users:
    if username==info['username']:
        current_user=info
        print('Istifadeci daxil oldu')


        
if current_user==None:
    print("bele bir istifadeci yoxdur")
    exit()