
# HOMEWORK 9

# animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')
# farm = ('inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at', 'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 'at', 'qoyun', 'inek', 'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', 'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

# text = """
# Axtarilan Heyvan: {}
# {}
# Fermadaki {} sayi:  {}
# Diger heyvanlara olan faizi: {}%
# {} umumi qiymeti: {} AZN
# """.format(
#    str(animal),
#    '-' * 20,
#    animal,
#    str(farm.count(animal)),
#    str(farm.count(animal)/len(farm) * 100),
#    animal,
#    (str(farm.count(animal) * qiymetler[animal]))
# )

# print(text)
# =========================
# HOMEWORK 8


# num, text = input("Cumleni daxil edin: ").split()

# num = int(num)

# result = text+" "

# for i in range(1, num):
#     result += text+" "

# print(result.strip())


# x = input("Cumle daxil edin: ")
# newlist = list(x.split(" "))
# newlist2 = (newlist[1] + ' ') * int(newlist[0])
# print(newlist2)
# x = "This is an example!"

# alma=x[::-1].split(" ")
# alma.reverse()
# print(alma)


numbers = [2384, 12385, 13226, 653, 12362423]
# dic ={}

# for i in numbers:
#     dic[i]=len(str(i))

# print(dic)

# result={str(i):len(str(i))for i in numbers}
# print(result)


# -100-dən müsbət 100-ə qədər ədədlər arasında 7-yə bölünən
#  ədədlərin 3-ə vurulmasından ibarət bir list qurun.
#  Bunun üçün range və list comprehensions istifadə edin.


# for i in range(-100, 100 ):
# print(i)
# result = [i*3 for i in range(-100, 100)if i % 7==0 ]
# print(result)


'''
Istifadəçi sizə bir input vasitəsilə bunun kimi
bir məlumat girəcək:
input: firstname Elcin, username elchina, 
birthday 18-08-2000
Bu inputa əsasən yuxarıdakı dictionary-ni 
update edin ve istifadəçiye gosterin. Misal yuxarıdakı 
inputa əsasən dictionary son halı 
aşağıdakı kimi olacaq.


user_info = {
    'firstname': 'Elcin',
    'lastname': 'Huseynov',
    'username': 'elchina',
    'password': '12345',
    'birthday': '18-08-2000'
}'''

# user_info = {
#     'firstname': 'Elvin',
#     'lastname': 'Huseynov',
#     'username': 'elivin_h_ov',
#     'password': '12345',
#     'birthday': '19-08-1997'
# }

# user_info.update({'firstname': 'Elcin',
#     'lastname': 'Huseynov',
#     'username': 'elchina',
#     'password': '12345',
#     'birthday': '18-08-2000'})

# print(user_info)


# user_info = {
#     'firstname': input('Adinizi daxil edin: '),
#     'lastname':input('Soyadi daxil edin: '),
#     'username': input('Logini daxil edin: '),
#     'password':input('Sifrenizi daxil edin: '),
#     'birthday': input('Dogum tarixini dd-mm-yyyy formatinda daxil edin: ')
# }
# print(user_info)


# user_info = {
#     'firstname': 'Elvin',
#     'lastname': 'Huseynov',
#     'username': 'elivin_h_ov',
#     'password': '12345',
#     'birthday': '19-08-1997'
# }


user_info = {
    'firstname': 'Elvin',
    'lastname': 'Huseynov',
    'username': 'elchina',
    'password': '12345',
    'birthday': '18-08-2000'
}

user_input = 'firstname Elcin, username elchina, birthday 18-08-2000'
info = user_input.split(',')
new_info = {}
for data in info:
    data=data.split() 
    new_info[data[0]] = data[1]
user_info.update(new_info)
print(user_info)




users = [
    {'name': 'Akif',
     'username': 'a456',
     'password': '1234',
     'blocked': False},
    {'name': 'Senan',
     'username': 'sm_ov',
     'password': '5423s',
     'blocked': False},
    {'name': 'Kamal',
     'username': 'km123',
     'password': '34-kk-325',
     'blocked': True}
]

username = input("Username daxil edin: ") 
password = input("Password daxil edin: ")

for i in users:
    if i['username'] == username:
        if i['password'] == password:
            if i['blocked']:
                print("Sizin hesabiniz bloklanib!")
            else:
                print("Daxil oldunuz!")
        else:
            print("Sifre duzgun deyil!")
        break
else:
    print("Istifadeci tapilmadi")