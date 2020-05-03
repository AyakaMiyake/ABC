N = int(input())
ali = list(map(int,input().split()))

cnt = 1
ans = 0

for a in ali:
    if a == cnt:
        cnt = cnt + 1
    else:
        ans = ans + 1

if ans == N:
    ans = -1

print(ans)