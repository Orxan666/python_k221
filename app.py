# """
# str
# int
# float
# bool


# """

# # name=" "
# # # print(name)
# # print(type(bool(name)))

# # name="555.555"
# # print(float(name))

# # print(int('2')/3)

# # print(int('36')+int("35"))

# # print((str(45)+str(22)))


# # language = "Javascript"

# # if "y" in language:
# #    print(len('t'))
# # else:
# #    print(False)


# # speed=80

# # if speed>60 or speed<80:
# #     print("Zeif gedirsen")
# # elif speed>80 :
# #     print("Normal gedirsen")
# # elif speed>100:
# #     print("Ucassan?")
# # else:
# #     print("zehmet olmasa sureti artirin")


# # val="o_rxan"

# # if '_' or '.' in val:
# #     print("true")
# # else:
# #     print("simvol yoxdur")

# # print(round(35.5545))
# # print(round(22.454,1))
# # print(round(36.666,2))
# # print(3**2)
# # print(pow(3,3))
# # print(abs(4))

# # print(divmod(17,3))

# # print(False==False)

# # sentence="Men Python oyrenirem"

# # print(len(sentence))
# # print(sentence[-1])
# # val=-4
# # print(sentence[(val)])

# # val="Sireli necesen?"
# # print(val[-1])
# # name="Rufet"
# # print(name.lower())
# # print(name.upper())
# # site="www.compar.edu.az"

# # print(site.removeprefix("www.").removesuffix(".az"))

# # sentence="seyfelerden en cox bu seyfeni seyfe olaraq sevirem"
# # print(sentence.replace('seyfe','sehife'))

# # val="445566"
# # print(val.rjust(7,"%"))

# sifre="4169-7388-6242-1878"

# print(sifre[4:14].center(16,"*"))

# name=input("Salam Adinizi daxil edin: ")
# print(type(name))


# value1=input("1-ci reqemi daxil edin: ")
# value2=input("2-ci reqemi daxil edin: ")
# print(float(value1)* float(value2))
# -------------------
# value = "5382-1739-9201-9017"[9:].rjust(16,"*")

# print(value)

# print(pow(15 % 4,3))


# print(round(256.91872,2))
# print(round(256.91872,-2))

# val=str(34)

# print(val.ljust(5,"0"))

# val=float (input("bura reqem daxil edin: "))

# val=int(val)
# print(val)
# val=int(val)
# val=str(val)
# print(len(
# site=input('sayti daxil edin:')
# print(site.removeprefix('https://').removesuffix('.com').upper().replace("K","C"))

# val=input("Reqem daxil edin: ")
# val=int(val)

# if (val%3==0) and (val%7==0) and (val%8==0):
#     print('daxil etdiyiniz reqem 3 7 8 bolunur')
# else:
#     print("bolunmur")


# credit =input("kreditinizi daxil edin:")
# credit =int(credit)
# if(credit<2000):
#   print("kredit verilmir")
# elif(credit<10_000):
#    print("yekun-borc",credit*1.05,"olacaq")
# elif(credit<50_000):
#    print("yekun-borc",credit*1.04,"oldu")
# elif(credit<200000):
#    print("yekun-borc",credit*1.002,"alindi")
# elif(credit<500000):
#    print("yekun-borc",credit*1.002,"verelecek")
# else:
#    print("bele kredit movcud deyil")


# password = input("Sifrenizi daxil edin: ")


# if  len(password) < 8 or len(password) > 40:
#     print("Parolunuz 8-den boyuk 40 dan kicik olmalidir")
# elif not password.isascii():
#     print("Zehmet olmasa ingilis  srifti ile qeyd etmelisiniz")
# elif not password.isalnum():
#     print("Hem herf hemde reqem olmalidir sizin sifrede")
# elif  password.islower() or password.isupper():
#     print("Sizin sifrede en azi bir boyuk bir balaca herf olmalidir")
# elif  password.isnumeric() or password.isalpha():
#     print("Daxil etdiyiniz parolda mutleq sekilde 1 herf bir reqem olmalidir")
# else:
#     print("Daxil oldunuz")






number = input('Enter a phone number: ')

if not isinstance(number, str):
    print('Invalid input: phone number must be a string')
else:
    if len(number) == 14:
        if number.startswith('+994'):
            if number[1:].isnumeric():
                print('Phone number is valid')
            else:
                print('Invalid input: phone number must contain only digits')
        else:
            print('Invalid input: phone number must start with +994')
    else:
        print('Invalid input: phone number must contain exactly 14 characters')

print(len(number))