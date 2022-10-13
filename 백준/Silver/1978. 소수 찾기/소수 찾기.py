n = int(input())
nums = map(int, input().split())
res = 0
for i in nums:
    error = 0
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                error += 1
        if error == 0:
            res += 1
print(res)