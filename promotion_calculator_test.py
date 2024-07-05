import unittest
from promotion_calculator import apply_promotions

class TestPromotionCalculator(unittest.TestCase):
    def test_apply_promotions(self):
        products = [
            {"ProductID": 1, "Name": "Computer Notebook", "Price": 15000, "Qty": 2, "AfterDiscountPrice": 0},
            {"ProductID": 2, "Name": "Printer", "Price": 3000, "Qty": 1, "AfterDiscountPrice": 0}
        ]
        promotions = [
            {"ID": 1, "Name": "Discount 15%", "Discount": 15, "DiscountType": "Percent", "ProductID": [1, 2, 3, 4, 5]},
            {"ID": 2, "Name": "Discount 100 Baht", "Discount": 100, "DiscountType": "Baht", "ProductID": [1, 3, 5]}
        ]
        expected = [
            {"ProductID": 1, "Name": "Computer Notebook", "Price": 15000, "Qty": 2, "AfterDiscountPrice": 12750},
            {"ProductID": 2, "Name": "Printer", "Price": 3000, "Qty": 1, "AfterDiscountPrice": 2550}
        ]
        self.assertEqual(apply_promotions(products, promotions), expected)

if __name__ == "__main__":
    unittest.main()
