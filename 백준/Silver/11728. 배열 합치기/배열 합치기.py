N = input()

a = list(map(int,input().split()))
b = list(map(int,input().split()))

res = a + b
res.sort()

print(' '.join(map(str,res)))