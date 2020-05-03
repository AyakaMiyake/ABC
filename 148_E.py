def f(x):
    if x < 2:
        return 1
    else:
        return x * f(x-2)

E = int(input())
keta = len(str(E))

ans = 0
ansCnt = 0
#print(f(E))

if E%2 == 1:
    print(0)
    exit()

for i in reversed(range(1, keta+1)):
#    ans = ans + ((int(E/(10**i)) - ansCnt) * i)
    ans = ans + ((int(E/(10**i))) * i)
    ansCnt = ansCnt + (int(E/(10**i)) - ansCnt)


print(ans)