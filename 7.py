import modzadnext
def main():
    try:
        N = int(input("Введите количество чисел: "))
        numbers = []
        for _ in range(N):
            numbers.append(int(input("Введите число: ")))
        
        max_sum_number = modzadnext.max_digit_sum(numbers)
        if max_sum_number is not None:
            print(f"Число с максимальной суммой цифр: {max_sum_number}")
            print(f"Сумма его цифр: {modzadnext.sum_of_digits(max_sum_number)}")
        else:
            print("Список чисел пуст.")

    except ValueError:
        print("Ошибка: Пожалуйста, введите целые числа.")

if __name__ == "__main__":
    main()