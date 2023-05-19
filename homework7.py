# '''
# users = [
#     {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
#     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
#     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# ]

# 1. istifadəçi username səhv girərsə belə bir istifadəçi yoxdur deyin
# 2. şifrəni səhv girərsə şifrəniz yanlışdır deyin
# 3. əgər blok olunubsa siz daxil ola bilməzsiniz deyin
# 4. əgər hər şey qaydasındadırsa “filankes giriş etdiniz” deyin

# '''
# users = [
#     {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
#     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
#     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# ]
# user_name=input('istifadeci adini daxil edin:')
# password=input('sifrenizi daxil edin:')
# finded_user=None
# for user in users:
#     if user["username"]==user_name:
#         finded_user=user
#         print(str(user["name"])+' xos geldiniz')
#         if user['password']==password:
#             if user['blocked']==False:
#                 print('daxil ola biler')
#             else:
#                 print('daxil ola bilmez')
#     else:
#         print('bele bir istifadeci movcud deyil')
#         break;

# =================================2-ci sual

'''
2. Bunları terminalda göstərin
    1. İstifadəçinin boyunu artırın
    2. Telefonun markasını dəyişərək Samsung edin
    3. İstifadəçinin adını silin
    4. İstifadəçinin ilk sifarişini silin
    5. İstifadəçinin sifarişlərinin başına ball əlavə edin
    6. Sonuna headphones əlavə edin
    user = {
        'name': 'Elnur',
        'height': 179,
        'phone': {
            'model': 'Iphone',
        },
        'orders': ['book', 'mouse', 'mousepad']
    }
'''
# user = {
#     'name': 'Elnur',
#     'height': 179,
#     'phone': {
#             'model': 'Iphone',
#     },
#     'orders': ['book', 'mouse', 'mousepad']
# }

# user['height']+=1
# user['phone']['model']='Samsung'
# del user['name']
# del user['orders'][0]
# user['orders'].insert(0,'ball')
# user['orders'].append('headphones')

# print(user)


# info = ["Resul", "Serifov", 35]

# # info=[''.join(info[:2]), 25]
# # info=[info[0]+' '+ info[1], 25 ]
# info.insert(0,info[0]+' ' + info[1])
# del1=info.pop(1)
# del2=info.pop(1)
# info[1]-=10

# # info[0]+=' '+info.pop(1)
# # info[1]-=10


# print(info)


# Dictionary əsasən istifadəçi sizə məhsul adı girəcək.
# Bu məhsulun mağazada olan qiymətini göstərən proqram hazırlayın.
#  Girilən məhsul mağaza da olmadığı halda "None" qaytarın.

shop = {
    "t-shirt": 59.00,
    "jeans": 75.00,
    "sweatshirt": 60.00,
    "shoe": 124.99,
    "jacket": 154.90
}
productName = input('Mehsulun adini daxil edin: ')
searchproductName = None
for key,value in shop.items():
    if key == productName:
        searchproductName= value
        print(value)
if not searchproductName:
    print(searchproductName)

# Mağazaya yeni məhsullar və qiymətlərini əlavə edin.
shop.update({'ball':73, 'mouse':150})
print(shop)

# Mağazada nə qədər məhsul olduğunu göstərin
print(len(shop))
# Məhsulların qiymətini 30% artırıb
#  yeni qiymətləri mağazaya əlavə edin.
for item,qiymet in shop.items():
    shop[item]=qiymet * 1.3
print(shop)