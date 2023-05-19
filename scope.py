# Scopes
# Globals
# Decorators
# Recursive Function


# number=5

# if number==5:
#     a=3

# # print(a)

# while a<number:
#     b=5
#     a+=1

# print(b)
# print(a)


# for i in range(1):
#     c=10
# print(c)

# z=10
# def f():
#     global simba
#     simba=30
#     t=20
#     print(globals())
#     print(locals())
#     def f2():
#         e=25
#         print(e)
# f()
# print(simba)
# ------------- 
# a=5

# def deyis():
#   global a  
#   a=a+2

# print(a)
# ---------------Decorators
# def salam(ad):
#     return f'Salam hormetli {ad}'
# def necesen(ad):
#     return f'necesiniz bugun {ad}'
# def isler(vezife):
#     return f'{vezife} nece gedir?'

# print(salam('Orxan'))
# print(necesen('Orxan'))
# print(isler('Muellimlik')


# def upper(function):
#     def wrapper(word):
#         result=function(word)
#         result=result.upper()
#         return result
#     return wrapper
# @upper
# def salam(ad):
#     return f'Salam hormetli {ad}'
# @upper

# def necesen(ad):
#     return f'necesiniz bugun {ad}'

# @upper
# def isler(vezife):
#     return f'{vezife} nece gedir?'


# necesen=upper(necesen)


# print(necesen("Eli"))
# print(salam("Eli"))
# print(isler("Muellimlik"))


# -----------

# logined=False


# def login_required(function):
#     def wrapper():
#         if logined:
#             result=function()
#         else:
#             result=print("Giris qadagandir")
#         return result
#     return wrapper
    


# @login_required
# def ana_sehife():
#     return ("ana sehifeye xos gelmissiniz")

# @login_required
# def login_sehifesi():
#     return ("login sehifesidir")



# @login_required
# def register():
#     return ("register sehifesi")


# @login_required
# def hesab():
#     return ("Hesab parametrleri sehifesi")


# print(ana_sehife())








#----------------- Recursive Function

 
# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))


