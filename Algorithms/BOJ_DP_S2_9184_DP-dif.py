#------------------------
# #DP #Recursive
# https://www.acmicpc.net/problem/9184
#------------------------

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return dp[0][0][0]

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # dp 테이블의 범위가 21까지이므로 3번째에 위치.
    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a,b,c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

if __name__ == '__main__':
    dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
    dp[0][0][0] = 1
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == -1:
            break
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')