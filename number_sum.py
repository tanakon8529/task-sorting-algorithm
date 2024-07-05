def calculate_sum():
    result = 0
    for i in range(1, 11):
        if i % 2 == 0:
            result += i
        else:
            result += i * 2
    return result

if __name__ == "__main__":
    print(calculate_sum())
