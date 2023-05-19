# Scopes,
# Globals,
# Decorator,
# Recursive Function,
# Callback Function,

# number=5

# if number==5:
#     a=3

# print(a)

# while number<10:
#     b=5
#     number+=1
# print(b)


# for i in range(8):
#     c=10

# print(c)

# z=10
# a=3
# c=6
# def f():
#     global z,a,c
#     z=z+1
#     a=a+1
#     c=c+1
# f()
# print(a,z,c)

# print(reqem1)

# print(locals())


# def f():
#     global z
#     z=10
#     def c():
#         global a
#         a=4
#     c()
#     print(a)
# f()

# print(z)

# a=5

# def test():
#     global a
#     a+=1

# # test()
# print(a)

# a=5
# def deyis():
#     global a
#     a+=2

# deyis()
# print(a)


# DECORATOR FUNCTION
# def upper(function):
#     def wrapper(word):
#         result = function(word)
#         result=result.upper()
#         return result
#     return wrapper


# @upper
# def salam(ad):
#     return f'Salam hormetli {ad}'

# @upper
# def necesen(ad):
#     return f'Necesen hormetli {ad}'

# @upper
# def isler(vezife):
#     return f'{vezife} nece gedir?'


# print(salam("Eli"))
# print(necesen("Eli"))
# print(isler("Hekimlik"))


# salam=upper(salam)
# print(salam("Rufet"))

# -------------------------

# logined = True


# def login_required(function):
#     def wrapper():
#         if logined:
#             result = function()
#             return result
#         else:
#             print("Zehmet olmasa login daxil edin")
#     return wrapper


# @login_required
# def ana_sehife():
#     return "Home sehifesine xos gelmisiniz"


# @login_required
# def login_sehife():
#     return "login  sehifesi"


# @login_required
# def hesab():
#     return "hesab cixarisi sehifesi"

# print(ana_sehife())
# print(login_sehife())
# print(hesab())

# Recursive function HomeWork 16


# eqs = {'ə':'e','ü':'u','ö':'o','ı':'i'}
# def replace_azeri_chars(func):
#     def wrapper(*args, **kwargs):
#         value = func(*args, **kwargs)
#         if isinstance(value, str):
#             result = ''
#             for i in value:
#                 result += eqs.get(i, i)
#             return result
#         return value
#     return wrapper

# @replace_azeri_chars
# def salam_ver(ad,soyad):
#     return 'Salam hörmətli {} {}, necəsiniz?'.format(ad, soyad)

# eqs = {'ə':'e','ü':'u','ö':'o','ı':'i'}


# def replace_azeri_chars(function):
#     def wrapper(*args, **kwargs):
#         value=function(*args, **kwargs)
#         if isinstance(value,str):
#             result=''
#             for i in value:
#                 result+=eqs.get(i,i)
#             return result
#         return value
#     return wrapper

# @replace_azeri_chars
# def salam_ver(ad, soyad,email):
# 	return 'Salam hörmətli {} {}, necəsiniz? sizin email adresiniz {}'.format(ad, soyad,email)

# print(salam_ver('Arif', 'Həsənov','ərif@mail.ru'))


