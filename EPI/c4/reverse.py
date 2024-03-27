def reverse(x):
    result, n = 0, abs(x)
    while n:
        result = result * 10 + n % 10
        n //= 10
    
    return result if x > 0 else -result

print(reverse(123))
print(reverse(-345))