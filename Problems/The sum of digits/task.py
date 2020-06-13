three_digit_int = int(input())
digit_1 = three_digit_int // 100
digit_2 = (three_digit_int // 10) - (digit_1 * 10)
digit_3 = three_digit_int % 10
sum_three_digit = digit_1 + digit_2 + digit_3
print(sum_three_digit)
