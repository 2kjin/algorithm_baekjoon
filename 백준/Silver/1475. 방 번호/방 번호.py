n = input()
ans = [0] * 10

for i in range(len(n)):
    number = int(n[i])
    if number == 6 or number == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[number] += 1
 
print(max(ans))