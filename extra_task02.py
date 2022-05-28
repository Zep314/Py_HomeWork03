# Определите функцию, которая удаляет весь текст, следующий за любым из переданных маркеров 
# комментариев. Любые пробелы в конце строки также должны быть удалены.
# Пример: 
# Входные данные:
# «apples, pears # and bananas
# grapes
# bananas !apples          » 
# Выходные данные:
# «apples, pears
# grapes
# bananas»
# Функция может вызываться вот так:
# result = function("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

def my_grep(local_str,local_markers):
    lines = local_str.split('\n')

    for ch in local_markers:    # каждый символ комментария обрабатываем отдельно
        lines = [line[:line.find(ch)] for line in lines]

    ret = "\n".join(lines)
    return ret

my_str = 'apples, pears # and bananas\ngrapes\nbananas !apples'
my_markers = ['#','!']

print('===== Исходный текст:')
print(my_str)
print('===== Обработка:')
print(my_grep(my_str,my_markers))
