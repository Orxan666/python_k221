# reqem1=65
# binreqem1=bin(reqem1)
# print(binreqem1)
# binreqem1=hex(reqem1)
# binreqem1=oct(reqem1)
# print(binreqem1)

# a='4E'

# print(int(a,16))


# num=74
# ----2lik say sitemi kecid
# binnum=bin(num)
# 8-lik say sistemine kecid
# octnum=oct(num)
# 16liq say sistemine kecid
# hexnum=hex(num)
# print(num)


# -----------10luq say sistemine cevirmek ucun
# b='1001010'
# print(int(b,2))
# print(int('112',8))
# print(int('4a',16))

# print(chr(78))
# print(bin(ord("N")))

# letter='A'

# print(chr(ord(letter)+32))
# print(letter.upper())
# print(letter.lower())


# ++++++++++++++++++++++++++HOMEWORK 11
# HomeWork 11
# 3-cu sual
# text=input('metn daxil edin : ')
# for key in text:
#     print(bin(ord(key)))

# 1-ci sual

# sentence = 'Men Javascript oyrenirem'
# sentence=input("Cumle daxil edin : ")
# result = ''
# for char in sentence.lower():
#     if char.isalpha():
#         order = ord(char) - 96
#         result+=str(order)+','
# print(result)
# ========================

# 2-ci sual

# ferma = ('at', 'inek', 'inek', 'keci', 'qoyun', 'qoyun', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'inek', 'keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', 'keci', 'inek', 'toyuq', 'inek',
#          'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}


# ferma1 = ferma[:len(ferma)//2]
# ferma2 = ferma[len(ferma)//2:]
# # print(ferma2)
# f1_price = 0
# for animal in ferma1:
#     f1_price += qiymetler[animal]

# f2_price = 0
# for animal in ferma2:
#     f2_price += qiymetler[animal]

# if f1_price > f2_price:
#     debt = (f1_price - f2_price)/2
#     print("Boyuk qardas kicik qardasa {} manaat pul vermelidir".format(debt))
# else:
#     debt = (f2_price - f1_price)/2
#     print("Kicik qardas boyuk qardasa {} manaat pul vermelidir".format(debt))


# sentence="{} xos gelmisen"
# print(sentence)


# sentence = input("Cumle daxil edin: ")
# result = ""
# for char in sentence.lower():
#     if char.isalpha():
#         order = ord(char)-96
#         result += str(order)+","
#     else:
#         print("duzgun daxil edin ")
# print(result)
# ferma = ('at', 'inek', 'inek', 'keci', 'qoyun', 'qoyun', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'inek', 'keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', 'keci', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}
# ferma1=ferma[:len(ferma)//2]
# ferma2=ferma[len(ferma)//2:]
# f1_price=0
# for animal in ferma1:
#     f1_price+=qiymetler[animal]
   

# f2_price=0
# for animal in ferma2:
#     f2_price+=qiymetler[animal]  


    
# if f1_price>f2_price:
#     result=(f1_price-f2_price)/2
#     print("boyuk qardas kicik qardasa {} manat pul vermelidir".format(result))
# else:
    
#     result=(f2_price-f1_price)/2
#     print('kicik qrdas boyuk qardasa {} pul vermelidir'.format(result))



test = "Men Python 3 oyrenirem"



# test2 = "  👍  ".join(format(ord(i),"b") for i in test)

# print(test2)

# for char in test:
#     print(bin(ord(char)))



