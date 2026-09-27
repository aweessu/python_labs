import numpy as np


# Exercise 1

numbers = [4, -5, 3, -2, 0, 10, -4, 7, 1]


def positive_odd(numbers):
    return [x for x in numbers if x > 0 and x % 2 != 0]


def all_positive(numbers):
    return [abs(x) for x in numbers]


def count_positive_odd(numbers):
    return len([x for x in numbers if x > 0 and x % 2 != 0])


def average(numbers):
    return int(sum(numbers) / len(numbers))


def positive_negative_average(numbers):
    positive = [x for x in numbers if x > 0]
    negative = [x for x in numbers if x < 0]

    positive_average = int(sum(positive) / len(positive))
    negative_average = int(sum(negative) / len(negative))

    return positive_average, negative_average


def negative_to_zero(numbers):
    return [0 if x < 0 else x for x in numbers]


print(positive_odd(numbers))
print(all_positive(numbers))
print(count_positive_odd(numbers))
print(average(numbers))
print(positive_negative_average(numbers))
print(negative_to_zero(numbers))


# Exercise 2

def sum_numbers(n):
    return sum(range(1, n + 1))


n = int(input("Enter n: "))
print(sum_numbers(n))


# Exercise 3

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_short():
    return [fibonacci(i) for i in range(1, 25) if fibonacci(i) <= 32767]


print(fibonacci_short())


# Exercise 4

array1 = np.array([2, 3, 5, 6, 1, 2, 4])
array2 = np.array([1, 2, 1, 2, 1, 2, 3])

greater_than_3 = array1[array1 > 3]
squared = array1 ** 2
greater_than_average = array1[array1 > np.mean(array1)]

multiplication = array1 * array2
division = array1 / array2
addition = array1 + array2

print(greater_than_3)
print(squared)
print(greater_than_average)

print(multiplication)
print(division)
print(addition)


# Exercise 5

numbers_np = np.array([4, -5, 3, -2, 0, 10, -4, 7, 1])


def positive_odd_np(numbers):
    return numbers[(numbers > 0) & (numbers % 2 != 0)]


def all_positive_np(numbers):
    return np.abs(numbers)


def count_positive_odd_np(numbers):
    return len(numbers[(numbers > 0) & (numbers % 2 != 0)])


def average_np(numbers):
    return int(np.mean(numbers))


def positive_negative_average_np(numbers):
    positive = numbers[numbers > 0]
    negative = numbers[numbers < 0]

    return int(np.mean(positive)), int(np.mean(negative))


def negative_to_zero_np(numbers):
    return np.where(numbers < 0, 0, numbers)


print(positive_odd_np(numbers_np))
print(all_positive_np(numbers_np))
print(count_positive_odd_np(numbers_np))
print(average_np(numbers_np))
print(positive_negative_average_np(numbers_np))
print(negative_to_zero_np(numbers_np))


def sum_numbers_np(n):
    numbers = np.arange(1, n + 1)
    return np.sum(numbers)


n = int(input("Enter n: "))
print(sum_numbers_np(n))


def fibonacci_np():
    return np.array(
        [fibonacci(i) for i in range(1, 25) if fibonacci(i) <= 32767]
    )


print(fibonacci_np())