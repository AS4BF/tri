import modzadanie

def main():
    try:
        N = int(input("Введите количество элементов в списке: "))
        A = []
        for _ in range(N):
            A.append(int(input("Введите элемент списка: ")))
        
        max_element = modzadanie.find_max_element(A)
        max_count = modzadanie.count_max_elements(A)

        print(f"Максимальный элемент: {max_element}")
        print(f"Количество максимальных элементов: {max_count}")

    except ValueError:
        print("Ошибка: Пожалуйста, введите целые числа.")

if __name__ == "__main__":
    main()