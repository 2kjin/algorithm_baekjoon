T = int(input())

for i in range(T):
    h, w, n = map(int,input().split())
    nums = n//h + 1
    floor = n % h
    if n % h == 0:
        nums = n//h
        floor = h
    res = floor*100+nums
    print(res)