def finding_gcd(a, b):
    ''' implements the greatest common divider algorithm '''
    while(b != 0):
        result = b
        a, b = b, a % b
    return result

def finding_gcd_rec(a, b):
    ''' implements the greatest common divider algorithm '''
    if b == 0:
        return a
    return finding_gcd_rec(b, a % b)

def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert(finding_gcd(number1, number2) == 3)
    assert(finding_gcd_rec(number1, number2) == 3)
    print('Tests passed!')

if __name__ == '__main__':
    test_finding_gcd()