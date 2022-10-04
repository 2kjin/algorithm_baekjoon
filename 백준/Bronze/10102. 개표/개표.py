n = int(input())

lst = input()

a = lst.count('A')
b = lst.count('B')

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')