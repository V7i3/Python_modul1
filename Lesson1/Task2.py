# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = int(input('Введите z: '))


func1 = not(x or y or z) 
func2 = not(x) and not(y) and not(z)
print(func1 == func2)

