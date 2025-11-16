import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, z = map(int, input().split())
    x = list(map(int, input().split()))
    
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        length = r - l + 1
        
        # Binary search for maximum k such that x[r-k+1] - x[l+k-1] > z
        left, right = 0, length // 2
        while left < right:
            mid = (left + right + 1) // 2
            if x[r - mid + 1] - x[l + mid - 1] > z:
                left = mid
            else:
                right = mid - 1
        print(length - left)
