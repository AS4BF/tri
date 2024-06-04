import mod

def main():
    name = input("Введите ваше имя: ")
    greeting = mod.greet(name)
    print(greeting)

    description = mod.module_description()
    print(description)

if __name__ == "__main__":
    main()