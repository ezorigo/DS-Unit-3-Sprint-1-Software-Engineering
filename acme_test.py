import unittest
from acme import Product
from acme_report import generate_products, adj, noun


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product("Test Product")
        self.assertEqual(prod.weight, 20)
    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product("Test Product")
        self.assertEqual(prod.flammability, 0.5)
    def test_explode(self):
        """Test stealabiity"""
        prod = Product("Test Product", flammability=1.0, weight=50)
        self.assertEqual(prod.explode(), "...BABOOM!!")

class AcmeReportTests(unittest.TestCase):
    "Making sure Acme report works"
    def test_default_num_products(self):
        """Test for default num_products"""
        products = generate_products()
        self.assertEqual(len(products), 30)
    def test_legal_names(self):
        """Test that generated names for a default batch or products are all 
        valid possible to generate"""
        products = generate_products()
        names = [] 
        for product in range(len(products)):
            names.append(products[product][1]['name'])
        for name in range(len(names)):
            self.assertIn(" ", names[name])
        names_split = []
        for name in range(len(names)):
            split = names[name].split()
            names_split.append(split)
        flat_list = []
        for sublist in names_split:
            for name in sublist:
                flat_list.append(name)
        words = noun + adj
        for word in range(len(flat_list)):
            self.assertIn(flat_list[word], words)
        

if __name__ == '__main__':
    unittest.main()