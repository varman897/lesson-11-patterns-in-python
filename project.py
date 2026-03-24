def mirrored_triangle(n):
    for i in range(1, n + 1):
        
        print(" " * (n - i) + "*" * i)


n = 5
mirrored_triangle(n)
