personInfo = {'виктор':'+777777777',
              'нурбол':'+77749685512',
              'искандер':'+78996251485'}

name = input("Введите имя: ")
name = name.lower()

if name in personInfo:
    print(personInfo[name])
else:
    print("Такого имени нет")
