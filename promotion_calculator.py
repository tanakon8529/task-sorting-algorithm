def apply_promotions(products, promotions):
    for product in products:
        original_price = product['Price']
        best_price = original_price
        for promo in promotions:
            if product['ProductID'] in promo['ProductID']:
                if promo['DiscountType'] == 'Percent':
                    discount_price = original_price * (1 - promo['Discount'] / 100)
                elif promo['DiscountType'] == 'Baht':
                    discount_price = original_price - promo['Discount']
                best_price = min(best_price, discount_price)
        product['AfterDiscountPrice'] = best_price
    return products

if __name__ == "__main__":
    products = [
        {"ProductID": 1, "Name": "Computer Notebook", "Price": 15000, "Qty": 2, "AfterDiscountPrice": 0},
        {"ProductID": 2, "Name": "Printer", "Price": 3000, "Qty": 1, "AfterDiscountPrice": 0}
    ]
    promotions = [
        {"ID": 1, "Name": "Discount 15%", "Discount": 15, "DiscountType": "Percent", "ProductID": [1, 2, 3, 4, 5]},
        {"ID": 2, "Name": "Discount 100 Baht", "Discount": 100, "DiscountType": "Baht", "ProductID": [1, 3, 5]}
    ]
    print(apply_promotions(products, promotions))
