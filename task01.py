# Найти НОК двух чисел


# Найти наименьшее общее кратное через наибольший общий делитель 
# можно по формуле НОК(a, b)=a⋅b/НОД(a, b).

def NOD(a, b):      # наименьший общий делитель
    while b > 0:
        tmp = b
        b = a % b
        a = tmp
    return a

def NOK(a, b):      # наименьшее общее кратное
    return a * b // NOD(a, b)    

print(NOK(126,70))