# 1-dən 100-ə kimi olan bütün ədədlərin toplamını tapın (1+2+3+...+99+100)


# number=1
# result=0

# while number<101:
#     result+=number
#     number=number+1


# print(result)


# number=100000
# while number>0:
#     if number%9999==0:
#         print(number)
#         break
#     number-=1


sentence='Men her gun Python oyrenirem'
saitler='aıoueəiöü'

result=''
counter=len(sentence)-1

while counter>=0:
    char =sentence[counter]
    if char not in saitler:
        result+=char
    counter-=1
print(result)


person='Elektriklesdirdiklerimizdensinizmi'

for p in person:
    print(p)


for i in range(2,10,2):
    print(i)