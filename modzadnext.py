def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

def max_digit_sum(numbers):
    if not numbers:
        return None
    return max(numbers, key=sum_of_digits)