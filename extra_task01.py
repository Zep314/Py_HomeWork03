# Определите функцию, которая принимает римскую цифру в качестве аргумента 
# и возвращает ее значение в виде числового десятичного целого числа. 
# Вам не нужно проверять форму римской цифры.
# Современные римские цифры записываются путем выражения 
# каждой десятичной цифры числа, которое должно быть закодировано 
# отдельно, начиная с самой левой цифры. Таким образом, 
# 1990 отображается "MCMXC" (1000 = M, 900 = CM, 90 = XC), 
# а 2008 отображается "MMVIII" (2000 = MM, 8 = VIII). 
# Римская цифра для 1666, "MDCLXVI", использует каждую букву в порядке убывания.

# Пример: имя_вашей_функции ('XXI') # должно вернуть 21

def R2A(rim_num):  # конвертируем числа от 1 до 3999
    rim_dict = {
                ' ' : 0,
                'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000
               }
    rim_num = rim_num.upper()+' '
    res =0

    for i in range(len(rim_num)-1):
        if rim_dict[rim_num[i]] < rim_dict[rim_num[i+1]]: # заглядываем вперед на 1 цифру
            res -= rim_dict[rim_num[i]]
        else:
            res += rim_dict[rim_num[i]]
    return res

print(R2A('MCMXC'))
print(R2A('MMVIII'))
print(R2A('MDCLXVI'))
print(R2A('XXI'))
