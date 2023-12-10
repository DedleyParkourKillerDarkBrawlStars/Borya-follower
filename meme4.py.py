numbers_input = input("Введите список чисел")
numbers = [int(x) for x in numbers_input.split()]

print(max(numbers))