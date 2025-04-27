"""
Инженеры завода считают, что наиболее эффективный путь, который может совершить погрузчик, — это поездка из некоторой начальной зоны в конечную, а затем возвращение по тому же маршруту обратно. Такая последовательность перемещений формирует так называемый «идеальный маршрут».

Вам необходимо найти длину самого длинного «идеального маршрута» в записи перемещений погрузчика.

Формат ввода
Первая строка содержит одно целое число n (1 ≤ n ≤ 1 0 4 10^410 
4
 ) — количество записей о перемещениях погрузчика.

Вторая строка содержит n целых чисел a₁, a₂, ..., aₙ (1 ≤ aᵢ ≤ 1 0 9 10^910 
9
 ) — последовательность зон, через которые проехал погрузчик.

Формат вывода
Выведите одно целое число — длину самого длинного «идеального маршрута» в записи перемещений. Если такого маршрута не существует, выведите 0.

Пример 1
Ввод	Вывод
7
1 2 3 4 3 2 1
7
Пример 2
Ввод	Вывод
5
1 2 3 4 5
0
Пример 3
Ввод	Вывод
10
1 2 3 4 5 5 4 3 2 1
10
Пример 4
Ввод	Вывод
6
1 2 3 1 2 3
0
Пример 5
Ввод	Вывод
3
1 1 2
2
"""


number = int(input('Общее количество зон: '))
numbers_str = input('Последовательность зон: ')
numbers_list = [int(num) for num in numbers_str.split()]
print(numbers_list)

arr_forward = []
arr_back = []

way = 0

for numb in numbers_list:
    if not arr_forward or numb > arr_forward[-1]:
        arr_forward.append(numb)
    else:
        break
print(arr_forward)

print (numbers_list[::-1])
for numb in numbers_list[::-1]:
    if not arr_back and numb != arr_forward[1]:
        break
    elif 


# max_len = 0
# stack = []
# for num in numbers_list:
#     if not stack or num > stack[-1]:
#         stack.append(num)
#     elif num == stack[-1]:
#         stack.append(num)
#     else:
#         if stack == stack[::-1]:
#             max_len = max(max_len, len(stack))
#         while stack and num < stack[-1]:
#             stack.pop()
#         stack.append(num)
# if stack == stack[::-1]:
#     max_len = max(max_len, len(stack))
# print(max_len if max_len > 1 else 0)


