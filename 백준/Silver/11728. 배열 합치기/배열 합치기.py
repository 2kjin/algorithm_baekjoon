a, b = map(int,input().split())

a_lst = list(map(int,input().split()))
b_lst = list(map(int,input().split()))

res = a_lst + b_lst
res.sort()

print(*res)