

# SET HOME WORK=============


# baliqlar = {
#     'qelseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
#     'yumurtlama', 'dis yoxdur', '4 ayaq'
# }

# cuculer = {
#     'toraks teneffusu', 'urek yoxdur', '6 ayaq',
#     'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz',
#     'dis yoxdur'
# }

# amfibialar = {
#     'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq',
#     '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'koteks vardir',
#     'yumurtlama', 'dis yoxdur'
# }

# surunenler = {
#     'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
#     'dis var'
# }

# quslar = {
#     'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
#     'yumurtlama', 'dis yoxdur'
# }

# memeliler = {
#     'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
#     'dogma', 'dis vardir'
# }

# sinifler = {
#     'baliqlar': baliqlar,
#     'cuculer': cuculer,
#     'amfibialar': amfibialar,
#     'surunenler': surunenler,
#     'quslar': quslar,
#     'memeliler': memeliler,
# }

# 1. Quşların xüsusiyyətlərinə `"2 ayaq"` əlavə edin.
# 2. Balıqların xüsusiyyətlərindən `"4 ayaq"` məlumatını çıxarın
# 3. Amfibialar ilə cücülərin ortaq cəhətlərini göstərən kod yazın
# 4. Balıqlar ilə amfibiaların fərqli cəhətlərini göstərən kod yazın
# 5. Balıqlar ilə heç bir ortaq cəhətə sahib olmayan sinifi tapan kod yazın
# 6. Quşlar ilə ən çox ortaq cəhətə sahib olan sinifi tapın
# 7. İstifadəçi input ilə sizə bəzi özəlliklər girəcək. Siz həmin özəlliklərə əsasən heyvanın hansı sinifə aid ola biləcəyini təxmin edən kod yazın. Örnək
# input: dis yoxdur, agciyer teneffusu, korteks vardir
# output: Bu heyvan quslar sinifine aid ola biler


# 1
# quslar.add(' 2ayaq')

# 2
# baliqlar.remove('4 ayaq')

# 3
# accomplice=amfibialar.intersection(cuculer)

# 4
# between_diff =baliqlar.difference(amfibialar)

# 5


# for ad, sinif in sinifler.items():
#     if ad != 'baliqlar' and not baliqlar.intersection(sinif):
#         print(ad)

# 6
# max_ad=''
# max_say=-1

# for ad,sinif in sinifler.items():
#     intersection=sinif.intersection(quslar)
#     # print(intersection)
#     say=len(intersection)
#     print(ad,say)
#     if say>max_say and sinif !=quslar:
#         max_ad=ad
#         max_say=say


# print(f'quslar ile en cox ortaq ozelliye sahib olan sinif {max_ad} sinifidir sayilarida {max_say}')

# 7
# text=input('ozellikleri daxil edin: ')
# spes=text.split(', ')
# spes=set(spes)

# for ad ,sinif in sinifler.items():
#     if spes.issubset(sinif):
#         print(f'bu canli {ad} sinifine aid ola biler')


# ----------------------ERROR handler


# # result=int(bolunen)/int(bolen)

# # print(result)

# try:
#     result=int(bolunen)/int(bolen)
#     print(result)
# except ValueError as error_message:
#     print(f'zehmet olmasa reqem daxil edin.Xetanin bas verdiyi error:{error_message}')
# except ZeroDivisionError as error_message:
#     print('reqem 0-a bolune bilmez xeta sebebi: ',error_message)
# except Exception as error_message:
#     print('proqramda xeta bas verdi')
# finally:
#     print('Proqram bitti')
# bolunen=input('Bolunen: ')
# bolen=input('Bolen: ')

# def bolme(a,b):
#     if b==0:
#         raise ZeroDivisionError('0 reqemi bolunen kimi daxil edile bilmez')
#     result=int(a)/int(b)
#     print(result)

# bolme(bolunen,bolen)


# file=open('text.txt',encoding='UTF-8')
# content=file.read()
# print(content.splitlines(keepends=True))

# with open('list.txt','w') as file:
#     for i in range(1,100):
#         file.write(f'{i:03}')







# +++++++++++++++++++++++++++++++++++++++++++++++++++++++








# bolunen=input('Bolunen: ')
# bolen=input('Bolen: ')


# try:
#     result=int(bolunen)/int(bolen*eded)
#     print('Netice' ,result)

# except ValueError as error_message:
#     print('ancaq eded girmek olar')
# except ZeroDivisionError as error_message:
#     print('hec bir eded sifira bolune bilmez!')
# except Exception as error_message:
#     print(f"Bilinmeyen xeta bas verdi.Xeta mesaji: {error_message}")
# finally:
#     print('Proqram bitti')

# -----------------------------

# bolunen=input('Bolunen: ')
# bolen=input('Bolen: ')

# def bolme(a,b):
#     if not a:
#         raise ValueError("bolunen bos ola bilmez")
#     result=int(a)/int(b)
#     print('Netice: ',result)

# bolme(bolunen,bolen)


# =============FILE HANDLE===========

# file=open('text.txt',encoding='UTF-8')
# content=file.read()
# print(content)

# print(content.splitlines(keepends=True))

# ================++++++++++++======================================

# ---------------ERROR HANDLING HOMEWORK

# file=open("numbers.txt",mode="w")
# for i in range(1000,0,-1):
#     file.write(f"{str(i):>04}.\n")
# file.close()


# def minify(file_path):
#     file=open(file_path,mode="r")
#     text=file.read()
#     file.close()
#     code="".join(text.split())
#     file=open(file_path,mode="w")
#     file.write(code)
#     file.close()

# try:
#     file_path=input("Minify etmek istediyiniz faylin adresini girin:")
#     minify(file_path)
#     print("Fayl ugurla minify edildi")  
# except FileNotFoundError:
#     print("Fayl tapilmadi")




# test = ['salam', 'necesn', 'yaxsiyam']
# test = 'salam necesn yasixam'

# result = ''.join(test.split())

# print(result)




# file = open('salary.txt', mode='r', encoding='utf-8')
# lines = file.readlines()

# new_lines = []

# for line in lines:
#     new_lines.append(line.split())


# for t in new_lines:
#     print(t[-2])


# new_lines.sort(key= lambda x: x[-2])

# print(new_lines)





# file = open('salary.txt', mode='r', encoding='utf-8')
# file.close()
# with open('salary.txt' , 'r', encoding='UTF-8') as file:
#     rows = file.readlines()

# rows.sort(key=lambda row: int(row.split()[2]), reverse=True)

# with open('salary.txt', 'w', encoding='UTF-8') as file:
#     file.writelines(rows)



