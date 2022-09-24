n = int(input())

a_res = 100
b_res = 100
for _ in range(n) :
  a, b = map(int, input().split())
  if a < b :
    a_res -= b
  elif a > b :
    b_res -= a

print(a_res)
print(b_res)