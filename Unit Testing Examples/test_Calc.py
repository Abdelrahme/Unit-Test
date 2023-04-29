import grade_Calc
import unittest
class myunittest(unittest.TestCase):
    def test1(self):
        self.assertTrue(grade_Calc.calculate_grade(90), "should be true")
    def empty_list(self):
        self.assertTrue(grade_Calc.calculate_grade([]),"print empty list")
    def one_score(self):
        self.assertTrue(grade_Calc.calculate_grade([40]),"print containing one score")

    def multiple_score(self):
        self.assertTrue(grade_Calc.calculate_grade([60.55,21,59]),"containing multiple score")
    def out_range(self):
        self.assertTrue((grade_Calc.calculate_grade([-1,200])),"containig out range")
    if __name__=="__main__":
        unittest.main()