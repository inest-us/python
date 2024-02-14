def closet_num_same_weight(x):
    NUM_BITS = 64
    for i in range(NUM_BITS - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1))
            return x
    
    raise ValueError("All bits are 0 or 1")

def main():
    print(closet_num_same_weight(7)) # 11
    print(closet_num_same_weight(6)) # 5
    print(closet_num_same_weight(8)) # 4

if __name__ == "__main__":
    main()