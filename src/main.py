def calculate(a, b):
    result = a + b
    return result


def main():
    print(calculate(10, 20))

    if calculate(1, 2) != 3:
        raise ValueError("Calculation failed")


if __name__ == "__main__":
    main()
