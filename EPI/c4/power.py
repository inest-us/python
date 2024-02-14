def calculate_power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1/x

    while power:
        if power & 1:
            result *= x

        x, power = x * x, power >> 1

    return result

def main():
    print(calculate_power(2, 10)) # 1024
    print(calculate_power(3, 3)) # 27
    print(calculate_power(2, 5)) # 32

if __name__ == "__main__":
    main()    
