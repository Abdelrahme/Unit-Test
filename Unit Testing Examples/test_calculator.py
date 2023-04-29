import unittest
import calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(10,5),15)
        self.assertEqual(calculator.add(-1,5),4)
        self.assertEqual(calculator.add(0,-5),-5)
        self.assertEqual(calculator.add(True,-5),-4)

    def test_type_string(self):
        data = "test"
        with self.assertRaises(TypeError):
            result = calculator.addTen(data)

    def test_type_string(self):
        data = "test"
        with self.assertRaises(TypeError):
            result = calculator.addTen(data)

    def test_addTen(self):
        x = 15
        result = calculator.addTen(x)
        self.assertEqual(result,25)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10,5),5)
        self.assertEqual(calculator.subtract(-1,5),-6)
        self.assertEqual(calculator.subtract(0,5),-5)
        self.assertEqual(calculator.subtract(200,-5),205)

    def test_divide(self):
        self.assertEqual(calculator.divide(10,5),2)
        self.assertEqual(calculator.divide(0,5),0)
        self.assertEqual(calculator.divide(5,2),2.5)
        self.assertRaises(ValueError,calculator.divide, 0,0)
        self.assertRaises(ValueError,calculator.divide, 5,0)
        
        with self.assertRaises(ValueError):
            calculator.divide(10,0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(10,5),50)
        self.assertEqual(calculator.multiply(10,-5),-50)
        self.assertEqual(calculator.multiply(-5,-5),25)
        self.assertEqual(calculator.multiply(0,5),0)

# python -m unittest test_calculator.py
# python test_calculator.py
if __name__ == "__main__":
    unittest.main()