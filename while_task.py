# num=1
# result=0

# while num<=100:
#     result+=num
#     num+=1
# print(result)
# =============

# num = 10000

# while num > 0:
#     if num % 9999 == 0:
#         print(num)
#     num -= 1
#     break

# print(num)
# ============

# text='Men her gun Python oyrenirem'

# saitler='eiuao'

# counter=len(text)-1
# result=''
# while counter>=0:
#     result+=text[counter]
#     counter-=1
# print(result)
# ===================
# FOR TASK

# i=0

# for number in range(101):
#     i+=number

# print(i)
# ----------


# for i in range(100000,0,-1):
#     if(i%9999==0):
#         break
# print(i)
# ---------------
# sentence="Men her gun Python oyrenirem"
# vowels='aıoeuüəiöü'
# result=''

# for char in sentence:
#     if char not in vowels:
#         result+=char
# print(result)
# ====================
# vowels='aıoeuüəiöü'
# sentence=input("Cumle daxil edin: ")

# counter=0

# for i in sentence:
#     if i in vowels:
#         counter+=1

# print(counter)



# sentence='Men her gun Python oyrenirem'
# vowels='aıoeuüəiöü'
# result=''

# for i in sentence:
#     if i not in vowels:
#         result+=i

# print(result[::-1])   


personal=["Orxan","Zaur","Cavad"]

del personal[0]
print(personal)