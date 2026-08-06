def is_armstrong(num):
    num_sty = str(num)
    num_digits = len(num_sty)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_sty)
    return sum_of_powers == num

print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))



