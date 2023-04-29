import calculate_grade
import unittest
class myunittest(unittest.TestCase):
    def testone(self):
        self.assertTrue(calculate_grade.calculate_grade(80), "should be true")
    def empty_list(self):
        self.assertTrue(calculate_grade.calculate_grade([]),"print empty list")
    def list_containing_one_score(self):
        self.assertTrue(calculate_grade.calculate_grade([50]),"print containing one score")

    def list_containing_multiple_score(self):
        self.assertTrue(calculate_grade.calculate_grade([50,18,80,99]),"containing multiple score")
    def list_out_range(self):
        self.assertTrue((calculate_grade.calculate_grade([-10,155])),"containig out range")
    if __name__=="__main__":
        unittest.main()
