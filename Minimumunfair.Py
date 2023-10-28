arr = list(map(int,  input().split() ))

k = int(input())

arr.sort()

ans = 999999

for i in range(0, len(arr)-k+1):

    temp = arr[i : i+k]

    res = max(temp) - min(temp)

    if res < ans:

        ans = res

print(ans)
