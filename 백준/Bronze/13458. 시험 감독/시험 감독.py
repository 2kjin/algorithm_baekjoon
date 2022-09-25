n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

res = n

for i in range(n) :
  cnt = a[i] - b

  if cnt > 0 :
    cnt1 = cnt//c
    cnt2 = cnt%c

    if cnt2 > 0 :
      cnt2 = 1
    
    res += cnt1 + cnt2

print(res)