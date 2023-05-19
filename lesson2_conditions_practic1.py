""" 

1)Istifadecinin sifresinin duzgun olub olmadigini yoxlayan kod yazin.
Sifre asagidaki qaydalara uymalidir.
Eger uymazsa istifadeciye sehvini print ederek bildirin :
a)En az 8 en cox 40 xarakterden ibarek olmalidir.
b)ancaq ingilis sriftlerinden ibaret olmalidir
c)Ancaq herf ve reqemlerden ibaret olmalidir.
d)Mutleq sekilde 1 boyuk ve 1 kicik herf olmalidir.
e)Mutleq sekilde 1 herf ve en az 1 reqem olmalidir.

# -----------------------

2)(Orta) Istifadeciden nomre isteyen bir proqram hazirlayin.
Nomreler +994 ile baslamali ve uzunlugu 13 ededden ibaret olmalidir.
Ilk xarakteri olan + cixmaq sertile ile ancaq ededlerden ibaret olmalidir

# -------------------------
3)3-cu sual 
Metni daxil edin :sehveler xosuma gelen sehve bu sehvedir
deyismek istediyin sozu daxil edin :sehve
neye deyismek istediyinizi girin:sehife
netice:sehifelerden xosuma gelen sehife bu sehifedir
"""


# 1ci sual cavab

# password = input('Zehmet olmasa sifrenizi daxil edin: ')

# if len(password) < 8 and len(password) > 40:
#     print("Sifrenin uzunlugu 8 ve 40 uzunlugu arasinda az olmalidir")
# elif not password.isascii():
#     print("Ingilis herfleri olmalidir")
# elif not password.isalnum():
#     print("herf ve reqemlerden ibaret olmalidir")
# elif password.isupper() or password.islower():
#     print("ancaq bir boyuk ve bir kicik herf olmalidir")
# elif password.isalpha() or password.isnumeric():
#     print("bir herf ve bir reqem olmalidir")
# else:
#     print('sifre qebul olundu')

# =================
# 2-ci sual

number = input('nomreni daxil edin: ')

if len(number) == 14:
    if number.startswith('+994'):
        if number[:1].isnumeric():
            print('nomre dogrudur')
        else:
            print('yalniz reqem daxil edin !')
    else:
        print('nomre +994 ile baslamalidir')
else:
    print('Uzunluq duzgun deyil')

# -------------------
# 3-cu sual

# text = input('Metni daxil edin: ')
# source =input('deyismek istediyin sozu daxil edin: ')
# target =input('neye deyismek istediyinizi girin: ')
# print('Netice:\n'+text.replace(source, target))

# number=1

# while number<=5:
#     print(number)
#     number+=1