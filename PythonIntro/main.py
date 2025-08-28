#1
# name = int(input("Enter your name: "))
# age = int(input("Enter your age: "))
#
# print(f'Привет, {name}! Через год тебе будет {age + 1} лет.')
#
#


#2
# num = int(input("Enter a number: "))
#
# if num % 2 == 1:
#     print(f'{num} is even.')
# else:
#     print(f'{num} is odd.')
#


#3
# def factorial(n):
#     prod = 1
#     for i in range(1, n + 1):
#         prod *= i
#
#     return prod
#
# inp = int(input("Enter a number: "))
#
# print(factorial(inp))


#4
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end='    ')
#     print("\n")


#5
# li = []
#
# for i in range(1, 21):
#     li.append(i*i)
#
# for i in li:
#     print(i, end = " ")


#6
# def palindrome(num):
#     if num == num[::-1]:
#         return True
#     return False
#
# inp = input("Enter a number: ")
# if palindrome(inp):
#     print("The number is palindrome")
# else:
#     print("The number is not palindrome")


#7
# def check_how_often(s):
#     di = {}
#     words = s.split()
#     for word in words:
#         di[word] = di.get(word, 0) + 1
#
#     return di
#
# inp = input("Enter a phrase: ")
# norm = inp.lower()
#
#
# print(check_how_often(norm))


#8
# def sort_words(words, asc=True):
#     for i in range(len(words)):
#         for j in range(0, len(words) - i - 1):
#             if asc:
#                 if len(words[j]) > len(words[j+1]):
#                     words[j], words[j+1] = words[j+1], words[j]
#             else:
#                 if len(words[j]) < len(words[j+1]):
#                     words[j], words[j+1] = words[j+1], words[j]
#     return words
#
#
# w = ['hello', 'hi', 'wow']
#
# print(sort_words(w, True))


#9
# import random
# import string
#
#
# def generate(n):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ""
#
#     for i in range(n):
#         password += random.choice(characters)
#
#     return password
#
#
# num = int(input("Enter the length of the password: "))
# print(generate(num))


#10
# li1 = [1, 2, 5, 6, 7]
# li2 = [1, 3, 4, 6, 8]
#
# merged = []
#
# for i in li1:
#     if i not in merged:
#         merged.append(i)
#
# for i in li2:
#     if i not in merged:
#         merged.append(i)
#
# print(merged)


#11
# def get_file():
#     f = open("input.txt")
#     text = f.read()
#
#     lines = text.splitlines()
#     line_count = len(lines)
#
#     word_count = 0
#     for line in lines:
#         words = line.split()
#         word_count += len(words)
#
#     char_count = len(text)
#
#     return line_count, word_count, char_count
#
#
# print(get_file())


#12
# def my_max(lis):
#     max_num = 0
#     for i in lis:
#         if i > max_num:
#             max_num = i
#
#     return max_num
#
#
# li = [1, 30, 4, 20]
#
# print(my_max(li))


#13
# try:
#     a = float(input("Enter first num: "))
#     b = float(input("Enter second num: "))
#     result = a / b
#
#     print("Result: ", result)
# except ZeroDivisionError:
#     print("Never divide by zero!")
# except ValueError:
#     print("Only numbers, pls!")


#14
# nums = [n for n in range(1, 101) if n % 3 == 0 and n % 5 != 0]
#
# print(nums)


#15
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print(calendar.month(year, month))
