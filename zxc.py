#1
project_name = 'Python for data analysis'
print('Course name is ' + project_name)

#2
users_astana = 4900
revenue_astana = 63000
arpu_astana = revenue_astana / users_astana

print('Astana: {} users, revenue {} tenge, ARPU {:.2f}'.format(
    users_astana, revenue_astana, arpu_astana
))
print(f'Astana: {users_astana} users, revenue {revenue_astana} tenge, ARPU {arpu_astana:.2f}')
print('Astana: %d users, revenue %d tenge, ARPU %.2f' % (
    users_astana, revenue_astana, arpu_astana
))

#3
users_almaty = int(input('Almaty users: '))
revenue_almaty = float(input('Almaty revenue: '))
arpu_almaty = revenue_almaty / users_almaty

print('Almaty: {} users, revenue {} tenge, ARPU {:.4f}'.format(
    users_almaty, revenue_almaty, arpu_almaty
))

#4
just_numbers = [2, 1, 5, 4, 3]
print(len(just_numbers))
print(sum(just_numbers))

#5
print(sorted(just_numbers))
print(sorted(just_numbers, reverse=True))

#6
just_numbers.append(55)
print(just_numbers)

#7
words = ['one', 'two', 'three']
print(sorted(words))

#8
queries_string = 'watch TV series online, sports news, movie poster, dollar rate, series this summer, python course, sports series'
print(queries_string.split(','))

#9
file_string = '003_logs_2017-11-03; 001_logs_2017-11-01; 005_logs_2017-11-05; 002_logs_2017-11-02; 004_logs_2017-11-04'
file_list = file_string.split(';')

for i in range(len(file_list)):
    file_list[i] = file_list[i].strip()

file_list_sorted = sorted(file_list)
file_list_sorted.append('006_logs_2017-11-06')
print(file_list_sorted)

#10
queriesList = [
    'watch TV series online',
    'sports news',
    'movie poster',
    'dollar exchange rate',
    'series this summer',
    'python course',
    'sports series'
]

print(','.join(queriesList))
print('\t'.join(queriesList))

#11
results = file_list_sorted
print('||'.join(results))

#12
sequence = ['Google Adwords', 'Yandex Direct', 'Facebook', 'VK', 'Partner']
print(sequence[1])
print(sequence[0])

#13
print(sequence[0:3])
print(sequence[:3])

#14
print(sequence[2:])
print(sequence[-1])

#15
print(sequence[2:-1])
print(sequence[-3:-1])
print(sequence[-3:4])
print(sequence[2:4])

#16
justNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(justNumbers[1::2])

#17
my_tuple = (100, 200, 300)
print('This is a tuple {}'.format(my_tuple))

#18
tuple_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

for i in range(len(tuple_list)):
    tuple_list[i] = tuple_list[i][:-1] + (100,)

print(tuple_list)

#19
tuples = (
    (4, 3, 2, 2, -1, 18),
    (2, 4, 8, 8, 3, 2, 9)
)

for t in tuples:
    product = 1
    for number in t:
        product *= number
    print(product)

#20
numbers = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)

averages = []

for t in numbers:
    averages.append(sum(t) / len(t))

print(averages)

#21
colors = (
    ('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime')
)

for color in ('White', 'White', 'Olive'):
    found = False
    for t in colors:
        if color in t:
            found = True
            break
    print(found)

#22
dictionary = {0: 10, 1: 20}
dictionary[2] = 30
print(dictionary)

#23
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

combined = {}
combined.update(dic1)
combined.update(dic2)
combined.update(dic3)
print(combined)

#24
n = 5
squares = {}

for x in range(1, n + 1):
    squares[x] = x * x

print(squares)

#25
dictionary = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
unique = {}

for key, value in dictionary.items():
    if value not in unique.values():
        unique[key] = value

print(unique)

#26
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined = d1.copy()

for key, value in d2.items():
    if key in combined:
        combined[key] += value
    else:
        combined[key] = value

print(combined)

#27
numbers = {4, 8, 1, 15, 3}
print(max(numbers))
print(min(numbers))

#28
items = {'apple', 'banana', 'orange'}
print(len(items))

#29
value = 'apple'
print(value in items)