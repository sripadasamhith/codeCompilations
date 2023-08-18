n = int(input())

def climbStairs(n: int) -> int:

    ways = [1, 2]

    if (n == 1):
        return 1
    else:
        for i in range(2, n):
            ways.append(ways[i - 1] + ways[i - 2])

    return ways[n - 1]

print(climbStairs(n))