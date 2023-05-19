# file=open("numbers.txt",mode="w")
# for i in range(1000,0,-1):
#     file.write(f"{str(i):>04}.\n")
# file.close()


def minify(file_path):
    file=open(file_path,mode="r")
    text=file.read()
    file.close()
    code="".join(text.split())
    file=open(file_path,mode="w")
    file.write(code)
    file.close()

try:
    file_path=input("Minify etmek istediyiniz faylin adresini girin:")
    minify(file_path)
    print("Fayl ugurla minify edildi")  
except FileNotFoundError:
    print("Fayl tapilmadi")




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