def check_number(i):
    if i >= 2:
        if i == 2:
            return True
        for j in range(2, i):
            if i % j == 0:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    for i in range(1, 21):
        print(f"{i}: {check_number(i)}")
