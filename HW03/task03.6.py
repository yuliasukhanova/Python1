# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def inc_func(text):
    string = []
    words = text.split(' ')
    for el in words:
        string_word = str(el)
        word = string_word[0].upper() + string_word[1:]
        string.append(word)
        beautiful_sting = " ".join(string)
    return beautiful_sting

print(inc_func(input("Введите слова в латинской транкрипции, разделенные пробелом: ")))