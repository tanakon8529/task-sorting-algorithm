def calculate_change(grand_total, received_money):
    change = received_money - grand_total
    denominations = [500, 100, 50, 20, 10, 5, 1]
    change_breakdown = {}

    for denom in denominations:
        if change >= denom:
            count = change // denom
            change %= denom
            change_breakdown[f"Bank{denom}" if denom >= 20 else f"Coin{denom}"] = count

    return change_breakdown

if __name__ == "__main__":
    print(calculate_change(125, 200))
