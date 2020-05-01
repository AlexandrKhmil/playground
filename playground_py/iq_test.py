def iq_test(numbers):
    a = [x % 2 for x in map(int, numbers.split(' '))]
    return (a.index(1) if sum(a) == 1 else a.index(0)) + 1

print(iq_test("2 4 7 8 10"))