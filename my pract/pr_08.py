import random

a = int(input("Кол-во чисел в списке: "))
sp = []
for i in range(a):
    num = random.randint(-100, 1000)
    sp.append(num)
    print(f"Сгенерировано число {i+1}: {num}")

print("список:", sp)
print("сумма:", sum(sp))
print("среднее арифметическое:", sum(sp) / len(sp))
print("максимальное:", max(sp))
print("минимальное:", min(sp))

for x in sp:
    if x < 0:
        print("отрицательное:", x)

print("наоборот:", sp[::-1])





