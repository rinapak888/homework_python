import os

title = input('Файл: ')
text = input('Текст для замены: ')
new_text = input('Текст на замену: ')
way = os.path.abspath(title) #вложенный модуль в модуле os, возвращает нормализованный абсолютный путь

def swap(title, text, new_text): 
    t1 = os.path.exists(way) #возвращает True, если path указывает на существующий путь или дескриптор открытого файла
    t2 = os.path.isfile(way) #является ли путь файлом
    t3 = way[-4:] == '.txt' #последние 4 символа строки (срез)
    if t1 and t2 and t3 == True:
        print('Файл существует, у него верное расширение')

        with open(title) as f: #шаблон для открытия текстового файла и чтения его содержимого, конструкция with гарантирует закрытие файла автоматически, open() принимает имя файла и режим в качестве аргументов, открывает файл в режиме только для чтения
            tex_t = f.read() #для чтения содержимого файла 
        with open(title, 'w') as f:
            tex_t = tex_t.replace(text, new_text) #возвращает копию строки; старая подстрока заменяется новой 
            f.write(tex_t) #записывает переданную строку/данные в файл
            print('Содержимое файла перезаписано') 
    else:
        print('Error')

swap(title, text, new_text) 