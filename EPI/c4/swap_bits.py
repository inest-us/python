def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask

    return x

def main():
    print(swap_bits(73, 1, 6)) # 11

if __name__ == "__main__":
    main()
